from __init__ import create_app
from datetime import datetime
from flask import Flask, render_template, request, jsonify,redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models.usuario import Usuario
from models.vecinos import Vecino

app = create_app()

app = Flask(__name__)
app.secret_key = 'mi_clave_super_secreta'

# Configuración de la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

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

@app.route('/admin_noticias')
def admin_noticias():
    return render_template('admin_noticias.html')

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

@app.route('/query_string')
def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return 'Listo'

@app.before_request
def before_request():
    print("Antes de la peticion de algo")

@app.after_request
def after_request(response):
    print("Despues de la peticion de algo")
    return response

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

@app.route('/ingreso', methods=['POST'])
def ingreso():
    # Obtener los datos del formulario enviados mediante POST
    datos = request.form
    print("Datos recibidos:", datos)  # Depuración para ver si los datos son recibidos correctamente

    rut = datos.get('rut')
    nombres = datos.get('nombres')
    apellido_paterno = datos.get('apellido_paterno')
    apellido_materno = datos.get('apellido_materno')
    fecha_nacimiento = datos.get('fecha_nacimiento')
    genero = datos.get('genero')
    direccion = datos.get('direccion')
    comuna = datos.get('comuna')
    email = datos.get('email')
    
    # Verifica los valores de los datos
    print(f"Rut: {rut}, Nombres: {nombres}, Apellido Paterno: {apellido_paterno}")
    
    # Validaciones básicas
    errores = []
    if not rut: errores.append("Rut es obligatorio")
    if not nombres: errores.append("Nombres son obligatorios")
    if not apellido_paterno: errores.append("Apellido paterno es obligatorio")
    if not apellido_materno: errores.append("Apellido materno es obligatorio")
    if not fecha_nacimiento: errores.append("Fecha de nacimiento es obligatoria")
    if not genero: errores.append("Género es obligatorio")
    if not direccion: errores.append("Dirección es obligatoria")
    if not comuna: errores.append("Comuna es obligatoria")
    if not email: errores.append("Email es obligatorio")
    
    print("Errores encontrados:", errores)
    
    if errores:
        # Mostrar mensajes de error y redirigir al formulario
        for error in errores:
            flash(error, 'danger')
        return render_template('home.html')
    
    # Crear un nuevo registro para la base de datos
    try:
        nuevo_vecino = Vecino(
            rut=rut,
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            direccion=direccion,
            comuna=comuna,
            email=email,
            fecha_registro=datetime.utcnow()  # Fecha actual
        )
        print("Nuevo vecino:", nuevo_vecino)
        db.session.add(nuevo_vecino)
        db.session.commit()

        # Mensaje de éxito y redirección
        flash("Usuario registrado exitosamente", "success")
        return redirect(url_for('registro_vecino'))
    except Exception as e:
        # Manejo de errores de base de datos
        db.session.rollback()
        flash(f"Error al registrar usuario: {str(e)}", "danger")
        return render_template('registro.html')

    
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

 


if __name__ == '__main__':
    app.run(debug=True)
