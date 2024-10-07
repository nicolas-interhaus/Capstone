import psycopg2

# Establecer conexión
conn = psycopg2.connect(
    host="localhost",         # Cambia si es un servidor remoto
    database="Capstone",      # Tu nombre de la base de datos
    user="postgres",         # Tu usuario de PostgreSQL
    password="admin"   # Tu contraseña de PostgreSQL
)

# Crear un cursor
cur = conn.cursor()

# Ejemplo de ejecución de una consulta
cur.execute("SELECT * FROM vecinos;")

# Obtener los resultados
rows = cur.fetchall()

for row in rows:
    print(row)

# Cerrar cursor y conexión
cur.close()
conn.close()
