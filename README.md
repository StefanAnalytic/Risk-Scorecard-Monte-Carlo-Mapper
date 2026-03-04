# 3D Risk Scorecard Engine

Eine deterministische Risiko-Pipeline, die qualitative Scorecard-Bewertungen in eine dynamische Monte-Carlo-Simulation übersetzt. Das Tool nimmt gewichtete Risikofaktoren (Kosten, Zeit, Strategic Fit) und visualisiert die resultierenden Unsicherheiten als 3D-Konfidenz-Ellipsoide.

## 📂 Struktur & Module

### Root
* `main.py`: Orchestrierung der gesamten Pipeline.
* `requirements.txt`: Abhängigkeiten (Pandas, Plotly, Scipy).

### /src (Logik)
* `normalizer.py`: Skalierung der CSV-Rohdaten auf 0.0 - 1.0.
* `simulator.py`: Berechnung der 1.500 Monte-Carlo-Punkte pro Option.
* `visualizer.py`: Erzeugung der 3D-KDE-Ellipsoide (Wolken) und HTML-Export.

### /data & /results
* `/data/input_data.csv`: Zentrale Datenbank für Optionen und Risiken.
* `/results/3d_simulation_report.html`: Der fertige visuelle Output.