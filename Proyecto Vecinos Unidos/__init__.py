# modelo/__init__.py
# modelo/__init__.py
import psycopg2
# modelo/usuario.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir el motor de conexión
DATABASE_URL = "postgresql://tu_usuario:tu_contraseña@localhost/zonaTesting"
engine = create_engine(DATABASE_URL)

# Crear una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para definir modelos
Base = declarative_base()

# Definir el modelo Usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    edad = Column(Integer)
    correo = Column(String, unique=True, index=True)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

def conectar_db():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="nombre_base_de_datos",
            user="tu_usuario",
            password="tu_contraseña"
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

BASE_DE_DATOS = "db.sqlite3"
