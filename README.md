<div align="center">

# 🎲 3D Risk Scorecard Engine

[![Python](https://img.shields.io/badge/Language-Python_3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SciPy](https://img.shields.io/badge/Math-SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org/)
[![Plotly](https://img.shields.io/badge/3D_Viz-Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Simulation](https://img.shields.io/badge/Stochastics-Monte_Carlo-F7931E?style=for-the-badge)](#)

**Eine deterministische Risiko-Pipeline, die qualitative Scorecard-Bewertungen in eine dynamische Monte-Carlo-Simulation übersetzt.**

*Nimmt gewichtete Risikofaktoren (Kosten, Zeit, Strategic Fit) und visualisiert die resultierenden Unsicherheiten als interaktive 3D-Konfidenz-Ellipsoide für das Management.*

---
</div>

## 🏗️ Projektstruktur & Module

Die Architektur trennt das Data Preprocessing strikt von der stochastischen Simulation und dem finalen Rendering:

| Komponente / Pfad | Beschreibung & Core Logic |
| :--- | :--- |
| 📄 **`main.py`** | **Orchestrator:** Steuert den gesamten Pipeline-Lebenszyklus vom Datenimport bis zum HTML-Export. |
| 📁 **`src/normalizer.py`** | **Data Preprocessing:** Skaliert die qualitativen rohen CSV-Scorecard-Daten systematisch auf einen normierten mathematischen Raum (0.0 - 1.0). |
| 📁 **`src/simulator.py`** | **Stochastic Engine:** Führt die Monte-Carlo-Simulation durch und berechnet **1.500 unabhängige Szenarien** pro Entscheidungsoption. |
| 📁 **`src/visualizer.py`** | **3D Rendering:** Generiert die 3D-KDE-Ellipsoide (Wahrscheinlichkeitswolken) via Plotly und exportiert diese als interaktives, browserfähiges HTML-Dokument. |
| 🗄️ **`data/` & `results/`** | Beinhaltet die zentrale Datenbank (`input_data.csv`) für die Definition der Optionen/Risiken sowie das finale Output-Artefakt (`3d_simulation_report.html`). |

---

## 🚀 Quick Start (Lokales Setup)

<details>
<summary><b>🛠️ Installation & Ausführung (Hier klicken zum Aufklappen)</b></summary>

### 1. Umgebung aufsetzen
Installiere alle benötigten Bibliotheken (Pandas, Plotly, SciPy):
```bash
pip install -r requirements.txt
