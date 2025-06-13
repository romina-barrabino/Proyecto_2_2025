# Página web a utilizar
https://www.themoviedb.org/login (Inicio una sesion y creo una API).

# Aplicaciones a instalar: 
SQL Microsoft Server (creo en ella una base de datos que llamo "moviesbd")
Visual Studio
Git (desde https://git-scm.com/downloads/win)

# Carpetas en Visual Studio:
Proyecto_2_2025/
│
├── Scripts/
│   ├── scripts_movies.py
│   └── scripts_movies_popularity.py
│
├── .gitignore
├── .env
├── README.md
└── Imagenes

# Detalle de carpetas:
.) Proyecto_2_2025= Carpeta creada en la terminal local
.) scripts_movies.py= Scripts para la extracción, transformación y carga de datos desde la página web hasta SQL en la tabla movies.
.) scripts_movies_popularity.py= Scripts para la extracción, transformación y carga de datos desde la página web hasta SQL en la tabla movies_popularity.
.) .env= Posee los datos para la conexion con SQL y con la API.
.) .gitignore= Posee el nombre de los archivos que no deberan visualizarse en el Github.
.) Imagenes= Tiene capturas de pantalla de los pasos realizados.

# Instalaciones y/o scripts para la terminal de Visual Studio: 
a) Instalacion de dotenv: pip install python-dotenv
b) Evitar la visualizacion de la carpeta .env en GitHub: git rm --cached .env
c) Verificacion de la instalacion de git: git --version

# Conexion entre Visual Studio y un repositorio en GitHub que llamare "Proyecto_2_2025"
git init
git add .
git commit -m "Iniciando proyecto"