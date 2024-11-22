from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost/base_datos'
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    Usuario_id = db.Column(db.Integer, primary_key=True)
    User = db.Column(db.String(200), nullable=False)
    Contraseña = db.Column(db.String(200), nullable=False)
    Cargo = db.Column(db.String(200), nullable=False)
    Perfil = db.Column(db.String(200), nullable=False)
    Fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

db.create_all()

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'Usuario_id': u.Usuario_id,
        'User': u.User,
        'Contraseña': u.Contraseña,
        'Cargo': u.Cargo,
        'Perfil': u.Perfil,
        'Fecha_registro': u.Fecha_registro
    } for u in usuarios])

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    usuario = Usuario.query.get_or_404(id)
    usuario.User = data['usuario']
    usuario.Cargo = data['cargo']
    db.session.commit()
    return jsonify({'message': 'Usuario actualizado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)
