import pandas as pd
import matplotlib.pyplot as plt

class Analisis:
    def __init__(self, ruta_datos):
        self.ruta_datos = ruta_datos
        self.df = pd.read_csv(ruta_datos)

    def total_participantes(self):
        return len(self.df)

    def participantes_incompletos(self):
        campos_obligatorios = ['nombre', 'apellido', 'edad', 'taller', 'telefono', 'email', 'mes']
        incompletos = self.df[self.df[campos_obligatorios].isnull().any(axis=1) | (self.df[campos_obligatorios] == '').any(axis=1)]
        return incompletos
    
    def promedio_pago_por_taller(self):
        return self.df.groupby('taller')['valor_pagado'].mean()

    def taller_mas_participantes(self):
        return self.df['taller'].value_counts().idxmax()

    def participante_mayor_pago(self):
        idx = self.df['valor_pagado'].idxmax()
        return self.df.loc[idx]
    
    def grafico_barras_participantes_por_taller(self):
        conteo = self.df['taller'].value_counts()
        conteo.plot(kind='bar', color='skyblue')
        plt.title('Participantes por Taller')
        plt.xlabel('Taller')
        plt.ylabel('Cantidad')
        plt.tight_layout()
        plt.show()

    def histograma_edades(self):
        self.df['edad'].dropna().astype(int).plot(kind='hist', bins=10, color='lightgreen')
        plt.title('Histograma de Edades')
        plt.xlabel('Edad')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.show()

    def grafico_circular_talleres(self):
        conteo = self.df['taller'].value_counts()
        conteo.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Distribución de Participantes por Taller')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()

    def guardar_datos(self):
        self.df.to_csv(self.ruta_datos, index=False)