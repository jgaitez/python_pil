# Funcion Base
    # Una funcion es un bloque de codigo que nosotros podemos usar
    # llamandola todas las veces que necesitemos
    # Funciones "predeterminadas": "print", "len", "type", etc.
    # Funciones "personalizadas":
    # Estructura:
        # Nombre (unico y en lo posible autodescriptivo)
        # Argumentos
        # Codigo
        # Retorno

def sumar(a, b):  # a y b son los parametros
    resultado = a + b  # Defino la variable resultado como la suma de a y b
    return resultado  # Retorno resultado

# Como la uso?

# Opcion 1:
resultado_suma = sumar(2, 3)
print(resultado_suma)

print("Fin Op 1")

# Opcion 2:
print(sumar(2, 3))

print("Fin Op 2")

# Funcion 3: (sin parametros)

def resta():
    resultado = 2 - 3

    return resultado

print(resta())

print("Fin Op 3")

# Funcion 4: (sin retorno)
def saludo_old(nombre):
   
    print("Hola",nombre)

saludo_old("Javier")

print("Fin Op 4")

# Funcion 5: 
def saludo_a_vos():
    
    name = input("Nombre: ")
    print ("Hola!", name)
    return name

print(saludo_a_vos())

print("Fin Op 5")

# Funcion 6: 
def saludo_a_alguien(name):
    
     print ("Hola!", name)
     return name
name = input("Ingrese su nombre")
print(saludo_a_alguien(name))

print("Fin Op 6")

def saludo(cantidad_saludos): 
    # Defino funcion "saludo". Determino que un parametro sea la 
    # cantidad de saludos
   
    lista_nombres = [] 
    # Creo una lista
    for i in range(cantidad_saludos): 
        # Esto se va a repetir la cantidad de veces que sea la cantidad 
        # de saludos
        nombre = input("Ingrese su nombre: ")
        # Primero me va a pedir un nombre
        print("Hola",nombre)
        # Luego me va a saludar

        lista_nombres.append(nombre)
        # Y por ultimo va a agregar ese nombre a la lista creada.
    
    print(lista_nombres)
    return lista_nombres

saludo(int(input("Ingrese la cantidad de saludos: "))) 
# Aca llamo a la función "saludo". Para darle la cantidad de saludos, 
# hago que el usuario los agregue con el "input".

# Tipos de argumentos:
# Posicionales:
    # En el orden que yo defina los argumentos es el orden en el 
    # que se los tengo que pasar

def prueba(a, b, c):
    print(a, b, c)

prueba(420,3,5)

def prueba(a, b, c):
    # Funcion "prueba", necesita 3 parametros "a, b, c"
    print(a, b, c)
    # Para imprimirlos luego

# Defino los valores en variables
a = 420
b = 3
c = 5

prueba(b,b,b)
# Invoco a la función y le doy los 3 parametros. En el ej. le doy 3
# veces el mismo parametros para ver. 
# Como los argumentos son posicionales, el primer valor que ingrese
# va a ser el parametro "a" por mas que el valor sea el de la variable
# "b".
# Para evitar esta situacion se los puede nombrar

prueba(b = b, c = c, a = a)
# Arg b = var b - arg c = var c - arg a = var a

prueba(a = b, b = c, c = a)
# Arg a = var b - arg b = var c - arg c = var a

# De esta forma no importa el orden en que los enuncie.



def ordenador(lista, sentido):
    # La funcion de una funcion puede explicarse con comentarios o 
    # docstring. La ventaja de este último es que se integra en la
    # interfaz del programa que estemos usando
    """Esta función nos permite ordenar listas en base a un sentido 
    determinado

    Args:
        lista (list): Lista genérica
        sentido (bool): Define si la lista se ordena de mayor a 
        menor o viceversa
    Returns:
        list: Lista ordenada
    """
    lista.sort(reverse = sentido)
   # Sort ordena la lista. "reverse" le indica el sentido del orden
    return lista

nombres = saludo(int(input("Ingrese la cantidad de saludos: "))) 
print(
    ordenador(nombres, False)
    # Invoco a la funcion "ordenador" para que la lista a ordenar sea
    # la de "nombres". True para que reverse sea el sentido (a la inversa)
)