class Usuario:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def __str__(self):
        return f"Usuario: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}"
