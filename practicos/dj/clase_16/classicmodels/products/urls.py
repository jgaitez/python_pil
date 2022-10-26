#Django Imports

from django.urls import path

#Views Imports
from products.views import ProductApiView

urlpatterns = [
    path('products-list/', ProductApiView.as_view(), name= "products_list"),
]
