from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route('/certificado', methods=['GET', 'POST'])
def generar_certificado():
    if request.method == 'POST':
        # Capturamos los datos del formulario
        nombre = request.form['nombre']
        rut = request.form['rut']
        direccion = request.form['direccion']
        comuna = request.form['comuna']
        fecha = request.form['fecha']

        # Aquí podrías agregar lógica para generar el PDF o guardar en la base de datos
        # Simulamos un mensaje de éxito y una URL de PDF de ejemplo
        pdf_url = url_for('static', filename='certificado_ejemplo.pdf')
        flash('Certificado generado exitosamente.', 'info')
        return render_template('certificado.html', pdf_url=pdf_url)

    return render_template('admin_vista.html')

if __name__ == '__main__':
    app.run(debug=True)
