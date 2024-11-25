from flask import Flask, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para la tabla usuario
class Usuario(db.Model):
    __tablename__ = 'usuario'
    usuario_id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(210),nullable=False)
    perfil = db.Column(db.String(210),nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)  # Campo con fecha actual por defecto

