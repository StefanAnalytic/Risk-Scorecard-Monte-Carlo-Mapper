import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde

def create_3d_scatter(df_sim: pd.DataFrame, output_path: str = "results/3d_simulation_report.html"):
    """Generiert einen übersichtlichen 3D-Report mit Risiko-Ellipsoiden statt Punktwolken."""
    
    fig = go.Figure()
    
    # Farbpalette für die Tools
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    # Konfidenzintervalle (Zwiebelschichten)
    levels = [0.5, 0.9, 0.99]
    opacities = [0.5, 0.3, 0.1] # Von innen nach außen transparenter

    options = df_sim['Option'].unique()
    
    for idx, option in enumerate(options):
        df_opt = df_sim[df_sim['Option'] == option]
        color = colors[idx % len(colors)]
        
        # Daten für KDE vorbereiten
        data = np.vstack([df_opt['Kosten_Sim'], df_opt['Zeit_Sim'], df_opt['Fit_Sim']])
        
        try:
            # Kerndichteschätzung (KDE) berechnen
            kde = gaussian_kde(data)
            
            # Grid für die Auswertung erstellen
            x, y, z = np.mgrid[
                df_opt['Kosten_Sim'].min():df_opt['Kosten_Sim'].max():20j,
                df_opt['Zeit_Sim'].min():df_opt['Zeit_Sim'].max():20j,
                df_opt['Fit_Sim'].min():df_opt['Fit_Sim'].max():20j
            ]
            
            grid_coords = np.vstack([x.ravel(), y.ravel(), z.ravel()])
            density = kde(grid_coords).reshape(x.shape)
            
            # Schwellenwerte für Dichte-Level berechnen
            density_sorted = np.sort(density.ravel())
            cumulative_density = np.cumsum(density_sorted)
            cumulative_density /= cumulative_density[-1]
            
            for level_idx, level in enumerate(levels):
                # Finde den Dichtewert, der das gewünschte Perzentil umschließt
                threshold = density_sorted[np.searchsorted(cumulative_density, 1 - level)]
                
                # Isosfläche (Ellipsoid) hinzufügen
                fig.add_trace(go.Isosurface(
                    x=x.ravel(),
                    y=y.ravel(),
                    z=z.ravel(),
                    value=density.ravel(),
                    isomin=threshold,
                    isomax=density.ravel().max(),
                    opacity=opacities[level_idx],
                    surface_count=1,
                    colorscale=[[0, color], [1, color]],
                    showscale=False,
                    name=f"{option} ({int(level*100)}% Konfidenz)",
                    legendgroup=option,
                    showlegend=(level_idx == 0) # Nur das innerste Level in der Legende zeigen
                ))
                
        except np.linalg.LinAlgError:
            print(f"⚠️ Warnung: Konnte Ellipsoid für {option} nicht berechnen (zu wenig Varianz).")
            # Fallback: Nur den Mittelpunkt zeichnen
            centroid = df_opt[['Kosten_Sim', 'Zeit_Sim', 'Fit_Sim']].mean()
            fig.add_trace(go.Scatter3d(
                x=[centroid['Kosten_Sim']], y=[centroid['Zeit_Sim']], z=[centroid['Fit_Sim']],
                mode='markers', marker=dict(color=color, size=10), name=f"{option} (Mittelpunkt)"
            ))

    # 3. Mathematisches Ranking (unverändert)
    summary = df_sim.groupby('Option').agg({
        'Kosten_Sim': 'mean', 'Zeit_Sim': 'mean', 'Fit_Sim': 'mean'
    }).reset_index()
    summary['Total_Score'] = (summary['Kosten_Sim'] + summary['Zeit_Sim'] + summary['Fit_Sim']) / 3
    summary = summary.sort_values(by='Total_Score', ascending=False)

    # Namen in der Legende mit Score aktualisieren
    for _, row in summary.iterrows():
        score_pct = round(row['Total_Score'] * 100, 1)
        fig.for_each_trace(lambda t: t.update(name=f"<b>{t.name}</b> (Score: {score_pct}%)") if t.name.startswith(row['Option']) else None)

    # 4. Layout
    fig.update_layout(
        title='Decision Intelligence: 3D Risk Mapping (Übersicht)',
        scene=dict(
            xaxis=dict(title='Kosten-Perf.'),
            yaxis=dict(title='Zeit-Perf.'),
            zaxis=dict(title='Strategischer Fit'),
            bgcolor='white'
        ),
        legend=dict(title="<b>Ranking & Risiko</b>", yanchor="top", y=0.9, xanchor="left", x=1.1, font=dict(size=13)),
        margin=dict(l=0, r=250, b=0, t=50)
    )

    fig.write_html(output_path)
    print(f"✅ Übersichtlicher Report mit Risiko-Ellipsoiden erstellt: '{output_path}'")