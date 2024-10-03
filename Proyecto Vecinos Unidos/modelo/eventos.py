class Eventos:
    def __init__(self, nombre,fec_evento,patrocinadores, direccion_evento, precio_evento,capacidad_evento):
        self.nombre = nombre
        self.fec_evento = fec_evento
        self.patrocinadores = patrocinadores
        self.direccion_evento = direccion_evento
        self.precio_evento = precio_evento
        self.capacidad_evento = capacidad_evento

    def __str__(self):
        return f"Usuario: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}" 