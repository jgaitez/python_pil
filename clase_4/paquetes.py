# Formas de importar modulos o funciones (de terceros o propias)
# Importar todo el modulo
import autopep8
import funciones
import clase_3.bucles

# Importar todo el modulo y renombrandolo

import autopep8 as ap
from funciones import ordenador as orden

# Importar solo una función del paquete

from autopep8 import argparse
from clase_3.bucles import lista

# Para generar un listado de paquetes necesarios para el funcionamiento
# del codigo hay que hacer un "Requirement". Para eso, desde la consola
# y con el entorno activo:
# "pip freeze > requirements.txt"
# Eso genera un .txt con el nombre del paquete instalado y su versión.
# Con ese .txt se pueden instalar automaticamente todos los paquetes
# necesarios, tipeando desde la consola:
# "pip install -r .\requirements.txt "

#funciones.ordenador(lista, true)