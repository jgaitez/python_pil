# CONDICIONALES EN PYTHON

# Los lenguajes leen secuencialmente las lineas de codigo

from codecs import oem_decode
from tkinter import E


a = 1
b = 2
c = 10

# Condicional IF (si) y ELSE (sino)
# Clasico con 2 valores
# Ejemplo 1

if a < b:
    print("A es menor a B")
else:
    print("A no es menor a B")
print("------Fin del Ejemplo 1------")

# Con 3 o mas valores
# Ejemplo 2

if a > b:
    print("A es mayor a B")

    if a > c:
        print("A es mayor que C y por lo tanto C es mayor que B")

    else:
        print("A no es mayor que C y por lo tanto C es mayor que todos")

else:
    print("A no es mayor a B")
print("------Fin del Ejemplo 2------")

# Ejemplo 3
# Un solo igual --> define variable
# Dos iguales --> compara
# =! significa desigual

a = 3
b = 2
c = 10

if a == 3:
    print("A es igual a 3 en int")

if a == "3":
    print("A es igual a 3 en string")
else:
    print("A no es igual a 3 en string")

print("------Fin del Ejemplo 3------")

# If con varias condiciones
# Se usa "and" para que todas las condiciones se tengan que cumplir
# para que el codigo se ejecute
# Ejemplo 4

edad_javier = 26
edad_diana = 20

if edad_javier >= 16 and edad_javier > 18:
    print("Javier puede votar y ademas es mayor de edad")
else:
    print("Alguna condición no se cumple")

print("------Fin del Ejemplo 4------")

# Se usa "OR" para comprobar que solo alguna de las condiciones se cumpla
# Ejemplo 5

if edad_diana >= 18 or edad_diana > 21 :
    print("Diana puede formar parte de la CD de la Biblio")

print("------Fin del Ejemplo 5------")

# Elif
# Permite comprobar diferentes condicionales en el mismo bucle (equivale a "resumir")
# comprobaciones sin tener que escribirlas con el if y con el else
# Ejemplo 6

if edad_diana == 18 :
    print("Diana tiene 18 años")
elif edad_diana == 19 :
    print("Diana tiene 19 años")
elif edad_diana == 20 :
    print("Diana tiene 20 años")

print("------Fin del Ejemplo 6------")
print("Fin del código")
