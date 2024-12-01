from __init__ import create_app
from datetime import datetime
from flask import Flask, make_response, render_template, request, jsonify,redirect, send_file, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from models.usuario import Usuario
from models.vecinos import Vecino
from models.noticias import Noticias
from controlador.usuario_controlador import app as usuario_app
from werkzeug.security import check_password_hash
import psycopg2
from functools import wraps
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os   

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

@app.route('/generar_certificado', methods=['POST'])
def generar_certificado():
    nombre = request.form['nombre']
    rut = request.form['rut']
    direccion = request.form['direccion']
    comuna = request.form['comuna']
    fecha = request.form['fecha']
    
    # Ruta completa donde se va a guardar el archivo PDF
    archivo_pdf = os.path.join(os.getcwd(), 'certificado_residencia.pdf')
    print(f"Archivo PDF guardado en: {archivo_pdf}")  # Verificar la ruta
    
    # Crear el archivo PDF
    c = canvas.Canvas(archivo_pdf, pagesize=letter)
    
    # Escribir contenido en el PDF
    c.drawString(100, 750, f"Certificado de Residencia")
    c.drawString(100, 730, f"Nombre completo: {nombre}")
    c.drawString(100, 710, f"RUT: {rut}")
    c.drawString(100, 690, f"Dirección: {direccion}")
    c.drawString(100, 670, f"Comuna: {comuna}")
    c.drawString(100, 650, f"Fecha de emisión: {fecha}")
    
    # Guardar el PDF
    c.save()
    
    # Verificar si el archivo fue creado correctamente
    if os.path.exists(archivo_pdf):
        print(f"El archivo PDF se creó correctamente en: {archivo_pdf}")
    else:
        print("No se pudo crear el archivo PDF.")

    # Devolver el archivo PDF como respuesta
    return send_file(archivo_pdf, as_attachment=True)

@app.route('/admin_certificado')
def admin_certificado():
    return render_template('admin_certificado.html')
