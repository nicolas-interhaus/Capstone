# modelo/evento.py

from controlador.app import db

class Evento(db.Model):
    __tablename__ = 'eventos'

    id_evento = db.Column(db.Integer, primary_key=True)
    evento = db.Column(db.String(200), nullable=False)
    fec_evento = db.Column(db.Date, nullable=False)
    patrocinadores = db.Column(db.String(200), nullable=True)
    direccion_evento = db.Column(db.String(200), nullable=False)
    precio_evento = db.Column(db.Float, nullable=False)
    capacidad_evento = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Evento {self.evento}>"
