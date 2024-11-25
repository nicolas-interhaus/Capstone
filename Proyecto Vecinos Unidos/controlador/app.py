import psycopg2
from flask import Flask, redirect, request, jsonify, render_template, flash, url_for
from flask_cors import CORS
import webbrowser
import threading

app = Flask(__name__)

CORS(app)
# Configuración de la conexión a PostgreSQL
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'capstone',
    'user': 'postgres',
    'password': 'admin',
    'port': 5432  # Puerto por defecto de PostgreSQL
}

# Función para conectar a la base de datos
def connect_db():
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

# Ruta para la página de inicio
@app.route('/')
def home():
    return render_template('home.html')
# Ruta para la página de inicio de sesión
@app.route('/')
def login_page():
    return render_template('inicio_sesion.html')

# Ruta para manejar el inicio de sesión
@app.route('/inicio_sesion', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = connect_db()
    if conn is None:
        return "Error al conectar con la base de datos", 500

    cursor = conn.cursor()

    # Consulta para verificar las credenciales
    query = """
    SELECT tipo_usuario
    FROM vecinos
    WHERE username = %s AND password = %s
    """
    try:
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result is None:
            flash('Usuario o contraseña incorrectos', 'error')
            return redirect(url_for('login_page'))
        
        tipo_usuario = result[0]
        if tipo_usuario == 'admin':
            return redirect(url_for('admin_page'))  # Redirigir a la página de administrador
        else:
            flash('Acceso denegado. Solo administradores pueden entrar.', 'warning')
            return redirect(url_for('login_page'))
    except Exception as e:
        print(f"Error al verificar usuario: {e}")
        flash('Error al procesar la solicitud', 'error')
        return redirect(url_for('login_page'))
    finally:
        cursor.close()
        conn.close()


# Ruta para generar un certificado (mantén las rutas existentes)
@app.route('/generacion_certificado', methods=['POST'])
def generar_certificado():
    data = request.json
    nombre = data.get('nombre')
    rut = data.get('rut')
    direccion = data.get('direccion')
    comuna = data.get('comuna')
    fecha = data.get('fecha')

    if not all([nombre, rut, direccion, comuna, fecha]):
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    conn = connect_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

    cursor = conn.cursor()
    query = """
    INSERT INTO certificado_residencia (cert_nombre, cert_rut, cert_direccion, cert_comuna, cert_fecha_emision)
    VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(query, (nombre, rut, direccion, comuna, fecha))
        conn.commit()
        return jsonify({'message': 'Certificado generado exitosamente'}), 201
    except Exception as e:
        conn.rollback()
        print(f"Error al ejecutar la consulta: {e}")
        return jsonify({'error': f'Error al generar certificado: {e}'}), 500
    finally:
        cursor.close()
        conn.close()

# Función para abrir la página en el navegador
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Abre el navegador en un hilo separado para evitar bloquear el servidor
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
