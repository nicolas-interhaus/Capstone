from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/capstone'
db = SQLAlchemy(app)

class Reserva(db.Model):
    __tablename__ = 'reservas'
    reserva_id = db.Column(db.Integer, primary_key=True)
    reserva_nombre = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.Boolean, nullable=False)
    aprobacion = db.Column(db.Boolean, nullable=False)  # Campo con fecha actual por defecto
    is_public = db.Column(db.Boolean, nullable=False)  # Campo con fecha actual por defecto
    rut_solicitante = db.Column(db.String(12), nullable=False)
    
    fecha_reserva = db.Column(db.DateTime, nullable=False)


