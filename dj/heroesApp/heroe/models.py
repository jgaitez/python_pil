from random import choices
from secrets import choice
from django.db import models

# Create your models here.
class Hero(models.Model):
    
    #Opciones
    UNIVERSE_CHOICE = (
        ("1", "Marvel"),
        ("2", "DC")
    )

    # Atributos
    name = models.CharField(
        max_length = 100,
        unique = True,
        verbose_name = "Nombre"
    )
    age = models.IntegerField(

    )

    universe = models.CharField(
        max_length = 1,
        choices = UNIVERSE_CHOICE,
        verbose_name = "Universo"
    )