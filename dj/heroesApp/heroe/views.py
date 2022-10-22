# Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Models Imports
from heroe.models import Hero

# Serializer import
from heroe.serializer import HeroSerializer

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