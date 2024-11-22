import psycopg2
from psycopg2 import sql
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuración de la conexión a PostgreSQL
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'capstone',
    'user': 'postgres',
    'password': 'admin'
}

# Función para conectar a la base de datos
def connect_db():
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

# Ruta para generar un certificado
@app.route('/generar_certificado', methods=['POST'])
def generar_certificado():
    data = request.json  # Asegúrate de enviar datos JSON
    nombre = data.get('nombre')
    rut = data.get('rut')
    direccion = data.get('direccion')
    comuna = data.get('comuna')
    fecha = data.get('fecha')

    # Validar que los datos están completos
    if not all([nombre, rut, direccion, comuna, fecha]):
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    # Conectar a la base de datos
    conn = connect_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

    cursor = conn.cursor()

    # Consulta SQL para insertar los datos
    query = """
    INSERT INTO certificado_residencia (cert_nombre, cert_rut, cert_direccion, cert_comuna, cert_fecha_emision)
    VALUES (%s, %s, %s, %s, %s)
    """

    try:
        # Ejecutar la consulta
        cursor.execute(query, (nombre, rut, direccion, comuna, fecha))
        conn.commit()
        return jsonify({'message': 'Certificado generado exitosamente'}), 201
    except Exception as e:
        conn.rollback()
        print(f"Error al ejecutar la consulta: {e}")
        return jsonify({'error': f'Error al generar certificado: {e}'}), 500
    finally:
        cursor.close()
        conn.close()

# Ruta para obtener certificados (opcional)
@app.route('/certificados', methods=['GET'])
def obtener_certificados():
    conn = connect_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

    cursor = conn.cursor()
    query = "SELECT * FROM certificados_residencia"

    try:
        cursor.execute(query)
        certificados = cursor.fetchall()
        result = []
        for cert in certificados:
            result.append({
                'id': cert[0],
                'nombre': cert[1],
                'rut': cert[2],
                'direccion': cert[3],
                'comuna': cert[4],
                'fecha_emision': cert[5].strftime('%Y-%m-%d')
            })
        return jsonify(result), 200
    except Exception as e:
        print(f"Error al obtener certificados: {e}")
        return jsonify({'error': f'Error al obtener certificados: {e}'}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
