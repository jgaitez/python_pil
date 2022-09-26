# Importo funciones de python:
import os
# Para limpiar consola
import random
# Para que el codigo determine la intensidad de los golpes y en la IA
# pueda autoseleccionar un golpe
import time
# Para incluir demoras en la visualización del codigo

def limpiar():
    """Borra el contenido de consola
    """
    os.system("cls")


def espera(segundos):
    """Demora la ejecución del codigo X cantidad de segundos

    Args:
        segundos (int / float): cantidad de segundos de espera
    """
    time.sleep(segundos)


def nombre_juego_entero():
    """Imprime el nombre completo del juego en formato ASCII
    """
    print("""
  ______    __                   __                   __            ______    _              __     __
 /_  __/   / /_   ___           / /_   ___    _____  / /_          / ____/   (_)   ____ _   / /_   / /_  ___    _____
  / /     / __ \ / _ \         / __ \ / _ \  / ___/ / __/         / /_      / /   / __ `/  / __ \ / __/ / _ \  / ___/
 / /     / / / //  __/        / /_/ //  __/ (__  ) / /_          / __/     / /   / /_/ /  / / / // /_  /  __/ / /
/_/     /_/ /_/ \___/        /_.___/ \___/ /____/  \__/         /_/       /_/    \__, /  /_/ /_/ \__/  \___/ /_/
                                                                                /____/""")


def bienvenida():
    """Imprime la bienvenida, el nombre del juego, la versión y una 
    miscelanéa. Los primeros dos se encuentran en formato ASCII y 
    se imprimen por linea 0.1 segundos uno despues del otro.
    """
    print("                           _     ___      _                                        _        __           __")
    espera(0.1)
    print("                          (_)   / __)    (_)  ___    ____  _   __  ___    ____    (_)  ____/ /  ____    / /")
    espera(0.1)
    print("                         / /   / __ |   / /  / _ \  / __ \| | / / / _ \  / __ \  / /  / __  /  / __ \  / / ")
    espera(0.1)
    print("                        / /   / /_/ /  / /  /  __/ / / / /| |/ / /  __/ / / / / / /  / /_/ /  / /_/ / /_/  ")
    espera(0.1)
    print("                       /_/   /_____/  /_/   \___/ /_/ /_/ |___/  \___/ /_/ /_/ /_/   \__,_/   \____/ (_)   \n")
    espera(0.1)
    print("                                                            ___ ")
    espera(0.1)
    print("                                                           /   |")
    espera(0.1)
    print("                                                          / /| |")
    espera(0.1)
    print("                                                         / ___ |")
    espera(0.1)
    print("                                                        /_/  |_|\n")
    espera(0.1)
    print("   ______  __                   __                   __            ______    _              __     __               ")
    espera(0.1)
    print("  /_  __/ / /_   ___           / /_   ___    _____  / /_          / ____/   (_)   ____ _   / /_   / /_  ___    _____")
    espera(0.1)
    print("   / /   / __ \ / _ \         / __ \ / _ \  / ___/ / __/         / /_      / /   / __ `/  / __ \ / __/ / _ \  / ___/")
    espera(0.1)
    print("  / /   / / / //  __/        / /_/ //  __/ (__  ) / /_          / __/     / /   / /_/ /  / / / // /_  /  __/ / /    ")
    espera(0.1)
    print(" /_/   /_/ /_/ \___/        /_.___/ \___/ /____/  \__/         /_/       /_/    \__, /  /_/ /_/ \__/  \___/ /_/     ")
    espera(0.1)
    print("                                                                               /____/\n")
    espera(0.1)
    print("                                         Versión 0.3 ~ Tributo a Guido van Rossum")
    espera(0.1)
    print("                                   ᴍᴇɪɴᴇ ᴀᴜꜰʀɪᴄʜᴛɪɢᴇ ᴇɴᴛsᴄʜᴜʟᴅɪɢᴜɴɢ, ʜᴇʀʀ ɢᴜɪᴅᴏ ᴠᴀɴ ʀᴏssᴜᴍ\n\n\n")


def prox_ronda():
    """Printea el texto "Próxima ronda" de manera particular

    Args:
        texto (str): Texto a printear de manera especial
        inicio (int): Inicio del rango a imprimir de la cadena
        fin (int): Fin del rango a imprimir de la cadena\n
        inicio y fin no deben ser modificados
    """
    texto = "Próxima ronda!"
    inicio = 0
    fin = 0

    for i in texto:
    # Bucle para simular que la palabra se va imprimiendo secuencialmente
        letra = texto[inicio:fin]
        print(letra)
        time.sleep(0.15)
        fin += 1
        limpiar()
    print(texto)
    espera(0.5)
    limpiar()


