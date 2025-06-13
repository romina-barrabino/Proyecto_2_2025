#Extraer datos de películas desde la API de TMDB.
#Librerias
import os
import requests
import pyodbc

#Parámetros
API_KEY = '19da0f4b67274245671f080a277d4972'
COUNTRY = 'Argentina'
SQL_SERVER_CONFIG = {
    'DRIVER': '{ODBC Driver 17 for SQL Server}',
    'SERVER': 'localhost',
    'DATABASE': 'movies', #base de datos en SQL
    'UID': 'sa',
    'PWD': 'simpleplan1994'
}

#Extracción de datos
def extraer_datos(api_key, country):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    print("Respuesta de la API:", data)
    return data

#Transformar los datos de popularidad en categorías: Alta, Media y Baja.
#Transformación de datos
def transformar_datos(data):
    try:
        return {
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
        }
    except KeyError as e:
        raise Exception(f"Se produjo un error en: {e}")
print ("Se transformaron los datos correctamente")

#Cargue los datos en SQL Server para su análisis posterior.
#Carga de datos
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
        print(f" Intentando conectar a: {conn_str}")
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print(" Conexión establecida con el servidor.")

#Creacion de la tabla 'movies_popularity' en la base de datos de SQL
        cursor.execute("""
            SELECT COUNT(*) 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_NAME = 'movies_popularity'
        """)
        table_exists = cursor.fetchone()[0]

        if table_exists == 0:
            print("La tabla 'movies_popularity' no existe. Creándola...")
            cursor.execute("""
                CREATE TABLE movies_popularity (
                    id_de_película INT IDENTITY(1,1) PRIMARY KEY,
                    título VARCHAR(50),
                    fecha_de_lanzamiento DATETIME,
                    idioma_original VARCHAR(50),
                    promedio_de_votos INT
                    recuento_de_votos INT
                    popularidad VARCHAR(50),
                    resumen VARCHAR(300),
                    ids_de_género INT
                )
            """)

            popularidad_
            categoría (BAJA, MEDIA, ALTA)
            conn.commit()
            print(" Tabla 'movies_popularity' creada.")

        insert_query = """
            INSERT INTO movies_popularity (country, temperature, humidity)
            VALUES (?, ?, ?)
        """
        cursor.execute(insert_query, (
            datos['country'],
            datos['temperature'],
            datos['humidity']
        ))
        conn.commit()
        print(" Datos insertados en la tabla 'movies_popularity'.")

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
    datos_extraidos = extraer_datos(API_KEY,COUNTRY)
    datos_transformados = transformar_datos(datos_extraidos)
    cargar_datos(datos_transformados, SQL_SERVER_CONFIG)
    print ("Se realizo el proceso ETL correctamente")

if __name__ == '__main__':
    ejecutar_etl()
