# Proyectoprueba
# Proyecto web para artista digital


 instrucciones
 1--instalar dependencias en la terminal
 pip install django
 pip install mysqlclient

 2--iniciar xampp msql apache

#3-- crear una base de datos llamada "pruebadb" en mysql ¡¡importante no poner ninguna tabla, dejar en blanco

 4----volver a vs code y en la terminal poner

 py manage.py makemigrations
 py manage.py migrate

esto hara que se creen las tablas necesarias en la base de datos

5---poner en la terminal:
py manage.py runserver

y entrar en http://127.0.0.1:8000/ en el navegador