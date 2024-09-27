def mostrar_usuario(usuario):
    print(f"Nombre: {usuario.nombre}")
    print(f"Edad: {usuario.edad}")
    print(f"Correo: {usuario.correo}")

def solicitar_datos_usuario():
    nombre = input("Ingresa el nombre del usuario: ")
    edad = int(input("Ingresa la edad del usuario: "))
    correo = input("Ingresa el correo del usuario: ")
    return nombre, edad, correo
