import pandas as pd  #Importamos pandas para manejar los datos
import matplotlib.pyplot as plt  #Importamos matplotlib para graficar los datos

class Analisis:
    def __init__(self, ruta_datos):  #Guardamos la ruta del archivo y cargamos el dataframe
        self.ruta_datos = ruta_datos
        self.df = pd.read_csv(ruta_datos)

    def total_participantes(self): #Contamos cuantos participantes hay en total
        return len(self.df)

    def participantes_incompletos(self): #Buscamos los participantes que tienen algun dato obligatorio vacio o nulo
        campos_obligatorios = ['nombre', 'apellido', 'edad', 'taller', 'telefono', 'email', 'mes']
        incompletos = self.df[self.df[campos_obligatorios].isnull().any(axis=1) | (self.df[campos_obligatorios] == '').any(axis=1)]
        return incompletos
    
    def promedio_pago_por_taller(self): #Calculamos el promedio de pago por taller
        return self.df.groupby('taller')['valor_pagado'].mean()

    def taller_mas_participantes(self): #Vemos cual es el taller con mas participantes
        return self.df['taller'].value_counts().idxmax()

    def participante_mayor_pago(self): #Vemos cual es el participante que mas ha pagado
        idx = self.df['valor_pagado'].idxmax()
        return self.df.loc[idx]
    
    def grafico_barras_participantes_por_taller(self): #Hacemos un grafico de barras para ver la cantidad de participantes por taller
        conteo = self.df['taller'].value_counts()
        conteo.plot(kind='bar', color='skyblue')
        plt.title('Participantes por Taller')
        plt.xlabel('Taller')
        plt.ylabel('Cantidad')
        plt.tight_layout()
        plt.show()

    def histograma_edades(self): #Mostramos un histograma para ver las edades
        self.df['edad'].dropna().astype(int).plot(kind='hist', bins=10, color='lightgreen')
        plt.title('Histograma de Edades')
        plt.xlabel('Edad')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.show()

    def grafico_circular_talleres(self): #hacemos un grafico de torta (circular) para ver la distribucion de participantes por taller
        conteo = self.df['taller'].value_counts()
        conteo.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Distribución de Participantes por Taller')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()

    def guardar_datos(self): #guardamos los datos actualizados en el archivo CSV
        self.df.to_csv(self.ruta_datos, index=False)