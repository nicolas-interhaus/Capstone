import psycopg2
from flask import Flask, request, render_template

app = Flask(__name__)

# Configuración de la conexión a PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",  # Cambiar si es un servidor remoto
            database="Capstone",  # Nombre de tu base de datos
            user="postgres",  # Usuario de PostgreSQL
            password="admin"  # Contraseña de PostgreSQL
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

@app.route('/generar_certificado', methods=['POST'])
def generar_certificado():
    nombre = request.form['nombre']
    rut = request.form['rut']
    direccion = request.form['direccion']
    comuna = request.form['comuna']
    fecha = request.form['fecha']

    # Conectarse a la base de datos
    conn = connect_db()
    if conn is None:
        return "Error al conectar con la base de datos", 500

    cursor = conn.cursor()

    # Consulta SQL para insertar los datos
    query = """
    INSERT INTO certificados_residencia (nombre, rut, direccion, comuna, fecha_emision)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    try:
        # Ejecutar la consulta
        cursor.execute(query, (nombre, rut, direccion, comuna, fecha))
        conn.commit()
        return "Certificado generado exitosamente"
    except Exception as e:
        conn.rollback()
        return f"Error al generar certificado: {e}"
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
