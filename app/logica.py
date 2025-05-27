class Participante:
    def __init__(self, nombre, apellido, edad, taller, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.taller = taller  
        self.telefono = telefono
        self.email = email
        self.asistencias = []  
        self.pagos = []        

    def registrar_asistencia(self, fecha):
        self.asistencias.append(fecha)

    def registrar_pago(self, monto):
        self.pagos.append(monto)

    def total_pagado(self):
        return sum(self.pagos)

    def total_asistencias(self):
        return len(self.asistencias)