
from datetime import datetime
from flask import Flask, render_template, request, jsonify,redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models.usuario import Usuario
from models.vecinos import Vecino
from werkzeug.security import check_password_hash
import psycopg2
from functools import wraps

usuario_app = Blueprint('usuario_app', __name__)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Falsedb = SQLAlchemy(app)
@app.route('/')
def formulario():
    return render_template('registro.html')  # Esto es el archivo de la vista
def connect_db():
    try:
        conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")

        return None
@app.route('/api/vecinos', methods=['GET'])
def api_vecinos():
    conn = connect_db()
    if conn is None:
        return jsonify({"error": "Error al conectar con la base de datos"}), 500

    cursor = conn.cursor()
    query = "SELECT rut, nombres, apellido_paterno, apellido_materno, direccion, comuna, email FROM vecinos"
    try:
        cursor.execute(query)
        vecinos = cursor.fetchall()
        # Convierte los resultados en una lista de diccionarios
        vecinos_list = [
            {
                "rut": row[0],
                "nombres": row[1],
                "apellido_paterno": row[2],
                "apellido_materno": row[3],
                "direccion": row[4],
                "comuna": row[5],
                "email": row[6],
            }
            for row in vecinos
        ]
        print(f"Vecinos obtenidos: {vecinos_list}")
        return jsonify(vecinos_list)
    except Exception as e:
        print(f"Error al obtener vecinos: {e}")
        return jsonify({"error": "Error al obtener los vecinos"}), 500
    finally:
        cursor.close()
        conn.close()
@app.route('/api/usuarios', methods=['GET'])
def api_usuarios():
    conn = connect_db()
    if conn is None:
        return jsonify({"error": "Error al conectar con la base de datos"}), 500

    cursor = conn.cursor()
    query = "SELECT usuario_id, usuario, contraseña, cargo, perfil, fecha_registro FROM usuarios"
    try:
        cursor.execute(query)
        usuarios = cursor.fetchall()
        usuarios_list = [
            {
                "usuario_id": row[0],
                "usuario": row[1],
                "contraseña": row[2],
                "cargo": row[3],
                "perfil": row[4],
                "fecha_registro": row[5],
            }
            for row in usuarios
        ]
        print(f"Usuarios obtenidos: {usuarios_list}")

        return jsonify(usuarios_list)
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return jsonify({"error": "Error al obtener los usuarios"}), 500
    finally:
        cursor.close()
        conn.close()


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