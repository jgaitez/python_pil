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
            Las Funciones pueden estar integradas en la misma clase o no.
            En el segundo caso 

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

            Traducir de json a BD
                    serializer = ModelSerializer(data=request.data)

            Agregar validacion de datos (por ejemplo al usar el metodo post, para evitar cargar 
            duplicados o valores mas extensos de lo permitido)
                if serializer.is_valid():
                    serializer.save()

            
            OTRAS FUNCIONES

            Obtener info de un objeto en particular
                class ModelDetalleApiView(APIView):

                    def get(self, request, pk):
                        #Nos retorna mas info de un un heroe en particular
                        
                        model = model.objects.filter()
                        es un filtro en general de acuerdo al criterio que se establece (que puede arrojar
                        varios resultados)
                        model = model.objects.get()
                        devuelve el primer valor
                        heroe_serializer = HeroSerializer(heroe, data=request.data)
                        traduzco el valor y se lo entrego al serializer junto a la nueva data

                        return Response(
                            data=heroes_serializer.data,
                            status=status.HTTP_200_OK
                        )
            
            Gestion de ERRORES
            Para que al momento de que aparezca un error, se brinde informacion apropiada para alguien no tecnico
            y para evitar tener que hacerlo en todas las funciones, se usan helpers

            Se crea dentro de la carpeta del modelo la carpeta "helpers"
            se crea el __init__
            Se crea dentro un archivo para gestionar los errores:
                Se importa el modelo sobre el cual trabajar
                Se empiezan a hacer las funciones
                    def hayError(pk):
                        try:
                            model = Hero.objects.get(id=pk)

                            return True, heroe
                        except:
                            return False
            Se importa en el archivo views.py las funciones creadas

        Otra alternativa para las metodos es a traves de los decoradores (funciones)
            se importan los decoradores a las views
                from rest_framework.decorators import api_view
            Y en el view se escribe
                @api_view(["GET"])
                Se llama a api_view y en la lista se escriben los metodos a usar
            Y se agrega la api view al import de las urls


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
                    path("path deseado/<argumentos>/", ModelAPIView.as_view(), name = "nombre")

            Dar de alta url en urls.py general
                agregar el paquete include a lo importado desde django.urls
                agregar url
                    path('path deseado/', include("app.urls")),



Extras: Personalizar "/admin"

Entramos al archivo models y dentro de la clase que define al modelo escribimos

    def __str__(self):
        return self.atributo que querramos mostrar en vez del default (Model Object X)
    
    class Meta:
    verbose_name = "Heroe"
    verbose_name_plural = "Heroes"

    Esto permite cambiar loa nombres

            

"""