@app.route('/admin_noticias')
def admin_noticias():
    return render_template('admin_noticias.html')

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
        flash('Datos no válidos', 'danger')
        return redirect(url_for('registro'))  # Redirige de nuevo al formulario

    # Extraer los datos obligatorios del JSON
    rut = data.get('rut')
    nombres = data.get('nombres')
    apellido_paterno = data.get('apellido_paterno')
    apellido_materno = data.get('apellido_materno')
    direccion = data.get('direccion')
    comuna = data.get('comuna')
    email = data.get('email')

    # Verificar que los campos obligatorios estén presentes
    if not (rut and nombres and apellido_paterno and apellido_materno and direccion and comuna and email):
        flash('Faltan datos obligatorios', 'danger')
        return redirect(url_for('registro'))

    # Obtener el último ID en la tabla
    ultimo_usuario = db.session.query(Vecino).order_by(Vecino.id.desc()).first()
    nuevo_id = (ultimo_usuario.id + 1) if ultimo_usuario else 1

    try:
        # Insertar el nuevo vecino en la base de datos
        nuevo_vecino = Vecino(
            id=nuevo_id,
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
        flash(f'Vecino registrado con éxito con RUT {rut}', 'success')
        # Redirigir al formulario de registro después de éxito
        return redirect(url_for('registro'))
    except Exception as e:
        print(f"Error al registrar vecino: {e}")
        db.session.rollback()  # Revertir cambios si ocurre un error
        flash('Error al registrar el vecino', 'danger')
        return redirect(url_for('registro'))



@app.route('/api/vecinos', methods=['GET'])
def api_vecinos():
    conn = connect_db()
    if conn is None:
        return jsonify({"error": "Error al conectar con la base de datos"}), 500

    cursor = conn.cursor()
    query = "SELECT id, rut, nombres, apellido_paterno, apellido_materno, direccion, comuna, email FROM vecinos"
    try:
        cursor.execute(query)
        vecinos = cursor.fetchall()
        # Convierte los resultados en una lista de diccionarios
        vecinos_list = [
            {
                "id":row[0],
                "rut": row[1],
                "nombres": row[2],
                "apellido_paterno": row[3],
                "apellido_materno": row[4],
                "direccion": row[5],
                "comuna": row[6],
                "email": row[7],
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

@app.route('/api/publicar_noticia', methods=['POST'])
def publicar_noticia():
    try:
        # Conectar a la base de datos
        conn = connect_db()
        if conn is None:
            return jsonify({"error": "Error al conectar con la base de datos"}), 500
        # Obtener el último ID en la tabla
        ultimo_usuario = db.session.query(Noticias).order_by(Noticias.noticia_id.desc()).first()
        print("valor ultimo_usuarrio")
        nuevo_id = (ultimo_usuario.noticia_id + 1) if ultimo_usuario else 1

        # Obtener los datos de la solicitud
        datos = request.json
        titulo = datos.get('titulo')
        detalle = datos.get('detalle')
        autor = datos.get('autor')
        fecha_publicacion = datos.get('fecha_publicacion')

        # Validar que todos los campos estén presentes
        if not all([titulo, detalle, autor, fecha_publicacion]):
            return jsonify({"error": "Faltan datos en la solicitud"}), 400

        # Insertar la nueva noticia en la base de datos
        cursor = conn.cursor()
        query = """
            INSERT INTO noticia (noticia_id,titulo, detalle, autor, fecha_publicacion, aprobacion, prioridad)
            VALUES (%s,%s, %s, %s, %s,True,True)
        """
        cursor.execute(query, (nuevo_id,titulo, detalle, autor, fecha_publicacion))
        conn.commit()

        return jsonify({"message": "Noticia publicada exitosamente"}), 201
    except Exception as e:
        print(f"Error al publicar noticia: {e}")
        return jsonify({"error": "Error al publicar la noticia"}), 500
    finally:
        if conn:
            conn.close()

@app.route('/api/mostrar_noticias', methods=['GET'])
def api_noticias():
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
            fecha_publicacion,
            aprobacion,
            prioridad
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
                "fecha_publicacion": row[4].strftime('%Y-%m-%d'),  # Formato de fecha
                "aprobacion": False, # Formato de fecha
                "prioridad": False  # Formato de fecha
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

@app.route('/api/actualizar_aprobacion', methods=['POST'])
def actualizar_aprobacion():
    data = request.get_json()
    noticia_id = data.get('noticia_id')
    aprobado = True

    conn = connect_db()
    if conn is None:
        return jsonify({"error": "Error al conectar con la base de datos"}), 500

    cursor = conn.cursor()
    query = "UPDATE noticia SET aprobacion = %s WHERE noticia_id = %s"
    try:
        cursor.execute(query, (aprobado, noticia_id))
        conn.commit()
        return jsonify({"message": "Estado de aprobación actualizado"})
    except Exception as e:
        print(f"Error al actualizar aprobación: {e}")
        return jsonify({"error": "Error al actualizar la aprobación"}), 500
    finally:
        cursor.close()
        conn.close()
@app.route('/api/noticias_aprobadas', methods=['GET'])
def noticias_aprobadas():
    conn = connect_db()
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
        WHERE 
            aprobacion = TRUE
        ORDER BY 
            fecha_publicacion DESC
        LIMIT 5;
    """
    try:
        cursor.execute(query)
        noticias = cursor.fetchall()
        noticias_list = [
            {
                "noticia_id": row[0],
                "titulo": row[1],
                "detalle": row[2],
                "autor": row[3],
                "fecha_publicacion": row[4].strftime('%Y-%m-%d')
            }
            for row in noticias
        ]
        return jsonify(noticias_list)
    except Exception as e:
        print(f"Error al obtener noticias aprobadas: {e}")
        return jsonify({"error": "Error al obtener las noticias aprobadas"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/inicio_sesion', methods=['POST'])
def login():
    try:
        # Asegurarse de que la solicitud tiene un cuerpo válido
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No se enviaron datos'}), 400

        username = data.get('usuario')
        password = data.get('contraseña')
        print(f"valor del username: {username}")
        print(f"valor del password: {password}")
        if not username or not password:
            return jsonify({'message': 'Faltan campos obligatorios'}), 400

        # Aquí, maneja la lógica de conexión a la base de datos
        conn = connect_db()
        if conn is None:
            return jsonify({'message': 'Error al conectar con la base de datos'}), 500

        cursor = conn.cursor()
        query = """
        SELECT contraseña, perfil
        FROM usuario
        WHERE usuario = %s and contraseña = %s
        """
        cursor.execute(query, (username,password))
        print(f"valor del query: {query}")
        result = cursor.fetchone()
        print(result)
        if result:
            session['usuario'] = password
            session['perfil'] = result[1]
            return jsonify({'message': 'success', 'perfil': result[1]}), 200
        else:
            return jsonify({'message': 'Usuario o contraseña incorrectos'}), 401
    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")
        return jsonify({'message': 'Error interno del servidor'}), 500




if __name__ == '__main__':
    app.run(debug=True)
