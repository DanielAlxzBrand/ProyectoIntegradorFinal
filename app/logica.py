class Participante:
    
    TARIFAS = {
        "pintura": 6000,
        "teatro": 8000,
        "música": 10000,
        "danza": 7000
    }

    def __init__(self, nombre, apellido, edad, taller, telefono, email, mes=None, clases_asistidas=0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.taller = taller.lower() if taller else None
        self.telefono = telefono
        self.email = email
        self.mes = mes  
        self.clases_asistidas = clases_asistidas  
        self.asistencias = []  
        self.pagos = []        
            
    def registrar_asistencia(self, fecha):
        self.asistencias.append(fecha)
        self.clases_asistidas += 1

    def registrar_pago(self, monto):
        self.pagos.append(monto)

    def calcular_pago_mes(self):
        
        tarifa = self.TARIFAS.get(self.taller, 0)
        return tarifa * self.clases_asistidas

    def total_pagado(self):
        return sum(self.pagos)

    def total_asistencias(self):
        return len(self.asistencias)

    def datos_incompletos(self):
        
        campos = [self.nombre, self.apellido, self.edad, self.taller, self.telefono, self.email, self.mes]
        return any(c is None or c == "" for c in campos)