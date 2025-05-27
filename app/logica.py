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