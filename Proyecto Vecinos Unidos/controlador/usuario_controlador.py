from flask import Flask, request, render_template, redirect
from modelo.vecinos import Usuario

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('registro.html')  # Esto es el archivo de la vista

@app.route('/registrar', methods=['POST'])
def registrar_usuario():
    nombres = request.form['nombres']
    apellido_paterno = request.form['apellido_paterno']
    apellido_materno = request.form['apellido_materno']
    fec_nacimiento = request.form['fecha_nacimiento']
    edad = request.form['edad']
    genero = request.form['genero']
    direccion = request.form['direccion']
    comuna = request.form['comuna']
    cargo = "vecino"
    email = request.form['email']

    # Llamar a la función que inserta en la BD
    Usuario.insertar_usuario(nombres, apellido_paterno, apellido_materno, fec_nacimiento, edad, genero, direccion, comuna, cargo, email)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
