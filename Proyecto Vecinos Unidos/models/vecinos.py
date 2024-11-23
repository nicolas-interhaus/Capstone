from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Vecino
class Vecino(db.Model):
    __tablename__ = 'vecinos'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    rut = db.Column(db.String(20), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    comuna = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Crear tablas en la base de datos


# Ruta para obtener todos los vecinos
@app.route('/vecinos', methods=['GET'])
def obtener_vecinos():
    vecinos = Vecino.query.all()
    return jsonify([{
        'id': v.id,
        'nombres': v.nombres,
        'apellido_paterno': v.apellido_paterno,
        'apellido_materno': v.apellido_materno,
        'fecha_nacimiento': v.fecha_nacimiento.strftime('%Y-%m-%d'),
        'rut': v.rut,
        'edad': v.edad,
        'genero': v.genero,
        'direccion': v.direccion,
        'comuna': v.comuna,
        'email': v.email,
        'fecha_registro': v.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')
    } for v in vecinos])

# Ruta para actualizar un vecino
@app.route('/vecinos/<int:id>', methods=['PUT'])
def actualizar_vecino(id):
    data = request.json
    vecino = Vecino.query.get_or_404(id)

    # Actualizar los campos permitidos
    vecino.nombres = data.get('nombres', vecino.nombres)
    vecino.apellido_paterno = data.get('apellido_paterno', vecino.apellido_paterno)
    vecino.apellido_materno = data.get('apellido_materno', vecino.apellido_materno)
    vecino.direccion = data.get('direccion', vecino.direccion)
    vecino.comuna = data.get('comuna', vecino.comuna)
    vecino.email = data.get('email', vecino.email)

    db.session.commit()
    return jsonify({'message': 'Vecino actualizado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)
