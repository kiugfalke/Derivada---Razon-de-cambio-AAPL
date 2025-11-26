import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class AnalisisDerivadas:
    def __init__(self, ticker):
        self.ticker = ticker
        self.datos = None
        self.derivadas = None
    
    def descargar_datos(self, años=10):
        """Descargar datos históricos"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=años*365)
        
        self.datos = yf.download(self.ticker, start=start_date, end=end_date)
        return self.datos
    
    def calcular_derivadas(self):
        """Calcular derivadas de diferentes órdenes usando métodos numéricos"""
        
        # Derivada primera (velocidad de cambio)
        self.datos['Derivada_1'] = self.calcular_derivada_numerica(self.datos['Close'], orden=1)
        
        # Derivada segunda (aceleración)
        self.datos['Derivada_2'] = self.calcular_derivada_numerica(self.datos['Close'], orden=2)
        
        # Derivada suavizada (media móvil de la derivada)
        self.datos['Derivada_Suavizada'] = self.datos['Derivada_1'].rolling(window=20).mean()
        
        return self.datos
    
    def calcular_derivada_numerica(self, serie, orden=1, h=1):
        """
        Calcular derivada numérica usando diferencias finitas
        orden 1: f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
        orden 2: f''(x) ≈ [f(x+h) - 2f(x) + f(x-h)] / h²
        """
        derivada = np.zeros_like(serie)
        
        if orden == 1:
            # Diferencias centradas para mayor precisión
            for i in range(1, len(serie)-1):
                derivada[i] = (serie.iloc[i+1] - serie.iloc[i-1]) / (2 * h)
            # Para los extremos usamos diferencias hacia adelante/atrás
            derivada[0] = (serie.iloc[1] - serie.iloc[0]) / h
            derivada[-1] = (serie.iloc[-1] - serie.iloc[-2]) / h
            
        elif orden == 2:
            # Segunda derivada
            for i in range(1, len(serie)-1):
                derivada[i] = (serie.iloc[i+1] - 2*serie.iloc[i] + serie.iloc[i-1]) / (h**2)
            derivada[0] = derivada[1]  # Extrapolación
            derivada[-1] = derivada[-2]
        
        return derivada
    
    def identificar_puntos_criticos(self):
        """Identificar máximos, mínimos y puntos de inflexión usando derivadas"""
        
        puntos_criticos = {
            'maximos': [],
            'minimos': [],
            'puntos_inflexion': []
        }
        
        # Buscar cambios de signo en la primera derivada (máximos y mínimos)
        for i in range(1, len(self.datos)-1):
            # Máximos locales (derivada cambia de + a -)
            if (self.datos['Derivada_1'].iloc[i-1] > 0 and 
                self.datos['Derivada_1'].iloc[i] < 0):
                puntos_criticos['maximos'].append(self.datos.index[i])
            
            # Mínimos locales (derivada cambia de - a +)
            elif (self.datos['Derivada_1'].iloc[i-1] < 0 and 
                  self.datos['Derivada_1'].iloc[i] > 0):
                puntos_criticos['minimos'].append(self.datos.index[i])
        
        # Buscar puntos de inflexión (cambios de signo en segunda derivada)
        for i in range(1, len(self.datos)-1):
            if (self.datos['Derivada_2'].iloc[i-1] * self.datos['Derivada_2'].iloc[i] < 0):
                puntos_criticos['puntos_inflexion'].append(self.datos.index[i])
        
        return puntos_criticos
    
    def analizar_tendencias_derivadas(self):
        """Analizar tendencias basadas en las derivadas"""
        
        # Tendencias basadas en primera derivada
        derivada_positiva = self.datos['Derivada_1'] > 0
        tendencia_alcista = derivada_positiva.mean()
        
        # Análisis de aceleración
        aceleracion_positiva = self.datos['Derivada_2'] > 0
        tendencia_aceleracion = aceleracion_positiva.mean()
        
        return {
            'porcentaje_tiempo_alcista': tendencia_alcista * 100,
            'porcentaje_tiempo_aceleracion': tendencia_aceleracion * 100,
            'derivada_promedio': self.datos['Derivada_1'].mean(),
            'aceleracion_promedio': self.datos['Derivada_2'].mean()
        }

# Ejecutar análisis completo
def analisis_completo_con_derivadas(ticker="AAPL"):
    # Inicializar analizador
    analizador = AnalisisDerivadas(ticker)
    
    # Descargar datos
    datos = analizador.descargar_datos(años=10)
    
    # Calcular derivadas
    datos_con_derivadas = analizador.calcular_derivadas()
    
    # Identificar puntos críticos
    puntos_criticos = analizador.identificar_puntos_criticos()
    
    # Analizar tendencias
    analisis_tendencias = analizador.analizar_tendencias_derivadas()
    
    return analizador, puntos_criticos, analisis_tendencias

# Visualización con derivadas
def crear_visualizacion_completa(analizador, puntos_criticos, analisis_tendencias):
    datos = analizador.datos
    
    fig, axes = plt.subplots(3, 2, figsize=(16, 12))
    fig.suptitle(f'Análisis con Derivadas: {analizador.ticker} - Comportamiento y Razón de Cambio', 
                 fontsize=16, fontweight='bold')
    
    # Gráfica 1: Precio y derivada primera
    ax1 = axes[0, 0]
    ax1.plot(datos.index, datos['Close'], label='Precio', linewidth=1.5, color='blue')
    ax1.set_ylabel('Precio (USD)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True, alpha=0.3)
    
    ax1b = ax1.twinx()
    ax1b.plot(datos.index, datos['Derivada_1'], label='Derivada 1ª (Velocidad)', 
              linewidth=1, color='red', alpha=0.7)
    ax1b.set_ylabel('Velocidad de Cambio', color='red')
    ax1b.tick_params(axis='y', labelcolor='red')
    ax1b.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    ax1.set_title('Precio y Primera Derivada (Velocidad)')
    
    # Gráfica 2: Primera y segunda derivada
    ax2 = axes[0, 1]
    ax2.plot(datos.index, datos['Derivada_1'], label='Derivada 1ª (Velocidad)', 
             linewidth=1.5, color='red')
    ax2.plot(datos.index, datos['Derivada_2'], label='Derivada 2ª (Aceleración)', 
             linewidth=1.5, color='green', alpha=0.7)
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    ax2.set_title('Velocidad y Aceleración del Cambio')
    ax2.set_ylabel('Tasa de Cambio')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Gráfica 3: Puntos críticos identificados
    ax3 = axes[1, 0]
    ax3.plot(datos.index, datos['Close'], label='Precio', linewidth=1.5, color='blue')
    
    # Marcar puntos críticos
    if puntos_criticos['maximos']:
        maximos_dates = puntos_criticos['maximos']
        maximos_prices = [datos.loc[date, 'Close'] for date in maximos_dates]
        ax3.scatter(maximos_dates, maximos_prices, color='red', s=50, 
                   label='Máximos', marker='v')
    
    if puntos_criticos['minimos']:
        minimos_dates = puntos_criticos['minimos']
        minimos_prices = [datos.loc[date, 'Close'] for date in minimos_dates]
        ax3.scatter(minimos_dates, minimos_prices, color='green', s=50, 
                   label='Mínimos', marker='^')
    
    if puntos_criticos['puntos_inflexion']:
        inflexion_dates = puntos_criticos['puntos_inflexion']
        inflexion_prices = [datos.loc[date, 'Close'] for date in inflexion_dates]
        ax3.scatter(inflexion_dates, inflexion_prices, color='orange', s=50, 
                   label='Puntos Inflexión', marker='o')
    
    ax3.set_title('Puntos Críticos Identificados')
    ax3.set_ylabel('Precio (USD)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Gráfica 4: Distribución de la primera derivada
    ax4 = axes[1, 1]
    derivada_positiva = datos['Derivada_1'][datos['Derivada_1'] > 0]
    derivada_negativa = datos['Derivada_1'][datos['Derivada_1'] < 0]
    
    ax4.hist(derivada_positiva, bins=50, alpha=0.7, color='green', 
             label='Derivada Positiva (+)', edgecolor='black')
    ax4.hist(derivada_negativa, bins=50, alpha=0.7, color='red', 
             label='Derivada Negativa (-)', edgecolor='black')
    ax4.axvline(x=0, color='black', linestyle='--', linewidth=2)
    ax4.set_title('Distribución de la Primera Derivada')
    ax4.set_xlabel('Valor de la Derivada')
    ax4.set_ylabel('Frecuencia')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # Gráfica 5: Análisis de tendencias por derivadas
    ax5 = axes[2, 0]
    tendencias = ['Alcista', 'Bajista', 'Acelerando', 'Desacelerando']
    valores = [
        analisis_tendencias['porcentaje_tiempo_alcista'],
        100 - analisis_tendencias['porcentaje_tiempo_alcista'],
        analisis_tendencias['porcentaje_tiempo_aceleracion'],
        100 - analisis_tendencias['porcentaje_tiempo_aceleracion']
    ]
    colores = ['green', 'red', 'blue', 'orange']
    
    bars = ax5.bar(tendencias, valores, color=colores, alpha=0.7, edgecolor='black')
    ax5.set_title('Análisis de Tendencias por Derivadas')
    ax5.set_ylabel('Porcentaje del Tiempo (%)')
    
    # Añadir valores en las barras
    for bar, valor in zip(bars, valores):
        ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{valor:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # Gráfica 6: Señales de trading basadas en derivadas
    ax6 = axes[2, 1]
    ax6.plot(datos.index, datos['Close'], label='Precio', linewidth=1.5, color='blue')
    
    # Señal de compra cuando derivada cambia de negativa a positiva
    compras = []
    for i in range(1, len(datos)):
        if (datos['Derivada_1'].iloc[i-1] < 0 and datos['Derivada_1'].iloc[i] > 0):
            compras.append(datos.index[i])
    
    # Señal de venta cuando derivada cambia de positiva a negativa
    ventas = []
    for i in range(1, len(datos)):
        if (datos['Derivada_1'].iloc[i-1] > 0 and datos['Derivada_1'].iloc[i] < 0):
            ventas.append(datos.index[i])
    
    if compras:
        precios_compras = [datos.loc[date, 'Close'] for date in compras]
        ax6.scatter(compras, precios_compras, color='green', s=100, 
                   label='Señal Compra', marker='^', zorder=5)
    
    if ventas:
        precios_ventas = [datos.loc[date, 'Close'] for date in ventas]
        ax6.scatter(ventas, precios_ventas, color='red', s=100, 
                   label='Señal Venta', marker='v', zorder=5)
    
    ax6.set_title('Señales de Trading Basadas en Derivadas')
    ax6.set_ylabel('Precio (USD)')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return fig

# Ejecutar análisis completo
if __name__ == "__main__":
    ticker = "AAPL"  # Puedes cambiar por MSFT, GOOGL, TSLA, etc.
    
    print("🔍 ANALISIS CON DERIVADAS - MODELO MATEMÁTICO")
    print("=" * 60)
    
    analizador, puntos_criticos, analisis_tendencias = analisis_completo_con_derivadas(ticker)
    
    # Mostrar resultados del análisis
    print("\n📊 RESULTADOS DEL ANÁLISIS CON DERIVADAS:")
    print(f"Empresa: {ticker}")
    print(f"Período: Últimos 10 años")
    print(f"Derivada promedio (velocidad): {analisis_tendencias['derivada_promedio']:.4f}")
    print(f"Aceleración promedio: {analisis_tendencias['aceleracion_promedio']:.4f}")
    print(f"Tiempo en tendencia alcista: {analisis_tendencias['porcentaje_tiempo_alcista']:.1f}%")
    print(f"Tiempo acelerando: {analisis_tendencias['porcentaje_tiempo_aceleracion']:.1f}%")
    
    print(f"\n📍 PUNTOS CRÍTICOS IDENTIFICADOS:")
    print(f"Máximos locales: {len(puntos_criticos['maximos'])}")
    print(f"Mínimos locales: {len(puntos_criticos['minimos'])}")
    print(f"Puntos de inflexión: {len(puntos_criticos['puntos_inflexion'])}")
    
    print("\n💡 INTERPRETACIÓN MATEMÁTICA:")
    print("• Primera derivada (Velocidad): Indica la dirección y velocidad del cambio")
    print("• Segunda derivada (Aceleración): Mide cómo cambia la velocidad")
    print("• Puntos críticos: Donde la derivada es cero (máximos, mínimos)")
    print("• Puntos de inflexión: Donde cambia la concavidad")
    
    print("\n🎯 RECOMENDACIONES ESTRATÉGICAS:")
    
    if analisis_tendencias['porcentaje_tiempo_alcista'] > 60:
        print("✓ TENDENCIA ALCISTA DOMINANTE: Favorece estrategias largas")
    else:
        print("⚠ TENDENCIA BAJISTA SIGNIFICATIVA: Considerar estrategias defensivas")
    
    if analisis_tendencias['derivada_promedio'] > 0:
        print("✓ VELOCIDAD PROMEDIO POSITIVA: Momentum favorable")
    else:
        print("⚠ VELOCIDAD PROMEDIO NEGATIVA: Cautela en nuevas posiciones")
    
    # Crear visualización
    fig = crear_visualizacion_completa(analizador, puntos_criticos, analisis_tendencias)