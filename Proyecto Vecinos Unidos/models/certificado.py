from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary, DateTime
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class Certificado(db.Model):
    __tablename__ = 'certificado'
    cert_id = db.Column(db.Integer, primary_key=True)
    cert_folio = db.Column(db.Integer, nullable=False)
    cert_nombre = db.Column(db.String(50), nullable=False) # Campo con fecha actual por defecto
    cert_rut = db.Column(db.String(12), nullable=False)
    cert_direccion = db.Column(db.String(100), nullable=False)  # Campo con fecha actual por defecto
    cert_comuna = db.Column(db.String(50), nullable=False) 
    cert_fecha = db.Column(db.DateTime, nullable=False)
    cert_estado = db.Column(db.String(20), default="Pendiente") 
    documentos = relationship("Documento", back_populates="certificado", cascade="all, delete-orphan")

class Documento(db.Model):
    __tablename__ = 'documentos'

    documento_id = db.Column(db.Integer, primary_key=True)
    documento_nombre = db.Column(db.String(100), nullable=False)
    documento_tipo = db.Column(db.String(50), nullable=False)
    documento_attachment = db.Column(db.LargeBinary, nullable=False)  # Almacena el archivo como BLOB
    documento_certificado_id= db.Column(db.Integer, ForeignKey('certificado.cert_id'), nullable=False)

    # Relación inversa
    certificado = relationship("Certificado", back_populates="documentos")


