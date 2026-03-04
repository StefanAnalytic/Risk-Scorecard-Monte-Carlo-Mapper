import pandas as pd

def normalize_data(df):
    """Normalisiert Kosten, Zeit und Fit auf eine Skala von 0 bis 1."""
    df_norm = df.copy()
    
    # Kosten: Kleiner ist besser (Invertiert)
    # Wenn alle Kosten gleich sind, setzen wir 1.0 (Bestwert)
    if df['Kosten'].max() != df['Kosten'].min():
        df_norm['Kosten_Norm'] = (df['Kosten'].max() - df['Kosten']) / (df['Kosten'].max() - df['Kosten'].min())
    else:
        df_norm['Kosten_Norm'] = 1.0
        
    # Zeit: Kleiner ist besser (Invertiert)
    if df['Zeit'].max() != df['Zeit'].min():
        df_norm['Zeit_Norm'] = (df['Zeit'].max() - df['Zeit']) / (df['Zeit'].max() - df['Zeit'].min())
    else:
        df_norm['Zeit_Norm'] = 1.0
        
    # Fit: Größer ist besser
    if df['Fit'].max() != df['Fit'].min():
        df_norm['Fit_Norm'] = (df['Fit'] - df['Fit'].min()) / (df['Fit'].max() - df['Fit'].min())
    else:
        df_norm['Fit_Norm'] = 1.0
        
    return df_norm