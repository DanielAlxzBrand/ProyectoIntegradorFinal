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