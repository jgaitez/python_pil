"""
Pasos previos
    1) Creacion de entorno virtual
        python -m venv env

    2) Iniciar entorno virtual
        .\env\Scripts\activate

    3) Instalar Django (y relacionados)
        pip install Django

    4) Instalar Django REST Framework

    5) Chequear que el interprete sea el del proyecto

Anotaciones:
    - Modelo vista controlador
    Modelo: Tipo de base de datos (tablas)
    Controlador: Funciones (Views). Establece la relacion entre back y front
    Vista: Frontend. Recibe archivos JSON


Creacion de Web con Django y Django Rest Framework
    CUESTIONES PREVIAS

        1) Manage.py
            Administrador del proyecto

        2) Archio URLS
        3) Archivo WSGI
        4) 

    CREACION DE PROYECTO
        0) Iniciar servidor Django
            python manage.py runserver

        1) Crear proyecto
            django-admin startproject nombreproyecto

            OPCIONALES:
                Poner en español de argentina:
                    Reemplazar valor de LANGUAGE_CODE en settings.py (proyecto\proyecto\settings.py) por "es-ar"
                Poner el servidor en horario argentino
                    Reemplazar valor de TIME_ZONE en settings.py (proyecto\proyecto\settings.py) por "America/Argentina/Buenos_Aires"

        2) Crear apps (permiten separar las funciones del proyecto)
           python manage.py startapp nombreapp
        
        3) Crear superadmin
           python manage.py createsuperuser

"""