
from datetime import datetime
from flask import Flask, render_template, request, jsonify,redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models.usuario import Usuario
from models.vecinos import Vecino
from werkzeug.security import check_password_hash
import psycopg2, pg8000
from functools import wraps

usuario_app = Blueprint('usuario_app', __name__)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://postgres:admin@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Falsedb = SQLAlchemy(app)
@app.route('/')
def formulario():
    return render_template('registro.html')  # Esto es el archivo de la vista
def connect_db():
    try:
        conn = pg8000.connect(app.config['SQLALCHEMY_DATABASE_URI'])
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")

        return None




def mostrar_usuario(usuario):
    print(f"Nombre: {usuario.nombre}")
    print(f"Edad: {usuario.edad}")
    print(f"Correo: {usuario.correo}")

def solicitar_datos_usuario():
    nombre = input("Ingresa el nombre del usuario: ")
    edad = int(input("Ingresa la edad del usuario: "))
    correo = input("Ingresa el correo del usuario: ")
    return nombre, edad, correo

if __name__ == '__main__':
    app.run(debug=True)