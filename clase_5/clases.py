# Objetos
# Entidades que se pueden reutilizar y atribuirles algunas funcionalidades
# y peculiaridades (Modelar)
    # Clases:
    # Plantilla / template que define o modela los objetos.


# Creacion de Clase Padre

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    def onomatopeya(self,sonido):
        # El self significa que los atributos son de la misma clase
        print(sonido)



# Definición y creación de la clase
class Perro(Animal):
    # Estructura: Clase(Clase de donde Hereda)
    # Atributos de clase (Iguales a una funcion global)
    # Constructor: Permite crear la instancia y atribuirle parametros al objeto

    def __init__(self, nombre, raza):
        # Parametro self: "A mi mismo". Significa que el objeto se va a
        # autoreferenciar
        # Atributos de instancia (Iguales a una funcion local)
        self.nombre = nombre
        # La funcion tiene un atributo "nombre" que es igual al parametro "nombre"
        self.raza = raza
        # Estos atributos de instancia son obligatorios para el uso de la funcion
        # Por lo tanto, "nombre" y "raza" deben ser escritos al momento de crear
        # un nuevo objeto (como en "perro_1" y "perro_2")
    
    # Metodos de la clase Perro
    def jugar(self, objeto):
        # La funcion jugar necesita además el objeto con el que esta jugando
        print("El perro esta jugando con",objeto)
    
    def saludar(self):
        print(f"{self.nombre} dio la pata")
    
    # Metodos
    # Acciones que le vamos a definir a nuestro objeto. Lo que es capaz de hacer
    # Pass sirve para que el interprete ignore esta parte del codigo

# Inicializacion del objeto
perro_1 = Perro("Beto", "Callejero")

print(perro_1)
# Esto imprime "<__main__.Perro object at 0x000001EA2253B670>" que es la 
# direccion de la memoria en donde esta guardada la información.

print(perro_1.raza)
# Aca pido una impresion de un atributo de la clase

# Llamando funciones y viendo que pueden hacer:
# Estructura: funcion.atributo(parametro)
perro_1.jugar("Pelota")
perro_1.saludar()

# Inicializacion de otro objeto independiente
perro_2 = Perro("Congo", "Callejero")
perro_2.especie = "Canino"

# Yo puedo crear los objetos que sean necesarios, pero partiendo de la
# informacion que pide la clase

# Agregando atributos de clase y usando f-string
print(f"Perro_2 -> {perro_2.nombre}, {perro_2.raza}, {perro_2.especie}")
perro_2.saludar()

class Gato:
    def __init__(self):
        self.nombre = ""
        self.raza = ""
        self.especie = ""
    # En esta clase, yo tambien defino que tiene 2 atributos como en "Perro",
    # sin embargo los instancio vacíos, para que cada objeto los defina
    # oportunamente

gato_1 = Gato()
print("El gato",gato_1.nombre+", es de raza", gato_1.raza+".")
# Al no tener los atributos definidos, el print solo va a mostrar un espacio vacío

gato_2 = Gato()
gato_2.nombre = "Michifus"
# Atributo nombre
gato_2.raza = "Egipcio"
# Atributo raza
gato_2.especie = "Felino"
gato_2.patas = "cuatro patas"
# Variable patas (No esta presente en el init de la clase "Gato")

print(f"El gato {gato_2.nombre}, es un {gato_2.especie} de raza {gato_2.raza}, con {gato_2.patas}.")