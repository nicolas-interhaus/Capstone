from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from models import db, Noticias  # Asegúrate de importar correctamente tu modelo

app = Flask(__name__)
app.secret_key = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost/tu_base_datos'
db.init_app(app)

@app.route('/noticias', methods=['GET', 'POST'])
def administrar_noticias():
    if request.method == 'POST':
        # Capturamos los datos del formulario para agregar una noticia
        titulo = request.form['titulo']
        detalle = request.form['detalle']
        autor = request.form['autor']
        fecha_publicacion = request.form['Fecha_publicacion']

        nueva_noticia = Noticias(
            titulo=titulo,
            detalle=detalle,
            autor=autor,
            fecha_publicacion=datetime.strptime(fecha_publicacion, '%Y-%m-%d')
        )
        db.session.add(nueva_noticia)
        db.session.commit()
        flash('Noticia agregada exitosamente.', 'success')
        return redirect(url_for('administrar_noticias'))

    # Obtenemos todas las noticias para mostrarlas en la vista
    noticias = Noticias.query.all()
    return render_template('noticias.html', noticias=noticias)

@app.route('/publicar/<int:noticia_id>', methods=['POST'])
def publicar_noticia(noticia_id):
    # Aquí puedes agregar lógica para cambiar el estado de la noticia a "publicada"
    flash(f'Noticia {noticia_id} publicada con éxito.', 'success')
    return redirect(url_for('administrar_noticias'))

@app.route('/rechazar/<int:noticia_id>', methods=['POST'])
def rechazar_noticia(noticia_id):
    # Aquí puedes agregar lógica para eliminar o marcar como rechazada la noticia
    flash(f'Noticia {noticia_id} rechazada.', 'danger')
    return redirect(url_for('administrar_noticias'))

if __name__ == '__main__':
    app.run(debug=True)
