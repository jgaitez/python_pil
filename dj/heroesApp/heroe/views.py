# Rest Imports
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Models Imports
from heroe.models import Hero

# Serializer Imports
from heroe.serializer import HeroSerializer

# Helpers Imports
from heroe.helpers.heroeErrors import hayHeroe

# Create your views here.

class HeroApiView(APIView):

    def get(self, request):
        """Retorna un listado con todos los heroes almacenados en la base"""
    
        heroes = Hero.objects.all()
        heroes_serializer = HeroSerializer(heroes, many = True)

        return Response(
            data=heroes_serializer.data,
            status=status.HTTP_200_OK
        )
    
@api_view(["GET"])
def hero_api_view(request):
    heroes = Hero.objects.all()
    heroes_serializer = HeroSerializer(heroes, many = True)

    return Response(
        data=heroes_serializer.data,
        status=status.HTTP_200_OK
    )

class CrearHeroApiView(APIView):

    def post(self, request):
        """Crear un nuevo registro/heroe"""
        print("Segundo POST")
        serializer = HeroSerializer(data = request.data, many = True)

        if serializer.is_valid():
            serializer.save()
        
            data = {
                "message":"El heroe fue creado de forma correcta"
            }
            return Response(
                data=data,
                status = status.HTTP_201_CREATED
            )
    
        return Response(
        data = serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )


class HeroDetalleApiView(APIView):
    
    def get(self, request, pk):
        """Nos retorna mas info de un heroe en particular"""

        try:
            heroe = Hero.objects.get(pk=pk)

            heroe_serializer = HeroSerializer(heroe)

            return Response(
                data=heroe_serializer.data,
                status=status.HTTP_200_OK
            )
        except:        
            data = {
                "message":"El heroe no fue encontrado"
            }

            return Response(
                data=data,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk):
        """Nos modifica un heroe en particular"""

        heroe = hayHeroe(pk)
        if heroe[0]:

            heroe_serializer = HeroSerializer((heroe)[1], data=request.data)

            if heroe_serializer.is_valid():
                heroe_serializer.save()
            
                data = {
                    "message":"El heroe fue modificado de forma correcta"
                }

                return Response(
                    data=data,
                    status=status.HTTP_200_OK
                )
            
        return Response(
            data = heroe_serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )


    def delete(self, request, pk):
        """Elimina un heroe"""

        heroe = Hero.objects.get(pk=pk)
        heroe.delete()

        data = {
            "message":"El heroe fue eliminado de forma correcta"
        }

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )


@api_view(["GET", "PUT", "DELETE"])
def hero_detail_api_view(request, pk):

    try:
        heroe = Hero.objects.get(pk=pk) 
    
    except:
        return Response(
        {"Mensaje":"Heroe No Encontrado"},
        status=status.HTTP_400_BAD_REQUEST
        )
    
    # Detail
    if request.method == "GET":
    
        heroe_serializer = HeroSerializer(heroe)

        return Response(
            data=heroe_serializer.data,
            status=status.HTTP_200_OK
        )


    # Actualizar
    elif request.method == "PUT":

        heroe_serializer = HeroSerializer(heroe, data=request.data)

        if heroe_serializer.is_valid():
            heroe_serializer.save()
        
            data = {
                "message":"El heroe fue modificado de forma correcta"
            }

            return Response(
                data=data,
                status=status.HTTP_200_OK
            )
            
    
    # Borrar
    elif request.method == "DELETE":

        heroe.delete()

        data = {
            "message":"El heroe fue eliminado de forma correcta"
        }

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )