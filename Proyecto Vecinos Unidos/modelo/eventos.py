class Eventos:
    def __init__(self, nombre, direccion, costo):
        self.nombre = nombre
        self.direccion = direccion
        self.costo = costo

    def __str__(self):
        return f"Usuario: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}" 