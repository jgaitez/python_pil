# Rest Imports
from rest_framework import serializers

# Models imports
from products.models import Product

# Serializer
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
