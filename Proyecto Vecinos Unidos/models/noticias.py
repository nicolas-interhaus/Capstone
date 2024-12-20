from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Noticias(db.Model):
    __tablename__ = 'noticia'

    noticia_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String, nullable=False)
    detalle = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    fecha_publicacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Campo con fecha actual por defecto
    aprobacion = db.Column(db.Boolean, nullable=False, default=False)  # Campo con fecha actual por defecto
    prioridad = db.Column(db.Boolean, nullable=False, default=False)  # Campo con fecha actual por defecto
    noticia_imagen = db.Column(db.LargeBinary, nullable=False)  # Almacena el archivo como BLOB
    
    def __repr__(self):
        return f'<Noticias {self.titulo} - {self.autor}>'
