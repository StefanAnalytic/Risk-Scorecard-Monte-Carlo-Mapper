import numpy as np
import pandas as pd

def run_monte_carlo(df_norm, iterations=1500): # Wir nennen es iterations
    results = []
    
    for _, row in df_norm.iterrows():
        for _ in range(iterations):
            # Simulation der normalisierten Werte (0 bis 1 für den Plot)
            sim_k = row['Kosten_Norm'] * (1 + np.random.normal(0, row['Risk_K']))
            sim_z = row['Zeit_Norm'] * (1 + np.random.normal(0, row['Risk_Z']))
            sim_f = row['Fit_Norm'] * (1 + np.random.normal(0, row['Risk_F']))
            
            # Real-Werte für das Hover-Menü (Euro, Monate, Punkte)
            real_k = row['Kosten'] * (1 + np.random.normal(0, row['Risk_K']))
            real_z = row['Zeit'] * (1 + np.random.normal(0, row['Risk_Z']))
            real_f = row['Fit'] * (1 + np.random.normal(0, row['Risk_F']))
            
            results.append({
                'Option': row['Option'],
                'Kosten_Sim': sim_k,
                'Zeit_Sim': sim_z,
                'Fit_Sim': sim_f,
                'Kosten_Euro': real_k,
                'Zeit_Monate': real_z,
                'Fit_Punkte': real_f
            })
            
    return pd.DataFrame(results)