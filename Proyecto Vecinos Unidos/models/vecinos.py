from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

# Modelo de Vecino
class Vecino(db.Model):
    __tablename__ = 'vecinos'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(12), nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    rut = db.Column(db.String(20), unique=True, nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    comuna = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