class Personajes:
    """Clase genérica para los jugadores sin importar si son humanos o no.
    """
    def __init__(self):
        """Inicializador de la clase, sin atributos obligatorios
           Atributos definidos: Vida, Maná, Fuerza, Inteligencia
           y 3 habilidades
        """
        self.hp_max = random.randrange(60, 71)
        self.mp_max = random.randrange(30, 41)
        self.fuerza = random.randrange(3, 7)
        self.inteligencia = random.randrange(2, 5)
        self.hp = self.hp_max
        self.mp = self.mp_max
        self.habilidades = [BolaDeFuego(), GolpeLetal(), Golpear()]

    def __str__(self):
        """
        Returns: Muestra vida y maná actual y vida y mana máxima
        """
        return "Jugador: " + str(self.nombre) + " HP: " + str(self.hp) + "/" + str(self.hp_max) + "  MP: " + str(self.mp) + "/" + str(self.mp_max)

    def stats(self):
        """Muestra las estadísticas iniciales de los jugadores

        Returns: str vacía
        """
        print("HP:", self.hp)
        print("MP:", self.mp)
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        return ""

    def eleccion(self):
        """Muestra los ataques a elegir

        Returns: int: Opción elegida
        """
        print("\nElige una habilidad:\n")
        print("0 - Bola de fuego (10 MP)")
        print("1 - Golpe letal (5 MP)")
        print("2 - Golpe común (0 MP)")
        x = input("➟  ")
        return int(x)


class Jugador(Personajes):
    """Clase hija de Personajes, para los jugadores humanos
    """
    def __init__(self, nombre):
        """Inicializo clase con atributos propios y uno obligatorio
        Args:
            nombre (str): Nombre del jugador humano
        """
        self.nombre = nombre
        super().__init__()


class Ia(Personajes):
    """Clase hija de Personajes, para la IA
    """
    nombre_ia = ["Adriel", "Agni", "Anmon", "Areu", "Axel", "Baco", "Bernal",
                 "Brais", "Caín", "Catriel", "Ciro", "Dante", "Drac", "Éber",
                 "Elián", "Elm", "Eros", "Esaú", "Farid", "Hans", "Inder",
                 "Ion", "Jaguar", "Jou", "Keanu"]
    # Lista de nombres de los posibles competidores
    

    def __init__(self):
        """Inicializador de la clase, sin atributos obligatorios
           Atributos definidos: Nombre en base a una elección aleatoria
           de la lista "nombre_ia"
        """
        self.nombre = random.choice(Ia.nombre_ia)
        super().__init__()


class BolaDeFuego():
    """Clase de ataque
    """
    def __init__(self):
        """Inicializador de la clase, sin atributos obligatorios
           Atributos definidos: Daño y nombre del arma
        """
        self.daño = 0
        self.nombre = "Bola de fuego"

    def atacar(self, atacante):
        """Realiza el ataque con la Bola de Fuego.

        Args:
            atacante (str): Primero controla si el atacante tiene maná
            suficiente. Si no lo tiene, devuelve mensaje de no generación 
            de daño. Caso contrario calcula el daño sumandole a un numero
            aleatorio entre 21 y 26 y la inteligencia del atacante.

        Returns:
            str: Error de no generación de daño
            int: Daño causado
        """
        if atacante.mp < 10:
            return "No hay suficiente MP. No se realizó daño alguno"
        else:
            self.daño = random.randrange(21, 26)+atacante.inteligencia
            atacante.mp += -10
            return self.daño


class GolpeLetal():
    """Clase de ataque
    """
    def __init__(self):
        """Inicializador de la clase, sin atributos obligatorios
           Atributos definidos: Daño y nombre del arma
        """
        self.daño = 0
        self.nombre = "Golpe letal"

    def atacar(self, atacante):
        """Realiza el ataque golpe letal.

        Args:
            atacante (str): Primero controla si el atacante tiene maná
            suficiente. Si no lo tiene, devuelve mensaje de no generación 
            de daño. Caso contrario calcula el daño sumandole a un numero
            aleatorio entre 12 y 16 y la inteligencia del atacante.

        Returns:
            str: Error de no generación de daño
            int: Daño causado
        """
        if atacante.mp < 5:
            return "No hay suficiente MP. No se realizó daño alguno"
        else:
            self.daño = random.randrange(12, 16)+atacante.fuerza
            atacante.mp += -5
        return self.daño


