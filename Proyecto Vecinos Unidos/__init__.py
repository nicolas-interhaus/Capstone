from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import controlador
import models


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/capstone'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Crear todas las tablas aquí

    return app


# Inicia la aplicación si se ejecuta directamente este archivo
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Puedes cambiar debug=False en producción
