# Django import
from django.urls import path

# Views import
from heroe.views import (
    HeroApiView,
    CrearHeroApiView,
    HeroDetalleApiView,
    hero_api_view
    )

# Urls
urlpatterns = [
    path("heroe-list/", HeroApiView.as_view(), name="heroe-list"),
    path("create-heroe/", CrearHeroApiView.as_view(), name="Create"),
    path("detalle-heroe/<int:pk>/", HeroDetalleApiView.as_view(), name="Detalle"),
]
