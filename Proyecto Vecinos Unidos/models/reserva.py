from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/capstone'
db = SQLAlchemy(app)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

@app.route('/')
def index():
    return render_template('admin_reserva.html')

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'GET':
        reservas = Reserva.query.all()
        eventos = [{"id": r.id, "title": r.nombre, "start": r.fecha.isoformat()} for r in reservas]
        return jsonify(eventos)
    
    if request.method == 'POST':
        data = request.json
        nueva_reserva = Reserva(nombre=data['nombre'], fecha=datetime.fromisoformat(data['fecha']))
        db.session.add(nueva_reserva)
        db.session.commit()
        return jsonify({"id": nueva_reserva.id, "message": "Reserva creada con éxito"})

if __name__ == '__main__':
    app.run(debug=True)
