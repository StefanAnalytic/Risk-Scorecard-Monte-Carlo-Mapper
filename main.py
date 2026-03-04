import pandas as pd
from src.normalizer import normalize_data
from src.simulator import run_monte_carlo
from src.visualizer import create_3d_scatter

def run_pipeline():
    print("🚀 Starte Decision Intelligence Pipeline...")
    
    # 1. Daten laden
    print("📂 Lade Optionen aus data/input_data.csv...")
    df_raw = pd.read_csv("data/input_data.csv")
    
    # 2. Normalisieren
    print("⚙️ Normalisiere KPIs...")
    df_norm = normalize_data(df_raw)
    
    # 3. Monte Carlo Simulation
    # WICHTIG: Name muss iterations sein, passend zur simulator.py
    print("🎲 Führe dynamische Monte Carlo Simulation durch...")
    df_sim = run_monte_carlo(df_norm, iterations=1500) 
    
    # 4. Visualisierung
    print("📊 Generiere 3D-Report...")
    create_3d_scatter(df_sim)
    
    print("✨ Pipeline erfolgreich abgeschlossen!")

if __name__ == "__main__":
    run_pipeline()