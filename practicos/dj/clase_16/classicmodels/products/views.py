# Rest Imports
from rest_framework.views import APIView

# Models imports
from products.models import Product

# Serializer imports


# Create your views here.

class ProductApiView(APIView):
    
    def get(self, request):
        """Retorna el listado de productos almacenados

        Args:
            request (_type_): _description_
        """