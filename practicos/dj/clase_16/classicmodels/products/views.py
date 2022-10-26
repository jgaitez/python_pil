# Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Models imports
from products.models import Product

# Serializer imports
from products.serializer import ProductSerializer

# Create your views here.

class ProductApiView(APIView):
    
    def get(self, request):
        """Retorna el listado de productos almacenados"""

        

        products = Product.objects.all()
        products_serializer = ProductSerializer(products)
        print(products_serializer)

        data = {
            "Products" : "hola"
        }

        return Response(
            data = data, 
            status = status.HTTP_200_OK
            )