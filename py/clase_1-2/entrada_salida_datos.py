# Salida de Datos
# Función PRINT
# Parametros extras: sep, end

print(".-:Hola Mundo:-.\n")
print("Desde Visual")
print("Y con extensiones\nque te facilitan codear\n")

# comentario comentando comentarios

# Otras funciones del print
# Ops aritmeticas 
print(2+2)

# \n salto de linea
print("Acá estamos viendo \nun salto de línea")

# \t tabulacion
print("Y acá una \t tabulacion")

# concatenar (con el signo más)
# como en excel, la concatenación une todo lo que se especifique como valores
# lo que significa que si no se concatenan espacios, todos los valores van
# a quedar "pegados"
print("Valor 1"+"Valor 2")

# Para agregar espacios: se puede agregar un espacio al ultimo del primer valor
# o al inicio del siguiente. Tambien se puede usar "sep", en esta ocasión, los
# valores deben ir separados con coma. En MI CASO, sin usar "sep" los valores 
# se separan con un espacio por default.
print("Valor 1","Valor 2")

# Aca usando otro "separador" distinto de la coma para mostrar el uso de "sep"
print("Valor 1", "Valor 2", sep= "-")

# Función END
# la funcion print por default termina en un salto de linea para que la proxima
# función empiece en la línea inferior. Con "End", podemos modificar ese 
# comportamiento

print("Esto es una prueba para entender", end="\t")
print("Le entiendo o no?")

# Entrada de datos
# Funcion INPUT
input("Mensaje para avisar al usuario que el sistema esta a la espera de\nun ingreso de info: ")
# El mensaje tambien se puede escribir con la función print
# (sin "end" haría el salto de linea y el input se escribiría abajo y con el 
# "end" se podria escribir al lado de haber terminado el mensaje que se 
# imprimió). La otra opcion es como en la linea 49, escribir el msj dentro
# del input y finalizarlo con un espacio para que quede prolijo cuando se
# imprima.
