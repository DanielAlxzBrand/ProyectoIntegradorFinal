import tkinter as tk
from tkinter import ttk 

class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Talleres Culturales")
        self.campos = ["nombre", "apellido", "edad", "taller", "telefono", "email", "mes", "clases_asistidas"]
        self.entradas = {}

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        for idx, campo in enumerate(self.campos):
            tk.Label(self.frame, text=campo.capitalize()).grid(row=idx, column=0, sticky="e")
            entry = tk.Entry(self.frame)
            entry.grid(row=idx, column=1)
            self.entradas[campo] = entry

        #botones (pendiente de implementar las funciones)
        tk.Button(self.frame, text="Registrar", command=self.registrar).grid(row=0, column=2, padx=5)
        tk.Button(self.frame, text="Modificar", command=self.modificar).grid(row=1, column=2, padx=5)
        tk.Button(self.frame, text="Eliminar", command=self.eliminar).grid(row=2, column=2, padx=5)
        tk.Button(self.frame, text="Mostrar Todos", command=self.mostrar_todos).grid(row=3, column=2, padx=5)
        tk.Button(self.frame, text="Reportes", command=self.reportes).grid(row=4, column=2, padx=5)

        #campo de resultados
        self.tabla = ttk.Treeview(root, columns=self.campos, show="headings")
        for campo in self.campos:
            self.tabla.heading(campo, text=campo.capitalize())
        self.tabla.pack(padx=10, pady=10, fill="x")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazApp(root)
    root.mainloop()