import psycopg2

class Usuario:
    def __init__(self, nombres,apellido_paterno,apellido_materno,fec_nacimiento,edad,genero,direccion,comuna,cargo,email):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fec_nacimiento = fec_nacimiento
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.comuna = comuna
        self.cargo = cargo
        self.email = email

    def __str__(self):
        return f"Usuario: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}"
    def insertar_usuario(nombres, apellido_paterno, apellido_materno, fec_nacimiento, edad, genero, direccion, comuna, cargo, email):
        conn = psycopg2.connect(
            host="localhost",
            database="Capstone",
            user="postgres",
            password="admin"
        )
        cur = conn.cursor()

        # Consulta para insertar los datos
        cur.execute("""
            INSERT INTO usuarios (nombres, apellido_paterno, apellido_materno, fec_nacimiento, edad, genero, direccion, comuna, cargo, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nombres, apellido_paterno, apellido_materno, fec_nacimiento, edad, genero, direccion, comuna, cargo, email))

        # Guardar cambios
        conn.commit()

        cur.close()
        conn.close()
