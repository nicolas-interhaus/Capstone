from __init__ import create_app
from flask import Flask, render_template, request

app = create_app()

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

@app.route('/ingreso')
def ingreso():
    return render_template('ingreso.html')

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

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
