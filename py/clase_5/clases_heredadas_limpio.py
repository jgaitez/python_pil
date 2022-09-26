class Vehiculos:
   
    desplazamiento = "a combustión"
    def __init__(self, ruedas, personas, carga, nombre):
        # Atributos de función obligatorios
        self.ruedas = ruedas
        self.personas = personas
        self.carga = carga
        self.nombre = nombre
        # Igualo los parametros

    def capacidad_de_carga(self):
        print(f"El {self.nombre} lleva {self.carga} carga.")
    
    def capacidad_de_transporte(self):
        print(f"El {self.nombre} lleva {self.personas} personas.")

    def nombre_vehiculo(self):
        print("El vehiculo se llama", self.nombre+".")


vehiculo_1 = Vehiculos(4,5,"poca","auto")
print(f"{vehiculo_1.nombre} es {Vehiculos.desplazamiento}, lleva {vehiculo_1.personas} personas, tiene espacio para {vehiculo_1.carga} carga y se mueve sobre {vehiculo_1.ruedas} ruedas.")

vehiculo_2 = Vehiculos(4,2,"mucha","coupe")
print(f"{vehiculo_2.nombre} es {Vehiculos.desplazamiento}, lleva {vehiculo_2.personas} personas, tiene espacio para {vehiculo_2.carga} carga y se mueve sobre {vehiculo_2.ruedas} ruedas.")

vehiculo_1.capacidad_de_carga()
vehiculo_2.nombre_vehiculo()
vehiculo_1.capacidad_de_transporte()

class Automovil(Vehiculos):

    def __init__(self):
        # Clase sin parametros obligatorios
        self.marca = ""
        self.tipo = ""
        self.modelo = ""
        self.uso = ""
        # Contiene cuatro atributos (sin definir)


auto_1 = Automovil()
auto_1.marca = "Renault"
auto_1.modelo = "Fluence"
auto_1.tipo = "Sedán"
auto_1.uso = "Particular"
print(auto_1.uso)

class Motocicleta(Vehiculos):

    def __init__(self, marca, tipo, modelo, cilindrada):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.cilindrada = cilindrada
        super().__init__(2,2,"poca","moto")

        # Clase padre: Vehiculos
        # Clase hija: Motocicleta
        # Para hacer la herencia:
            # Al definir la clase hace falta poner entre parentesis la clase superior
            # En los atributos hace falta agregar el "super().__init__() y en los 
            # segundos parentesís especificar, si corresponde, los atributos de la
            # funcion padre

    def potencia(self):
        print(f"La cilindrada de la {self.marca} {self.tipo} es de {self.cilindrada} CC. Por eso su {self.carga} carga.")

    def muestra_marca(self):
        print("La marca de la moto es", self.marca)

moto_1 = Motocicleta("Yamaha", "De calle", "XX100", 600,)

print(moto_1.cilindrada)
moto_1.potencia()
moto_1.muestra_marca()
moto_1.nombre_vehiculo()