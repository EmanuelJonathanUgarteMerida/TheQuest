# TheQuest
This is a game that consist in crossing asteroids without collide against them to level complete.

# Windows
# Primero tener instalado python: 
- https://www.python.org/downloads/

# Comprobar la instalación Python:
- En ventana del sistema: py --version ó python --version
- La versión confirma instalación correcta

# Descargar Git 
- https://git-scm.com/download/win
- Todo siguiente

# Comprobar la instalación Git:
- En ventana del sistema: git version
- La versión confirma instalación correcta

# Descargar proyecto:
- En ventana del sistema, posicionarnos en la carpeta donde queramos descargar el proyecto
- En ventana del sistema: git clone https://github.com/EmanuelJonathanUgarteMerida/TheQuest.git

# Creamos variable de entorno:
- Nos posicionamos dentro de la carpeta del proyecto descargado (The Quest)
- En ventana del sistema: py -m venv env ó py -m venv env
- Activamos la variable creada (env): .\env\Scripts\activate

# Descargamos librerias del proyecto
- En ventana deñ sistema, para comprobar libererias disponibles: pip list
- En ventana del sistema, para instalar las del proyecto: pip install -r requirements.txt
- En ventana del sistema, para ver las isntaladas: pip list

# Lanzamos el juego
- py main.py

# Estadísticas
- Aparecerá al completar el juego
- Perder todas las vidas implica reiniciar juego
- Si no se reinicia el juego, se vuelve a portada

# Settings __init__.py
- **SC_HEIGHT** determina altura de ventana
- **SC_WIDTH** determina anchuura de ventana
- **G_LEVEL_LIMIT_TIME** determina la duración de cada nivel
- **G_REMAINING_TIME** determina los segundos de cuenta atrás al perder las vidas
- **G_LIVES_LIMIT** determina las vidas en el juego

