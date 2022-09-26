# Idear un programa que solicite al usuario dos números enteros y el programa
# deberá retornar aquellos números pares que se encuentren dentro del rango
# formado entre los números ingresados.

primero = int(input("Por favor ingrese el primer numero: "))
segundo = int(input("Por favor ingrese el segundo numero: "))

if segundo - primero == 1 :
    print("Por favor, especifique 2 valores cuya diferencia sea mayor a 1")
elif segundo - primero == 0 :
    print("Por favor, especifique 2 valores distintos")
else:
    if primero > segundo :
        print("El primer número debe ser menor al segundo")
    else:
        for i in range(primero,(segundo+1)) :
            if not i%2 :
                print(i)
# OK