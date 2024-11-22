from flask import Flask, request, render_template, redirect, send_file
from fpdf import FPDF
from models.usuario import Usuario
import io

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
    cargo = request.form['cargo']
    email = request.form['email']

    # Llamar a la función que inserta en la BD
    Usuario.insertar_usuario(nombres, apellido_paterno, apellido_materno, fec_nacimiento, edad, genero, direccion, comuna, cargo, email)

    return redirect('/')
@app.route('/generar-certificado', methods=['POST'])
def generar_certificado():
    nombre = request.form['nombre']
    rut = request.form['rut']
    direccion = request.form['direccion']
    comuna = request.form['comuna']
    fecha = request.form['fecha']

    # Crear un PDF con FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Agregar contenido al PDF
    pdf.cell(200, 10, txt="Certificado de Residencia", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True)
    pdf.cell(200, 10, txt=f"RUT: {rut}", ln=True)
    pdf.cell(200, 10, txt=f"Dirección: {direccion}", ln=True)
    pdf.cell(200, 10, txt=f"Comuna: {comuna}", ln=True)
    pdf.cell(200, 10, txt=f"Fecha de emisión: {fecha}", ln=True)

    # Generar el PDF en memoria
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    # Devolver el archivo PDF al usuario
    return send_file(pdf_output, as_attachment=True, download_name="certificado_residencia.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)

def mostrar_usuario(usuario):
    print(f"Nombre: {usuario.nombre}")
    print(f"Edad: {usuario.edad}")
    print(f"Correo: {usuario.correo}")

def solicitar_datos_usuario():
    nombre = input("Ingresa el nombre del usuario: ")
    edad = int(input("Ingresa la edad del usuario: "))
    correo = input("Ingresa el correo del usuario: ")
    return nombre, edad, correo
