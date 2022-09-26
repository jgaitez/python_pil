# Bucles
# Permiten hacer que una porción de codigo se repita
# Los principales son: "for" y "while"
# For necesita que le especifiquemos las veces a ejecutar o hasta que
# se cumpla una condicion

# Ejemplo 1

for i in "Python":
    # "Repetir (iterar) i en una cadena de texto"
    print(i)
# Imprimir cada uno de los caracteres de la cadena
print("------Fin del Ejemplo 1------")

# Ejemplo 2

lista = [1, 2, 3, 4, "Hola", "Chau", True, False]

for i in lista:
    # "Repetir i en una lista"
    print(i, type(i))
# Imprimir cada uno de los caracteres de la cadena y su tipo
print("------Fin del Ejemplo 2------")

# Ejemplo 3

for i in range(10):
    # "Repetir i en un rango del 0 al 10 (no es necesario especificar el inicio si este es 0)"
    # En los rangos, el último numero no se agrega (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(i)
# Imprimir cada uno de los caracteres del rango
print("------Fin del Ejemplo 3------")

# Ejemplo 4
# Range: primer parametro: inicio del rango (si no esta, es 0), segundo parametro: final del
# rango, tercer parametro: step (el salto que da). Si se usa este ultimo, tiene que estar el
# primer paramentro.

for i in range(0, 10, 2):
    print(i)

print("------Fin del Ejemplo 4------")

# Ejemplo 5

lista = []
# creamos una variable "lista" vacía

for i in range(10):
# Repetir i en un rango del 0 al 10 (tambien puede ser un string)
    lista.append(i)
# Agregar a la lista vacía creada en #48 los valores del rango (o del string)
print(lista)
# Imprimir lista con los valores actualizados

print("------Fin del Ejemplo 5------")

# Ejemplo 6
# Se solicita crear un programa que almacene 10 valores ingresados por el usuario

lista = []
for i in range(3) :
# Esto se va a repetir 3 veces
    numero_usuario = int(input("Ingrese un número: "))
# Defino una variable que se forma de convertir a enteros lo que yo escribo
    lista.append(numero_usuario)
# Hago que los numeros agregados en #65, se guarden en la lista

print(lista)
# Imprimo la lista

print("------Fin del Ejemplo 6------")

# Ejemplo 6 bis
# Requerimiento igual a ejemplo 6, pero mostrando una linea de codigo alternativa

lista = []
for i in range(3) :
# Esto se va a repetir 3 veces
    lista.append(int(input("Ingrese un número: ")))
# Quiero que en la lista vacía de #79 se agreguen los valores que voy a introducir
# convertidos a entero

print(lista)
# Imprimo la lista

print("------Fin del Ejemplo 6 bis------")

# Ejemplo 6 ter
# Igual requerimiento que el Ejemplo 6, pero sin formatear el input como entero

lista = []
for i in range(3) :
# Esto se va a repetir 3 veces

    # Ingreso de datos
    dato_ingreso = input("Ingrese un número: ")
    # Defino una variable que almacena lo que yo escribo

    # Validación de datos
    if dato_ingreso.isnumeric() :
    # Chequea si el dato ingresado anteriormente es un numero. Devuelve true o false
        lista.append(int(dato_ingreso))
        # Si el dato ingresado es un numero, lo agrega convertido en entero a la lista
    else:
        print("El dato ingresado no es un número")
        # Si el dato ingresado no es un numero, imprime mensaje de error
        break
        # Break sirve para romper la ejecución y terminar el código.

print(lista)
# Imprimo la lista

print("------Fin del Ejemplo 6 ter------")

# Todo lo que este entre """ se va a "comentar" y no ejecutar

# While ejecuta el codigo sin restriccion de veces y hasta que yo lo
# detenga o se cumpla una condicion

# Ejemplo 7

x = 10

while x > 0:
# Lo que se ponga a continuacion hacerlo hasta x deje de ser mayor a 0
    print(x)
# Si el codigo terminara aca, provocaria un loop, ya que no hay nada que
# reduzca el valor de x. Para terminar manualmente la ejecución del codigo
# hay que presionar ctrl + c.
    x = x - 1
# Alternativa rapida: 
# x -= 1
# Redefino la variable para que su valor nuevo, sea el anterior menos 1.


print("Fin del código")
