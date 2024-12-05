from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Reserva(db.Model):
    __tablename__ = 'reserva'
    reserva_id = db.Column(db.Integer, primary_key=True)
    reserva_nombre = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.Boolean, nullable=False)
    aprobacion = db.Column(db.String(10), nullable=False)  # Campo con fecha actual por defecto
    is_public = db.Column(db.Boolean, nullable=False)  # Campo con fecha actual por defecto
    rut_solicitante = db.Column(db.String(12), nullable=False)
    
    fecha_reserva_inicio = db.Column(db.DateTime, nullable=False)
    fecha_reserva_termino = db.Column(db.DateTime, nullable=False)


