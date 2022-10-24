from django.db import models

# Create your models here.

class Product(models.Model):
    
    # Opciones

    PRODUCTLINE_CHOICES = (
        ("1","Autos Clásicos"),
        ("2","Motocicletas"),
        ("3","Aviones"),
        ("4","Barcos"),
        ("5","Trenes"),
        ("6","Camiones y Colectivos"),
        ("7","Autos Antiguos")
    )


    #Atributos
    productCode = models.CharField(
        max_length = 8,
        verbose_name = "Id Producto"
    )

    productName = models.CharField(
        max_length = 70,
        verbose_name = "Nombre Producto"
        
    )

    productLine = models.CharField(
        max_length = 25,
        verbose_name = "Línea Producto"
    )

    choice_productLine = models.CharField(
        max_length = 1,
        choices = PRODUCTLINE_CHOICES,
        verbose_name = "Línea Elegida Producto"
    )

    productScale = models.CharField(
        max_length = 10,
        verbose_name = "Escala Producto"
    )

    productVendor = models.CharField(
        max_length = 30,
        verbose_name = "Proveedor Producto"
    )

    productDescription = models.CharField(
        max_length = 400,
        verbose_name = "Descripción Producto"
    )

    quantity = models.IntegerField(
        verbose_name = "Stock Producto"
    )
    
    buyPrice = models.DecimalField(
        verbose_name = "Precio de Compra Producto",
        decimal_places = 2,
        max_digits = 8
    )

    msrp = models.DecimalField(
        verbose_name = "Precio de Venta Sugerido Producto",
        decimal_places = 2,
        max_digits = 8
    )