import os
import random
import time


def limpiar():
    """Borra el contenido de consola
    """
    os.system("cls")


def espera(segundos):
    time.sleep(segundos)


def nombre_juego_entero():
    print("""
  ______    __                   __                   __            ______    _              __     __
 /_  __/   / /_   ___           / /_   ___    _____  / /_          / ____/   (_)   ____ _   / /_   / /_  ___    _____
  / /     / __ \ / _ \         / __ \ / _ \  / ___/ / __/         / /_      / /   / __ `/  / __ \ / __/ / _ \  / ___/
 / /     / / / //  __/        / /_/ //  __/ (__  ) / /_          / __/     / /   / /_/ /  / / / // /_  /  __/ / /
/_/     /_/ /_/ \___/        /_.___/ \___/ /____/  \__/         /_/       /_/    \__, /  /_/ /_/ \__/  \___/ /_/
                                                                                /____/""")


def bienvenida():
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
    texto = "Próxima ronda!"
    inicio = 0
    fin = 0

    for i in texto:
        letra = texto[inicio:fin]
        print(letra)
        time.sleep(0.15)
        fin += 1
        limpiar()
    print(texto)
    espera(0.5)
    limpiar()


class Personajes:
    def __init__(self):
        self.hp_max = random.randrange(60, 71)
        self.mp_max = random.randrange(30, 41)
        self.fuerza = random.randrange(3, 7)
        self.inteligencia = random.randrange(2, 5)
        self.hp = self.hp_max
        self.mp = self.mp_max
        self.habilidades = [BolaDeFuego(), GolpeLetal(), Golpear()]

    def __str__(self):
        return "Jugador: " + str(self.nombre) + " HP: " + str(self.hp) + "/" + str(self.hp_max) + "  MP: " + str(self.mp) + "/" + str(self.mp_max)

    def stats(self):
        print("HP:", self.hp, "/", self.hp_max)
        print("MP:", self.mp, "/", self.mp_max)
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        return ""

    def eleccion(self):
            print("\nElige una habilidad:\n")
            print("0 - Bola de fuego (10 MP)")
            print("1 - Golpe letal (5 MP)")
            print("2 - Golpe común (0 MP)")
            x = input("➟  ")
            return int(x)


class Jugador(Personajes):
    def __init__(self, nombre):
            self.nombre = nombre
            super().__init__()


class Ia(Personajes):
    nombre_ia = ["Adriel", "Agni", "Anmon", "Areu", "Axel", "Baco", "Bernal",
                 "Brais", "Caín", "Catriel", "Ciro", "Dante", "Drac", "Éber",
                 "Elián", "Elm", "Eros", "Esaú", "Farid", "Hans", "Inder",
                 "Ion", "Jaguar", "Jou", "Keanu"]

    def __init__(self):
        self.nombre = random.choice(Ia.nombre_ia)
        super().__init__()


class BolaDeFuego():
    def __init__(self):
        self.daño = 0
        self.nombre = "Bola de fuego"

    def devolverAtaque(self, origen):
        if origen.mp < 10:
            return "No tenes suficiente MP"
        else:
            self.daño = random.randrange(21, 26)+origen.inteligencia
            origen.mp += -10
            return self.daño


class GolpeLetal():
    def __init__(self):
        self.daño = 0
        self.nombre = "Golpe letal"

    def devolverAtaque(self, origen):
        if origen.mp < 5:
            return 0
        else:
            self.daño = random.randrange(12, 16)+origen.fuerza
            origen.mp += -5
            return self.daño


class Golpear():
    def __init__(self):
        self.daño = 0
        self.nombre = "Golpear"

    def devolverAtaque(self, origen):
        self.daño = origen.inteligencia+origen.fuerza
        return self.daño


def juego():
    bienvenida()
    nombre_humano = input("Cuál es tu nombre?\n➟  ")
    humano = Jugador(nombre_humano.capitalize())
    maquina = Ia()
    limpiar()
    print(f"Hola {humano.nombre}!, gracias por jugar a este juego! Te muestro tus estadisticas iniciales:")
    print(humano.stats())
    espera(1)
    print(f"Las estadísticas de tu oponente, {maquina.nombre}, son las siguientes:")
    print(maquina.stats())
    espera(1)
    print(f"Vamos a jugar {humano.nombre}!")
    espera(1)
    limpiar()

    ronda = 0
    while humano.hp > 0 and maquina.hp > 0:
        limpiar()
        ronda += 1
        nombre_juego_entero()
        print(f"Ronda N°: {ronda}")
        print("---------------")
        print(humano)
        print("---------------")
        print(maquina)
        print("---------------")
        print("\nTurno de", humano.nombre)
        elec1 = humano.eleccion()
        maquina.hp -= humano.habilidades[elec1].devolverAtaque(humano)
        print("Haz usado", humano.habilidades[elec1].nombre)
        print("Atacando...")
        print("Daño que causaste:", humano.habilidades[elec1].devolverAtaque(humano))
        if humano.hp <= 0 and maquina.hp <= 0:
            break

        print("\nTurno de", maquina.nombre)
        elec2 = random.randint(0, 2)
        humano.hp -= maquina.habilidades[elec2].devolverAtaque(maquina)
        print(maquina.nombre, "ha usado", maquina.habilidades[elec2].nombre)
        espera(1)
        print("Atacando...")
        espera(1)
        print("Daño que te causaron:", maquina.habilidades[elec2].devolverAtaque(maquina))
        espera(1)
        prox_ronda()
        if humano.hp <= 0 or maquina.hp <= 0:
            break
    if humano.hp > 0:
            print(f"No hizo falta una {ronda+1}° ronda! Ya ganaste {humano.nombre}!")
            print("--------------------")
            print("Gracias por jugarme!")
            print("--------------------")
            nombre_juego_entero()
    else:
        print(f"No hizo falta una {ronda+1}° ronda! {maquina.nombre} ya ganó!")
        print("--------------------")
        print("Gracias por jugarme!")
        print("--------------------")
        nombre_juego_entero()

juego()
