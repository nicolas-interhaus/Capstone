from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary, DateTime
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/capstone'
db = SQLAlchemy(app)

class Certificado(db.Model):
    __tablename__ = 'certificado'
    cert_id = db.Column(db.Integer, primary_key=True)
    cert_folio = db.Column(db.Integer, nullable=False)
    cert_nombre = db.Column(db.String(50), nullable=False) # Campo con fecha actual por defecto
    cert_rut = db.Column(db.String(12), nullable=False)
    cert_direccion = db.Column(db.String(100), nullable=False)  # Campo con fecha actual por defecto
    cert_comuna = db.Column(db.String(50), nullable=False) 
    cert_fecha = db.Column(db.DateTime, nullable=False)
    documentos = relationship("Documento", back_populates="certificado", cascade="all, delete-orphan")

class Documento(db.Model):
    __tablename__ = 'documento'

    doc_id = db.Column(db.Integer, primary_key=True)
    doc_nombre = db.Column(db.String(100), nullable=False)
    doc_tipo = db.Column(db.String(50), nullable=False)
    doc_contenido = db.Column(db.LargeBinary, nullable=False)  # Almacena el archivo como BLOB
    cert_id = db.Column(db.Integer, ForeignKey('certificado.cert_id'), nullable=False)

    # Relación inversa
    certificado = relationship("Certificado", back_populates="documentos")


