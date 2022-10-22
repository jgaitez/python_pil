# Rest Imports
from rest_framework.views import APIView

# Models Imports
from heroe.models import Hero

# Serializer import

# Create your views here.

class HeroApiView(APIView):

    def get(self, request):
        """Retorna un listado con todos los heroes almacenados en la base"""

    def post(self, request):
        """"""

class ModificarHeroeApiView(APIView):
    
    def put(self, request, id):
        """"""

class DeleteHeroeApiView(APIView):

    def delete(self, request, id):
        """"""
