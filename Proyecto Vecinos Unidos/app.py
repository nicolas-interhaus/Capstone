from __init__ import create_app
from datetime import datetime
from flask import Flask, make_response, render_template, request, jsonify,redirect, send_file, url_for, flash, session, Blueprint, Response
from weasyprint import HTML
from flask_sqlalchemy import SQLAlchemy
from models.usuario import Usuario
from models.vecinos import Vecino
from models.noticias import Noticias
from models.reserva import Reserva
from models.certificado import Certificado
from models.certificado import Documento
from werkzeug.utils import secure_filename
from xhtml2pdf import pisa
from io import BytesIO

from controlador.usuario_controlador import app as usuario_app
from werkzeug.security import check_password_hash
import psycopg2
from functools import wraps
import os   

app = create_app

app = Flask(__name__)

app.secret_key = 'mi_clave_super_secreta'

reservas = Blueprint('reservas', __name__)
# Configuración de la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

# Función para verificar si el archivo tiene una extensión permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Directorio para guardar archivos subidos
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
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
@app.route('/user_vista')
def user_vista():
    return render_template('user_vista.html')
@app.route('/user_certificado')
def user_certificado():
    return render_template('user_certificado.html')
@app.route('/user_reserva')
def user_reserva():
    return render_template('user_reserva.html')

@reservas.route('/reservas', methods=['GET'])
def obtener_reservas():
    try:
        start_date = request.args.get('start')
        end_date = request.args.get('end')

        start_date = datetime.fromisoformat(start_date)
        end_date = datetime.fromisoformat(end_date)

        reservas = Reserva.query.filter(
            Reserva.fecha >= start_date,
            Reserva.fecha <= end_date,
            Reserva.aprobacion == True
        ).all()

        reservas_json = [
            {
                'id': reserva.id,
                'title': reserva.nombre,
                'start': reserva.fecha.isoformat()
            }
            for reserva in reservas
        ]

        return jsonify(reservas_json)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/user_reserva_registro')
def user_reserva_registro():
    return render_template('user_reserva_registro.html')
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

@app.route("/generar_certificado", methods=["POST"])
def generar_certificado():
    ultimo_folio = db.session.query(Certificado).order_by(Certificado.cert_folio.desc()).first()
    
    # Si no hay registros, el folio comenzará en 1438
    if ultimo_folio is None:
        nuevo_folio = 1438
    else:
        # Si ya existen registros, se incrementa el folio
        nuevo_folio = ultimo_folio.cert_folio + 1
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    rut = request.form['rut']
    direccion = request.form['direccion']
    comuna = request.form['comuna']
    fecha_emision = request.form['fecha_emision']

    # Crear el certificado
    nuevo_certificado = Certificado(
        cert_folio=nuevo_folio,  # Asignamos el nuevo folio
        cert_nombre=nombre,
        cert_rut=rut,
        cert_direccion=direccion,
        cert_comuna=comuna,
        cert_fecha=datetime.strptime(fecha_emision, '%Y-%m-%d')
    )
    print(nuevo_certificado.cert_nombre)
    print(nuevo_certificado.cert_rut)
    print(nuevo_certificado.cert_direccion)
    db.session.add(nuevo_certificado)
    db.session.commit()  # Commit para generar el cert_id

    # Procesar los archivos subidos
    for archivo in request.files.getlist('documentos[]'):
        if archivo and allowed_file(archivo.filename):
            file_content = archivo.read()

            # Crear los registros en la tabla Documento
            nuevo_documento = Documento(
                doc_nombre=secure_filename(archivo.filename),
                doc_tipo=archivo.content_type,
                doc_contenido=file_content,
                cert_id=nuevo_certificado.cert_id  # Asociar el documento al certificado
            )
            print(f"valor de nuevo_documento{nuevo_documento}")
            db.session.add(nuevo_documento)
    print(f"valor de nuevo_certificado {nuevo_certificado}")
    db.session.commit()

    flash('Certificado generado exitosamente y notificado al administrador.', 'success')
    return redirect(url_for('user_vista'))




@app.route("/ver_documento/<int:certificado_id>")
def ver_documento(certificado_id):
    certificado = Certificado.query.get(certificado_id)
    print(certificado)
    if certificado and certificado.documentos:
        return send_file(BytesIO(certificado.documentos), as_attachment=True, download_name="certificado.pdf", mimetype="application/pdf")
    return "Documento no encontrado", 404


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
    conn = connect_db()  # Conexión a la base de datos
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
            prioridad
        FROM 
            noticia
        WHERE 
            aprobacion = true
        ORDER BY 
            prioridad DESC, fecha_publicacion DESC
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
                "fecha_publicacion": row[4].strftime('%Y-%m-%d'),
                "prioridad": row[5]
            }
            for row in noticias
        ]

        return jsonify(noticias_list)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()
@app.route('/reserva', methods=['POST'])
def crear_reserva():
    data = request.json
    print("Datos recibidos del cliente:", data)
    # Obtener el último ID en la tabla
    ultimo_usuario = db.session.query(Reserva).order_by(Reserva.reserva_id.desc()).first()
    print("valor ultimo_usuarrio")
    nuevo_id = (ultimo_usuario.reserva_id + 1) if ultimo_usuario else 1
    nombre = data.get('nombre')
    rut_solicitante = data.get('rut_solicitante')
    fecha = data.get('fecha')
    periodo = data.get('periodo')  # Booleano para semanal
    aprobacion = data.get('aprobacion')  # Booleano para aprobación
    print("Datos recibidos del nombre:", nombre)

    conn = connect_db()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO reserva (reserva_id,reserva_nombre, rut_solicitante, fecha_reserva, periodo, aprobacion)
            VALUES (%s,%s, %s, %s, %s, %s) RETURNING reserva_id;
        """
        cursor.execute(query, (nuevo_id,nombre, rut_solicitante, fecha, periodo, aprobacion))
        reserva_id = cursor.fetchone()[0]
        print(f"valor de la cocnsulta reserva {reserva_id}")
        conn.commit()
        return jsonify({"id": reserva_id, "reserva_nombre": nombre, "fecha": fecha})
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
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
