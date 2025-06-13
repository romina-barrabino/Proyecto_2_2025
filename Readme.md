Creo e inicio una sesion en https://www.themoviedb.org/login, luego copio la API.
Instalo SQL Microsoft Server y creo una base de datos que llamo "moviesbd".
Creo una carpeta en la computadora que llamo "Proyecto_2_2025" y la abro en el Visual Studio.
Descargo e instalo git desde https://git-scm.com/downloads/win
Verifico la version de git 
git --version
Creo la carpeta .env en Visual Studio con la API y con los datos para la conexion con SQL
Creo la carpeta .gitignore en Visual Studio con el siguiente script:
.env
En la terminal de Visual Studio instalo dotenv 
pip install python-dotenv
En la terminal de Visual Studio se hace la conexion entre la carpeta .env y .gitignore
git rm --cached .env
Creo una carpeta llamada "Scripts" y le agrego 2 archivos, uno llamado "scripts_movies.py" y otro "scripts_movies_popularity.py" donde se pondran los scripts para la extracción, transformación y carga de datos desde la página web hasta SQL.
Conecto desde la terminal a Visual Studio con un repositorio en GitHub que llamare "Proyecto_2_2025"
git init
git add .
git commit -m "Iniciando proyecto"