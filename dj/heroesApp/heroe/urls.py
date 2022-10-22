# Django import
from django.urls import path

# Views import
from heroe.views import HeroApiView

# Urls
urlpatterns = [
    path("heroe-list/", HeroApiView.as_view(), name="heroe-list"),
]
