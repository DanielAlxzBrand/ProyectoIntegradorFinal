# Definimos la clase Participante, que representa a cada persona inscrita en un taller
class Participante:
    
# Declaramos las tarifas correspondientes a cada taller en un diccionario
    TARIFAS = {
        "pintura": 6000,
        "teatro": 8000,
        "música": 10000,
        "danza": 7000
    }

# Inicializamos los atributos del participante al crear una nueva instancia
    def __init__(self, nombre, apellido, edad, taller, telefono, email, mes=None, clases_asistidas=0):
        self.nombre = nombre # Asignamos el nombre del participante
        self.apellido = apellido # Asignamos el apellido del participante
        self.edad = edad # Asignamos la edad del participante
        self.taller = taller.lower() if taller else None # Guardamos el taller en minúsculas para uniformidad
        self.telefono = telefono # Guardamos el número de teléfono
        self.email = email # Guardamos el correo electrónico
        self.mes = mes  # Guardamos el mes de inscripción o asistencia
        self.clases_asistidas = clases_asistidas # Inicializamos la cantidad de clases asistidas
        self.asistencias = []  # Creamos una lista vacía para registrar las asistencias
        self.pagos = [] # Creamos una lista vacía para registrar los pagos       

# Definimos el método para registrar una nueva asistencia            
    def registrar_asistencia(self, fecha):
        self.asistencias.append(fecha) # Agregamos la fecha de asistencia a la lista
        self.clases_asistidas += 1 #Incrementamos el contador de clases asistidas

# Definimos el método para registrar un nuevo pago
    def registrar_pago(self, monto):
        self.pagos.append(monto) # Agregamos el monto pagado a la lista de pagos

# Calculamos el pago total del mes según el taller y la cantidad de clases asistidas
    def calcular_pago_mes(self):
        
        tarifa = self.TARIFAS.get(self.taller, 0) # Obtenemos la tarifa correspondiente al taller
        return tarifa * self.clases_asistidas # Multiplicamos la tarifa por las clases asistidas

# Calculamos el total pagado sumando todos los pagos registrados
    def total_pagado(self):
        return sum(self.pagos) # Sumamos todos los montos en la lista de pagos

# Calculamos el total de asistencias registradas
    def total_asistencias(self):
        return len(self.asistencias) # Contamos la cantidad de fechas en la lista de asistencias

# Verificamos si hay algún dato obligatorio incompleto
    def datos_incompletos(self):
        
        campos = [self.nombre, self.apellido, self.edad, self.taller, self.telefono, self.email, self.mes] # Listamos los campos obligatorios
        return any(c is None or c == "" for c in campos) # Retornamos True si algún campo está vacío o es None