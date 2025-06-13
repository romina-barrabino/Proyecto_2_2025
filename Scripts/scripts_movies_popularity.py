#Creo la tabla 'movies_popularity' con los datos de la tabla 'movies'

#Libreria
import pyodbc
import os
from dotenv import load_dotenv

#Cargo las variables desde el archivo .env
load_dotenv()

#Llamo a los parametros desde el archivo .env
API_KEY = os.getenv('API_KEY')

SQL_SERVER_CONFIG = {
    'DRIVER': os.getenv('SQL_DRIVER'),
    'SERVER': os.getenv('SQL_SERVER'),
    'DATABASE': os.getenv('SQL_DATABASE'),
    'UID': os.getenv('SQL_UID'),
    'PWD': os.getenv('SQL_PWD')
}

#Conecto con el servidor SQL
def cargar_datos(config):
    try:
        print(" Preparando cadena de conexión...")
        conn_str = (
            f"DRIVER={config['DRIVER']};"
            f"SERVER={config['SERVER']};"
            f"DATABASE={config['DATABASE']};"
            f"UID={config['UID']};"
            f"PWD={config['PWD']};"
        )
        print(" Intentando conectar al servidor de SQL...")
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print(" Conexión establecida con el servidor.")

# Creo la tabla 'movies_popularity'
        cursor.execute("""
            IF OBJECT_ID('movies_popularity', 'U') IS NOT NULL
                DROP TABLE movies_popularity;
        """)
        cursor.execute("""
            SELECT 
                id_de_película, 
                título,  
                popularidad
            INTO movies_popularity
            FROM movies;
        """)
        conn.commit()
        print(" Tabla 'movies_popularity' creada correctamente.")

    except Exception as e:
        print(" Error durante la creación de la tabla:")
        print(e)

    finally:
        cursor.close()
        conn.close()
        print(" Conexión cerrada.")

# Ejecutar función
if __name__ == '__main__':
    cargar_datos(SQL_SERVER_CONFIG)