class Golpear():
    """Clase de ataque
    """
    def __init__(self):
        """Inicializador de la clase, sin atributos obligatorios
           Atributos definidos: Daño y nombre del arma
        """
        self.daño = 0
        self.nombre = "Golpear"

    def atacar(self, atacante):
        """Realiza el ataque golpe común. No necesita de maná por lo
        que no es necesario controlar si el atacante tiene o no. 
        Siempre causa daño.

        Args:
            atacante (str): Calcula el daño sumando la inteligencia
            y la fuerza del atacante.

        Returns:
            int: Daño causado
        """
        self.daño = atacante.inteligencia+atacante.fuerza
        return self.daño


def juego():
    """Desarrollo del juego
    """
    bienvenida()
    # Solicita nombre usuario
    nombre_humano = input("Cuál es tu nombre?\n➟  ")
    # Crea el objeto humano, el cual va a ser de la clase Jugador.
    # Su atributo nombre sera lo introducido en el paso anterior
    # con mayúscula inicial
    humano = Jugador(nombre_humano.capitalize())
    # Crea el objeto maquina, el cual va a ser de la clase Ia
    maquina = Ia()
    # Limpia la consola
    limpiar()
    # Da la bienvenida
    print(f"Hola {humano.nombre}!, gracias por jugar a este juego! Te muestro tus estadisticas iniciales:")
    # Muestra las estadisticas del jugador humano
    print(humano.stats())
    # Espera 1 segundo
    espera(1)
    # Muestra las estadisticas del jugador ia
    print(f"Las estadísticas de tu oponente, {maquina.nombre}, son las siguientes:")
    print(maquina.stats())
    espera(1)
    print(f"Vamos a jugar {humano.nombre}!")
    espera(1)
    limpiar()
    # Define valor de ronda para despues mostrarlo
    ronda = 0
    # Mientras la vida de humano y maquina sean mayor a cero
    while humano.hp > 0 and maquina.hp > 0:
        # Empezar limpiando la consola
        limpiar()
        # Sumarle 1 al valor de ronda
        ronda += 1
        # Mostrar el nombre del juego
        nombre_juego_entero()
        # Imprimir el número de ronda
        print(f"Ronda N°: {ronda}")
        print("---------------")
        # Imprimir valores estadisticos actuales/totales de los jugadores
        print(humano)
        print("---------------")
        print(maquina)
        print("---------------")
        print("\nTurno de", humano.nombre.upper)
        # Hace que el jugador elija un ataque
        elec1 = humano.eleccion()
        # Descuenta a la vida de IA el daño del ataque elegido
        maquina.hp -= humano.habilidades[elec1].atacar(humano)
        # Muestra el ataque usado
        print("Haz usado", humano.habilidades[elec1].nombre)
        print("Atacando...")
        # Muestra el daño causado
        print("Daño que causaste:", humano.habilidades[elec1].atacar(humano))
        if humano.hp <= 0 and maquina.hp <= 0:
            break

        print("\nTurno de", maquina.nombre.upper)
        # Hace que la IA eliga un ataque
        elec2 = random.randint(0, 2)
        # Descuenta a la vida del humano el daño del ataque elegido
        humano.hp -= maquina.habilidades[elec2].atacar(maquina)
        # Muestra el ataque usado
        print(maquina.nombre, "ha usado", maquina.habilidades[elec2].nombre)
        espera(1)
        print("Atacando...")
        espera(1)
        # Muestra el daño causado al humano
        print("Daño que te causaron:", maquina.habilidades[elec2].atacar(maquina))
        # Espera cinco segundos
        espera(5)
        prox_ronda()
        # Si la vida de los jugadores es mayor a 0, repite
        if humano.hp <= 0 or maquina.hp <= 0:
            break
    # Si las vidas de humano y maquina dejan de ser mayores a cero y
    # solo la vida de humano es mayor a cero
    if humano.hp > 0:
            # Declara ganador a humano y dice en cuantas rondas ganó
            print(f"No hizo falta una {ronda+1}° ronda! Ya ganaste {humano.nombre}!")
            # Procede a despedirse
            print("--------------------")
            print("Gracias por jugarme!")
            print("--------------------")
            nombre_juego_entero()
    else:
        # Declara ganador a la IA y dice en cuantas rondas ganó
        print(f"No hizo falta una {ronda+1}° ronda! {maquina.nombre} ya ganó!")
        # Procede a despedirse
        print("--------------------")
        print("Gracias por jugarme!")
        print("--------------------")
        nombre_juego_entero()

# Ejecuto el juego
juego()
