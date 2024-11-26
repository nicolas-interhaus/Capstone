from __init__ import create_app
from datetime import datetime
from flask import Flask, render_template, request, jsonify,redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from models.usuario import Usuario
from models.vecinos import Vecino
from models.noticias import Noticias
from controlador.usuario_controlador import app as usuario_app
from werkzeug.security import check_password_hash
import psycopg2
from functools import wraps


app = create_app()

app = Flask(__name__)

app.secret_key = 'mi_clave_super_secreta'

# Configuración de la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
# Función para conectar a la base de datos
def connect_db():
    try:
        conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None
    

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('tipo_usuario') != 'admin':
            flash('Acceso denegado', 'danger')
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registro_vecino', methods=['GET'])
def registro_vecino():
    return render_template('ingreso.html')  # Asegúrate de que 'registro.html' sea la plantilla correcta



@app.route('/admin_certificado')
def admin_certificado():
    return render_template('admin_certificado.html')

@app.route('/admin_contacto')
def admin_contacto():
    return render_template('admin_contacto.html')



@app.route('/admin_reserva')
def admin_reserva():
    return render_template('admin_reserva.html')

@app.route('/admin_usuario')
def admin_usuario():
    return render_template('admin_usuario.html')

@app.route('/admin_vista')
def admin_vista():
    return render_template('admin_vista.html')

@app.route('/certificado')
def certificado():
    return render_template('certificado.html')

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

@app.route('/ingreso', methods=['POST'])
def registro_vecinos():
    # Obtener los datos enviados como JSON
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Datos no válidos'}), 400

    # Extraer los datos obligatorios del JSON
    rut = data.get('rut')
    nombres = data.get('nombres')
    apellido_paterno = data.get('apellido_paterno')
    apellido_materno = data.get('apellido_materno')
    direccion = data.get('direccion')
    comuna = data.get('comuna')
    email = data.get('email')
    print(f"valor de data en ingreso{data}")
    # Verificar que los campos obligatorios estén presentes
    if not (rut and nombres and apellido_paterno and apellido_materno and direccion and comuna and email):
        return jsonify({'message': 'Faltan datos obligatorios'}), 400

    try:
        # Insertar el nuevo vecino en la base de datos
        nuevo_vecino = Vecino(
            rut=rut,
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            direccion=direccion,
            comuna=comuna,
            email=email
        )
        db.session.add(nuevo_vecino)
        db.session.commit()
        print("Se ha crado el vecino")
        # Redirigir a la página de registro.html si el registro fue exitoso
        flash(f'Vecino registrado con éxito con RUT {rut}', 'success')
        return redirect(url_for('registro.html'))  # Asegúrate de que 'formulario' sea la ruta correcta.
    except Exception as e:
        print(f"Error al registrar vecino: {e}")
        db.session.rollback()  # Revertir cambios si ocurre un error
        flash('Error al registrar el vecino', 'danger')
        return redirect(url_for('registro.html'))


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
    query = "SELECT usuario_id, usuario, contraseña, cargo, perfil, fecha_registro FROM usuario"
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



@app.route('/api/admin_noticias', methods=['GET'])
def admin_noticias():
    conn = connect_db()  # Reemplaza con tu función de conexión a la base de datos
    if conn is None:
        return jsonify({"error": "Error al conectar con la base de datos"}), 500

    cursor = conn.cursor()
    query = """
        SELECT 
            noticia_id, 
            titulo, 
            detalle, 
            autor, 
            fecha_publicacion 
        FROM 
            noticia
    """
    try:
        # Ejecutar consulta
        cursor.execute(query)
        noticias = cursor.fetchall()
        
        # Formatear las noticias en una lista de diccionarios
        noticias_list = [
            {
                "noticia_id": row[0],
                "titulo": row[1],
                "detalle": row[2],
                "autor": row[3],
                "fecha_publicacion": row[4].strftime('%Y-%m-%d')  # Formato de fecha
            }
            for row in noticias
        ]
        print(f"Noticias obtenidas: {noticias_list}")

        # Devolver las noticias en formato JSON
        return jsonify(noticias_list)
    
    except Exception as e:
        print(f"Error al obtener noticias: {e}")
        return jsonify({"error": "Error al obtener las noticias"}), 500
    finally:
        # Cerrar cursor y conexión
        cursor.close()
        conn.close()

@app.route('/registro', methods=['POST'])
def registrar_usuario():

    data = request.get_json()  # Obtener los datos enviados como JSON
    if not data:
        return jsonify({'message': 'Datos no válidos'}), 400
    nombre_usuario = data.get('usuario')
    contraseña = data.get('contraseña')
    
    # Asignar valores predeterminados
    cargo = data.get('cargo', 'vecino')
    perfil = data.get('perfil', 'user')

    if not nombre_usuario or not contraseña:
        print(f"valor usuario {nombre_usuario}")
        print(f"valor contraseña {contraseña}")
        return jsonify({'message': 'Faltan datos obligatorios'}), 400

    # Obtener el último ID en la tabla
    ultimo_usuario = db.session.query(Usuario).order_by(Usuario.usuario_id.desc()).first()
    nuevo_id = (ultimo_usuario.usuario_id + 1) if ultimo_usuario else 1

    # Insertar el nuevo registro con el ID calculado
    nuevo_usuario = Usuario(usuario_id=nuevo_id, usuario=nombre_usuario, contraseña=contraseña, cargo=cargo, perfil=perfil)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'message': f'Usuario registrado con éxito con ID {nuevo_id}'}), 201

@app.route('/inicio_sesion', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = connect_db()
    if conn is None:
        return "Error al conectar con la base de datos", 500

    cursor = conn.cursor()

    # Consulta solo para obtener la contraseña hasheada y tipo de usuario
    query = """
    SELECT password, tipo_usuario
    FROM vecinos
    WHERE username = %s
    """
    try:
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result is None:
            flash('Usuario no encontrado', 'danger')
            return redirect(url_for('login_page'))

        hashed_password, tipo_usuario = result

        # Validar la contraseña usando check_password_hash
        if not check_password_hash(hashed_password, password):
            flash('Contraseña incorrecta', 'danger')
            return redirect(url_for('login_page'))

        # Redirigir según el tipo de usuario
        if tipo_usuario == 'admin':
            return redirect(url_for('admin_page'))
        else:
            flash('Acceso denegado. Solo administradores pueden entrar.', 'warning')
            return redirect(url_for('login_page'))
    except Exception as e:
        print(f"Error al verificar usuario: {e}")
        flash('Error al procesar la solicitud', 'danger')
        return redirect(url_for('login_page'))
    finally:
        cursor.close()
        conn.close()



if __name__ == '__main__':
    app.run(debug=True)
