# modelo/usuario.py

from controlador.app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(12), unique=True, nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    fec_nacimiento = db.Column(db.Date, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    comuna = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nombres} {self.apellido_paterno}>"
