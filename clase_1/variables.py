# Variables
# Los nombres de las variables tienen que ser autoexplicativos
# Tecnica: "nombre de variable" = lo que se quiera almacenar

mensaje_usuario = input("Ingrese un mensaje: ")
print(mensaje_usuario)

# Input siempre devuelve contenido de tipo string (cadena de caracteres).
# Como saber el  tipo de dato que recibe? Usando la función "type"
print(type(mensaje_usuario)) # Esto significa "Imprimir" el tipo de dato de la variable "mensaje_usuario"
# Python no necesita definir el tipo de dato que contiene la variable, sino
# que Python en base al dato define su tipo. Una situación practica donde esto
# genera problemas es al momento de realizar operaciones aritméticas.

x = input("Ingrese un número: ")
y = input("Ingrese otro número: ")

# Por mas que yo en x e y ingrese números, Python no los va a tratar como tales
# pues #8. Si yo los printeo unidos con un "+" los va a concatenar. Si yo necesito
# mostrar diversos tipos de datos, los tengo que unir con "," y no con "+" 

resultado = x + y
print("El resultado es -->: ", resultado)

# Para que Python trate a x e y como numeros, se debe aclarar que el dato que 
# se esta por agregar es de ese tipo (usando "int"):

x = int(input("Ingrese solamente un numero: "))
y = int(input("Ingrese solamente otro numero: "))
resultado2 = x*y

print("El tipo de dato de X es: ",type(x))
print("El tipo de dato de X es: ",type(y))
print("El resultado de multiplicar los dos valores ingresados es: ",resultado2)
print("El tipo de dato del resultado es: ",type(resultado2))

x = str(x) #Esto significa que a partir de ahora, "x" va a ser el contenido de
#           la "x" anterior pero en formato string (originamente en #27 fue 
#           int)

resultado3 = x * y
# Con la redefinicion de "x" en #36 al querer repetir la multiplicación de #29 
# lo que va a suceder es que python va a entender que al valor (string) "x" debe ser 
# repetido (int) "y" veces.

print("Luego de la redefinición de la variable, el resultado es: ",resultado3)
