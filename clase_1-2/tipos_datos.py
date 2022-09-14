# String / str
a = 'Esto es una "cadena" y no nacional'
b = "Esto es otra cadena"

print("El valor a es:",a, type(a))
print("El valor b es:",b, type(b))

# Para convertir un dato a string:
c = str(120.80)
print(c, type(c))

# Para saber la longitud de una cadena: "len"

print("La longitud es de:",len(a),"caracteres")

print("----------------------------------------")

# Uso de indices: Permiten mostrar la posición de un elemento
# Super importante: en informática, el primer elemento SIEMPRE es 0
# y no 1. Si yo quiero mostrar el determinado elemento:
print('El primer elemento de "a" es:',a[0])
print('El cuarto elemento de "a" es:',a[3])

# Si yo quiero mostrar un rango:
print('El rango de "a" que voy a mostrar es',a[0:4]) # Esto se puede
# leer como imprimir desde la posicion cero hasta antes de la posición 4.

# Si yo quiero contar de derecha a izquierda:
print('El antepenultimo caracter de "a" es',a[-3])

print("----------------------------------------")

# Metodos de String
# Funciones que se pueden utilizar se acceden: "variable.metodo"
# Para mostrar todo en minuscula:
print("Minuscula:",a.lower())
# Para mostrar todo en mayuscula:
print("Mayuscula:",a.upper())
# Para separar la cadena y convertirla en una lista:
print("En lista:",a.split())
# Para saber la longitud de la cadena ("split" hace que la cadena
# ahora este compuesta por palabras y no sea una sola frase):
print(len(a.split()))

print("----------------------------------------")

# List
# Tipo de dato que permite almacenar dentro cualquier tipo de dato

lista_1 = ["Hola", 3, 2.3, False, [6,4,2,0],("a","b")]
print("La lista 1 contiene:",lista_1)
print("El tipo de dato de Lista 1 es:",type(lista_1))
print("El largo de Lista 1 es:",len(lista_1))
print("El tercer elemento de Lista 1 es:",lista_1[2])

# Tambien se pueden hacer variables con objetos de la lista:
var_uno = lista_1[3]
print(var_uno, type(var_uno))

# Tupla: es igual que una lista, pero sus valores son inmutables, solo 
# son los que se definen en un primer momento. En la listas esto es mucho
# mas flexible

# Metodos de lista
# Para agregar contenidos al ultimo de la lista:
lista_1.append("cosa agregada")
print(lista_1)

# Para averiguar la ubicacion de un valor de la lista:
print('El valor "6,4,2,0" esta en el indice:',lista_1.index([6,4,2,0]))

# Para agregar un contenido en un lugar especifico de la lista: insert(posicion, contenido)
lista_1.insert(0, "primero")
print(lista_1)

print("----------------------------------------")

# Diccionario
# Estructura de datos que permite manejarlos a traves de una "llave": "valor". La llave siempre
# tiene que ser string. El valor es indistinto

usuario = {
    "nombre":"Javier",
    "apellido":"Gaitez",
    "edad":"26",
    "hobbies": ["Conducir", "Andar en bicicleta", "Leer"],
    "mascotas": False
}
print("El diccionario Usuario esta compuesto por:",usuario)

#se puede mostrar el valor relacionado a una determinada llave/key 
print("La edad es:",usuario["edad"])

#se puede mostrar la cantidad de elementos del diccionario
print("La cantidad de elementos del diccionario es:", len(usuario))


# Metodos de diccionario
# Get: permite obtener el valor a traves de la llave
print("Los hobbies del usuario son:",usuario.get("hobbies"))

# Else: devuelve algo en caso de no encontrarse la key
print(usuario.get("Novia", "No encontrado"))

# Mostrar todas las llaves
print(usuario.keys())

# Transformar en lista las keys
keys_usuario = list(usuario.keys())
print(type(keys_usuario))
print(usuario.get(keys_usuario[0])) #Imprimir: de lo que se obtiene del diccionario usuario (#82),
# lo que este en la posicion 0 de la variable keys_usuario definida en #109

# Mostrar todas las valores
print(usuario.values())

# Transformar en lista los valores
valores_usuario = list(usuario.values())
