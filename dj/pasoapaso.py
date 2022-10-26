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
    Controlador: Funciones (Views). Establece la relacion entre back y front. Cuestiones de logica


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
                    Reemplazar valor de TIME_ZONE en settings.py (proyecto\proyecto\settings.py)
                    por "America/Argentina/Buenos_Aires"

        2) Crear apps (permiten separar las funciones del proyecto)
           python manage.py startapp nombreapp

        3) Registrar app
            agregar a settings.py (se recomienda separar en listas las apps de "INSTALLED_APPS" segun su origen
            y que "INSTALLED_APPS" sea su concatenacion)
        
        3) Crear superadmin
           python manage.py createsuperuser
        
        4) Establecer mysqlclient como driver de conexion entre la base de datos y la proyeccion
            DATABASES = {
                'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'heroesApp',
                'USER': 'root',
                'PASSWORD': '',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                }
            }
        
        5) Crear tablas "base" para Django
            make migrations
        
        6) Crear Model
            Darlo de alta como clase
            class nombremodelo(models.model)
            Darle atributos 
            atributo = models.tipodedato(Argumentos del atributo: maxima extension, si es unico
            o no, si es un desplegable de opciones y algunos obligatorios segun el tipo de dato)
        
        7) Registrar Model
            en admin.py
            Al inicio: Importar modelo
                from app.models import Model
            Al final:
                admin.site.register(Model)
        
        8) Crear View (vistas basadas en clases)

            eliminar funcion render
            importar funciones de REST Framework
                from rest_framework.views import APIView
                from rest_framework.response import Response
                from rest_framework import status

            importar modelo creado
                from model.models import Model
            class ModelApiView(ApiView)

            importar serializers
                from app.serializer import ModelSerializer

            Definir las funciones
            def get/post/put(self, request)

            Establecer contacto con la Tabla de la BD
                Si yo quiero trabajar con todos los objetos del modelo:
                    model = Model.objects.all()

            Igualar lista a lista serializada
                model_serializer = ModelSerializer(Model, many = True)
                El "many" es necesario para especificar que se va a trabajar con muchos valores
            
            Definir Response (y agregar data y status)
                return Response(
                    data = model_serializer.data
                    status = status.X
                )

        ) Crear serializer
            Importar funciones desde rest
                from rest_framework import serializers
            Importar modelos creados
                from products.models import Product
            
            Nombrar Serializer segun convencion
                class ModelSerializer(serializers.ModelSerializer): Este ultimo ModelSerializer 
                es distinto del primero
            
            Definir subclase Meta, dentro de esta determinar el modelo y los datos con los que
            se trabajan (si son todos: "__all__", si son una parte: escribirlos dentro de una
            tupla)
                class Meta:
                    model = Model,
                    fields = "__all__"


        
        9) Crear URLS
            Dar de alta urls.py en carpeta de la app
                Importar views al archivo
                    from nombreapp.view import ModelAPIView
                Agregar url
                    path("path deseado/", ModelAPIView.as_view(), name = "nombre")

            Dar de alta url en urls.py general
                agregar el paquete include a lo importado desde django.urls
                agregar url
                    path('path deseado/', include("app.urls")),

            

"""