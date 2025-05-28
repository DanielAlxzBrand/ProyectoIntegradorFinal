# Importamos los módulos necesarios para la interfaz gráfica, manejo de datos y lógica del proyecto
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from logica import Participante
from analisis import Analisis

# Definimos la ruta donde se almacenarán los datos de los participantes
RUTA_DATOS = "./app/datos/participantes.csv"

class InterfazApp:
    def __init__(self, root):
        # Inicializamos la ventana principal y configuramos los campos del formulario
        self.root = root
        self.root.title("Gestión de Talleres Culturales")
        self.campos = ["nombre", "apellido", "edad", "taller", "telefono", "email", "mes", "clases_asistidas"]
        self.entradas = {}

        # Creamos el frame principal para los widgets del formulario
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Generamos dinámicamente las etiquetas y cajas de texto para cada campo
        for idx, campo in enumerate(self.campos):
            tk.Label(self.frame, text=campo.capitalize()).grid(row=idx, column=0, sticky="e")
            entry = tk.Entry(self.frame)
            entry.grid(row=idx, column=1)
            self.entradas[campo] = entry

        # Agregamos los botones principales para las acciones CRUD y reportes
        tk.Button(self.frame, text="Registrar", command=self.registrar).grid(row=0, column=2, padx=5)
        tk.Button(self.frame, text="Modificar", command=self.modificar).grid(row=1, column=2, padx=5)
        tk.Button(self.frame, text="Eliminar", command=self.eliminar).grid(row=2, column=2, padx=5)
        tk.Button(self.frame, text="Mostrar Todos", command=self.mostrar_todos).grid(row=3, column=2, padx=5)
        tk.Button(self.frame, text="Reportes", command=self.reportes).grid(row=4, column=2, padx=5)

        # Creamos la tabla donde se mostrarán los registros de los participantes
        self.tabla = ttk.Treeview(root, columns=self.campos, show="headings")
        for campo in self.campos:
            self.tabla.heading(campo, text=campo.capitalize())
        self.tabla.pack(padx=10, pady=10, fill="x")

        # Cargamos los datos existentes al iniciar la aplicación
        self.cargar_datos()
        
    def cargar_datos(self):
        # Intentamos leer los datos desde el archivo CSV, si no existe creamos un DataFrame vacío
        try:
            self.df = pd.read_csv(RUTA_DATOS)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=self.campos)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        # Limpiamos la tabla y la llenamos con los datos actuales del DataFrame
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        for _, fila in self.df.iterrows():
            self.tabla.insert("", "end", values=[fila.get(c, "") for c in self.campos])

    def registrar(self):
        # Registramos un nuevo participante validando los datos y actualizando el archivo CSV
        datos = {campo: self.entradas[campo].get() for campo in self.campos}
        if not all(datos.values()):
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return
        try:
            datos["edad"] = int(datos["edad"])
            datos["clases_asistidas"] = int(datos["clases_asistidas"])
        except ValueError:
            messagebox.showerror("Error", "Edad y clases asistidas deben ser números.")
            return
        participante = Participante(**datos)
        datos["valor_pagado"] = participante.calcular_pago_mes()
        nueva_fila = pd.DataFrame([datos])
        self.df = pd.concat([self.df, nueva_fila], ignore_index=True)
        self.df.to_csv(RUTA_DATOS, index=False)
        self.actualizar_tabla()
        messagebox.showinfo("Éxito", "Participante registrado correctamente.")

    def modificar(self):
        # Permitimos modificar los datos de un participante seleccionado en la tabla
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Seleccionar", "Seleccione un registro para modificar.")
            return
        idx = self.tabla.index(seleccionado[0])
        for campo in self.campos:
            self.df.at[idx, campo] = self.entradas[campo].get()
        try:
            self.df.at[idx, "edad"] = int(self.df.at[idx, "edad"])
            self.df.at[idx, "clases_asistidas"] = int(self.df.at[idx, "clases_asistidas"])
        except ValueError:
            messagebox.showerror("Error", "Edad y clases asistidas deben ser números.")
            return
        participante = Participante(**{campo: self.df.at[idx, campo] for campo in self.campos})
        self.df.at[idx, "valor_pagado"] = participante.calcular_pago_mes()
        self.df.to_csv(RUTA_DATOS, index=False)
        self.actualizar_tabla()
        messagebox.showinfo("Éxito", "Participante modificado correctamente.")

    def eliminar(self):
        # Eliminamos el registro seleccionado de la tabla y del archivo CSV
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Seleccionar", "Seleccione un registro para eliminar.")
            return
        idx = self.tabla.index(seleccionado[0])
        self.df = self.df.drop(self.df.index[idx]).reset_index(drop=True)
        self.df.to_csv(RUTA_DATOS, index=False)
        self.actualizar_tabla()
        messagebox.showinfo("Éxito", "Participante eliminado correctamente.")

    def mostrar_todos(self):
        # Recargamos todos los datos desde el archivo CSV
        self.cargar_datos()

    def reportes(self):
        # Generamos y mostramos reportes estadísticos y gráficos sobre los participantes
        analisis = Analisis(RUTA_DATOS)
        total = analisis.total_participantes()
        incompletos = analisis.participantes_incompletos()
        promedio = analisis.promedio_pago_por_taller()
        taller_max = analisis.taller_mas_participantes()
        mayor_pago = analisis.participante_mayor_pago()

        reporte = (
            f"Total participantes: {total}\n"
            f"Participantes incompletos: {len(incompletos)}\n"
            f"Promedio pago por taller:\n{promedio}\n"
            f"Taller con más participantes: {taller_max}\n"
            f"Participante con mayor pago:\n{mayor_pago}\n"
        )
        messagebox.showinfo("Reporte", reporte)

        # Mostramos los gráficos generados por el módulo de análisis
        analisis.grafico_barras_participantes_por_taller()
        analisis.histograma_edades()
        analisis.grafico_circular_talleres()

if __name__ == "__main__":
    # Iniciamos la aplicación principal de Tkinter
    root = tk.Tk()
    app = InterfazApp(root)
    root.mainloop()