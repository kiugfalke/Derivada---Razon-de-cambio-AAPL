📈 Derivatives Analysis: Unlocking Market Velocity and Acceleration (AAPL)

Welcome to the Derivatives Analysis project for stock market data, specifically focusing on Apple Inc. ($\text{AAPL}$). This Python script leverages the fundamental principles of differential calculus to extract deep insights into price movement, far beyond simple trend observation.

<img width="1536" height="754" alt="Figure_1" src="https://github.com/user-attachments/assets/2c5ebae8-55b3-4950-a187-736339bc1c85" />


Core Concept: The Calculus of Finance

In this model, the **stock price is treated as a function of time, $P(t)$**. By calculating its derivatives, we can quantitatively measure the rate and direction of change:

| Derivative | Mathematical Concept | Financial Interpretation | Strategy Implication |

| **First Derivative** ($\mathbf{P'(t)}$) | **Velocity** (Rate of Change) | The **speed and direction** of the price movement. | $\mathbf{P'(t) > 0}$ suggests a buying signal (Uptrend). $\mathbf{P'(t) < 0}$ suggests caution (Downtrend). |
| **Second Derivative** ($\mathbf{P''(t)}$) | **Acceleration** (Change in Rate) | The **momentum** of the trend; how quickly the velocity is changing. | $\mathbf{P''(t) > 0}$ suggests an accelerating trend. $\mathbf{P''(t) < 0}$ suggests a decelerating trend. |

-----

**🚀 Key Features of the Script (`Derivada razon de cambio utilidad AAPL.py`)**

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/74bfe760-3e2d-4e7a-b267-0242d39a3675" />


1.  **Data Acquisition:** Downloads 10 years of historical 'Close' price data for the specified ticker (default is $\text{AAPL}$) using `yfinance`.
2.  **Numerical Differentiation:** Implements robust **Finite Difference Methods** to calculate the 1st and 2nd derivatives of the price series.
      * *1st Derivative (Velocity):* Approximated using the **Central Difference Formula**: $f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$.
      * *2nd Derivative (Acceleration):* Approximated using the formula: $f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$.
3.  **Critical Point Identification:** Mathematically identifies **local Maxima and Minima** (where $P'(t)$ changes sign) and **Inflection Points** (where $P''(t)$ changes sign, indicating a change in market concavity/momentum).
4.  **Trend and Momentum Analysis:** Quantifies the percentage of time the stock spent in an **Uptrend** ($P'(t) > 0$) and **Accelerating** ($P''(t) > 0$).
5.  **Comprehensive Visualisation:** Generates a detailed 6-panel figure (`Figure_1.png`) for an intuitive understanding:
      * Price vs. Velocity.
      * Velocity vs. Acceleration.
      * Price with all **Critical Points** marked.
      * Distribution of the 1st Derivative (Volatility Skew).
      * Trend Analysis Bar Chart (Uptrend/Downtrend, Accelerating/Decelerating).
      * Basic **Derivative-based Trading Signals**.

### **🛠️ How to Run the Analysis**

**Prerequisites:**

Ensure you have the necessary Python libraries installed:

```bash
pip install yfinance pandas numpy matplotlib seaborn scipy
```

**Execution:**

1.  Save the code as `Derivada razon de cambio utilidad AAPL.py`.
2.  Run the script from your terminal:
    ```bash
    python "Derivada razon de cambio utilidad AAPL.py"
    ```
3.  The script will print the analysis summary to the console and display the generated plots.

-----

-----

## 🇩🇪 README (Deutsche Sprache)

### 📈 Ableitungsanalyse: Marktgeschwindigkeit und Beschleunigung entschlüsseln (AAPL)

Herzlich willkommen zum **Ableitungsanalyse**-Projekt für Börsendaten, das sich speziell auf **Apple Inc. ($\text{AAPL}$)** konzentriert. Dieses Python-Skript nutzt die grundlegenden Prinzipien der Differentialrechnung, um tiefgreifende Einblicke in die Preisentwicklung zu gewinnen, die über die einfache Trendbeobachtung hinausgehen.

-----

### **Kernkonzept: Die Analysis der Finanzen**

In diesem Modell wird der **Aktienkurs als Funktion der Zeit, $P(t)$**, behandelt. Durch die Berechnung seiner Ableitungen können wir die Rate und Richtung der Veränderung quantitativ messen:

| Ableitung | Mathematisches Konzept | Finanzielle Interpretation | Strategische Implikation |
| :--- | :--- | :--- | :--- |
| **Erste Ableitung** ($\mathbf{P'(t)}$) | **Geschwindigkeit** (Veränderungsrate) | Die **Geschwindigkeit und Richtung** der Preisbewegung. | $\mathbf{P'(t) > 0}$ deutet auf ein Kaufsignal hin (Aufwärtstrend). $\mathbf{P'(t) < 0}$ deutet auf Vorsicht hin (Abwärtstrend). |
| **Zweite Ableitung** ($\mathbf{P''(t)}$) | **Beschleunigung** (Veränderung der Rate) | Das **Momentum** des Trends; wie schnell sich die Geschwindigkeit ändert. | $\mathbf{P''(t) > 0}$ deutet auf einen sich beschleunigenden Trend hin. $\mathbf{P''(t) < 0}$ deutet auf einen sich verlangsamenden Trend hin. |

-----

### **🚀 Hauptfunktionen des Skripts (`Derivada razon de cambio utilidad AAPL.py`)**

1.  **Datenerfassung:** Lädt 10 Jahre historische 'Close'-Kursdaten für den angegebenen Ticker (Standard ist $\text{AAPL}$) mithilfe von `yfinance` herunter.
2.  **Numerische Differenzierung:** Implementiert robuste **Finite-Differenzen-Methoden** zur Berechnung der 1. und 2. Ableitung der Preisreihe.
      * *1. Ableitung (Geschwindigkeit):* Genähert mit der **zentralen Differenzenformel**: $f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$.
      * *2. Ableitung (Beschleunigung):* Genähert mit der Formel: $f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$.
3.  **Identifizierung kritischer Punkte:** Identifiziert mathematisch **lokale Maxima und Minima** (wo $\mathbf{P'(t)}$ das Vorzeichen wechselt) und **Wendepunkte** (wo $\mathbf{P''(t)}$ das Vorzeichen wechselt, was auf eine Änderung der Marktkonkavität/des Momentums hindeutet).
4.  **Trend- und Momentumanalyse:** Quantifiziert den prozentualen Zeitanteil, den die Aktie in einem **Aufwärtstrend** ($\mathbf{P'(t) > 0}$) und in der **Beschleunigung** ($\mathbf{P''(t) > 0}$) verbracht hat.
5.  **Umfassende Visualisierung:** Erzeugt eine detaillierte Abbildung mit 6 Panels (`Figure_1.png`) für ein intuitives Verständnis:
      * Kurs vs. Geschwindigkeit.
      * Geschwindigkeit vs. Beschleunigung.
      * Kurs mit allen markierten **kritischen Punkten**.
      * Verteilung der 1. Ableitung (Volatilitätsschiefe).
      * Balkendiagramm zur Trendanalyse (Auf-/Abwärtstrend, Beschleunigung/Verlangsamung).
      * Basis-**Handelssignale basierend auf Ableitungen**.

### **🛠️ Wie man die Analyse ausführt**

**Voraussetzungen:**

Stellen Sie sicher, dass Sie die notwendigen Python-Bibliotheken installiert haben:

```bash
pip install yfinance pandas numpy matplotlib seaborn scipy
```

**Ausführung:**

1.  Speichern Sie den Code als `Derivada razon de cambio utilidad AAPL.py`.
2.  Führen Sie das Skript in Ihrem Terminal aus:
    ```bash
    python "Derivada razon de cambio utilidad AAPL.py"
    ```
3.  Das Skript gibt die Analyse-Zusammenfassung in der Konsole aus und zeigt die generierten Plots an.

Would you like me to translate the output analysis of the script for AAPL for the British English or German README?
