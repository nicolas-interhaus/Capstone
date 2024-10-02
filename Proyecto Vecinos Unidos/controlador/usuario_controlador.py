from modelo.vecinos import Usuario
from vista.usuario_vista import mostrar_usuario, solicitar_datos_usuario
# controlador/usuario_controlador.py
from modelo.vecinos import Usuario, SessionLocal

def crear_usuario(nombre, edad, correo):
    session = SessionLocal()
    nuevo_usuario = Usuario(nombre=nombre, edad=edad, correo=correo)
    session.add(nuevo_usuario)
    session.commit()
    session.close()
    print("Usuario creado exitosamente.")

# controlador/usuario_controlador.py
def obtener_usuarios():
    session = SessionLocal()
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"Nombre: {usuario.nombre}, Edad: {usuario.edad}, Correo: {usuario.correo}")
    session.close()
