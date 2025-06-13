#Libreria
import requests
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

#Extracción de datos
def extraer_datos(api_key):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=es-ES&page=1'
    response = requests.get(url)
    data = response.json()
    print("Se extrayeron los datos correctamente")
    return data['results']

#Transformar los datos de popularidad en categorías: Alta, Media y Baja.
def transformar_datos(data):
    try:
        datos_transformados = {
            'título': data['title'],
            'fecha_de_lanzamiento': data['release_date'],
            'idioma_original': data['original_language'],
            'promedio_de_votos': data['vote_average'],
            'recuento_de_votos': data['vote_count'],
            'popularidad': (
                "Alta" if data['popularity'] > 1000 else
                "Media" if data['popularity'] > 500 else
                "Baja"
            ),
            'resumen': data['overview'],
            'ids_de_género': data['genre_ids'][0] if data['genre_ids'] else None
        }
        print("Se transformaron los datos correctamente")
        return datos_transformados
    except KeyError as e:
        raise Exception(f"Se produjo un error en: {e}")

#Cargue los datos crudos en la tabla 'movies' en SQL Server.
def cargar_datos(datos, config):
    try:
        print(" Preparando cadena de conexión...")
        conn_str = (
            f"DRIVER={config['DRIVER']};"
            f"SERVER={config['SERVER']};"
            f"DATABASE={config['DATABASE']};"
            f"UID={config['UID']};"
            f"PWD={config['PWD']};"
        )
        print(f" Intentando conectar al servidor de SQL")
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print(" Conexión establecida con el servidor.")

#Creacion de la tabla 'movies' en la base de datos de SQL
        cursor.execute("""
            SELECT COUNT(*) 
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_NAME = 'movies'
        """)
        table_exists = cursor.fetchone()[0]

        if table_exists == 0:
            print("La tabla 'movies' no existe. Creándola...")
            cursor.execute("""
                CREATE TABLE movies (
                    id_de_película INT IDENTITY(1,1) PRIMARY KEY,
                    título VARCHAR(50),
                    fecha_de_lanzamiento DATETIME,
                    idioma_original VARCHAR(50),
                    promedio_de_votos INT,
                    recuento_de_votos INT,
                    popularidad VARCHAR(50),
                    resumen NVARCHAR(MAX),
                    ids_de_género INT
                )
            """)
            conn.commit()
            print(" Tabla 'movies' creada.")

        insert_query = """
            INSERT INTO movies (título, fecha_de_lanzamiento, idioma_original, promedio_de_votos, recuento_de_votos,
                    popularidad, resumen, ids_de_género)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            datos['título'],
            datos['fecha_de_lanzamiento'],
            datos['idioma_original'],
            datos['promedio_de_votos'],
            datos['recuento_de_votos'],
            datos['popularidad'],
            datos['resumen'],
            datos['ids_de_género']
        ))
        conn.commit()
        print(" Datos insertados en la tabla 'movies'.")

    except Exception as e:
        import traceback
        print(" Error durante la carga de datos:")
        traceback.print_exc()

    finally:
        cursor.close()
        conn.close()
        print(" Conexión cerrada.")

#Proceso ETL completo
def ejecutar_etl():
    datos_extraidos = extraer_datos(API_KEY)
    for pelicula in datos_extraidos:
        datos_transformados = transformar_datos(pelicula)
        cargar_datos(datos_transformados, SQL_SERVER_CONFIG)
    print ("Se realizo el proceso ETL correctamente")

if __name__ == '__main__':
    ejecutar_etl()
