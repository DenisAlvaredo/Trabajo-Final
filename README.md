CREAR UN ENTORNO Y ACTIVARLO
DENTRO DE LA CONSOLA CON EL ENTORNO ACTIVO, POSICIONARSE EN LA RUTA DONDE SE ENCUENTRA EL ARCHIVO "REQUISITOS.TXT" Y INGRESAR EL SIGUIENTE COMANDO: pip install -r requisitos.txt
DEBERIA PROCEDER A INSTALAR TODOS LOS REQUERIMIENTOS PARA PODER LEVANTAR EL PROYECTO SIN PROBLEMAS

Si se va a probar el proyecto localmente con una base de datos en SQL Express, se debe hacer lo siguiente despues de descargar:

1-Borrar la base de datos antigua.
2-Descargar todo (git fetch, git restore . , git pull) o, en su defecto, (git clone)
3-Borrar las migraciones del proyecto
4-Comentar las líneas 5, 7, 9, 10, 17, 18 y 19 del archivo posts/forms.py, y las líneas 6, 8, 10, 11, 24, 25 y 26 del archivo posts/admin.py
5-Ejecutar makemigrations, migrate, runserver
6-Descomentar las lineas anteriormente comentadas y guardar.