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
    edad = request.form['edad']  # Tendrías que calcular la edad a partir de la fecha de nacimiento
    genero = request.form['genero']
    direccion = request.form['direccion']
    comuna = request.form['comuna']
    cargo = "vecino"  # Por ejemplo, puedes tener este valor fijo o ingresarlo
    email = request.form['email']

    # Crear una instancia del modelo Usuario
    nuevo_usuario = Usuario(nombres, apellido_paterno, apellido_materno, fec_nacimiento, edad, genero, direccion, comuna, cargo, email)
    
    # Aquí puedes guardar los datos en una base de datos o archivo
    print(nuevo_usuario)  # Por ahora, solo imprimimos el usuario

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
