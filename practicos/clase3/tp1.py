# Realizar un menú de un cajero automático, donde el usuario pueda escoger entre
# alguna de las siguientes opciones:
# Deposito.
# Extracción.
# Transferencia.
# Salir.
# En todos los casos se le pedirá al usuario ingresar un monto de dinero y el
# programa deberá mostrar en todo momento la sección del menú en la que se
# encuentre, pudiendo retornar al menú principal siempre que se quiera y solo se
# detendrá la ejecución cuando se ingrese la opción de “salir” en el menú principal.


opcion = "x"

while opcion == "x" :
    print("=================================================================")
    print("+++++++++++++++++++  ATM - Cajero Automático  +++++++++++++++++++")
    print("=================================================================")
    print("Elija la operación a realizar tipeando la letra entre parentesís:")
    print("-----------------------------------------------------------------\n")
    print("(D)eposito\t(E)xtracción\t(T)ransferencia\t\t(S)alir\n")
    opcion = input("Opción a elegir: ")
    if opcion == "d" :
        print("=================================================================")
        print("++++++++++++++++++++++++++++  DEPÓSITOS  ++++++++++++++++++++++++")
        print("=================================================================")
        monto_depo = input("Ingrese el monto a depositar: $")
        if monto_depo.isnumeric() :
            print("=================================================================")
            print("++++++++++++++++++++++++++++  DEPÓSITOS  ++++++++++++++++++++++++")
            print("=================================================================")
            print("Su depósito de $"+monto_depo+" ha sido confirmado.")
            print("Ahora volverá al menú principal")
        else:
            print("No ha ingresado un número válido")
            print("Ahora volverá al menú principal")
    elif opcion == "e" :
        print("Bienvenido a la sección de extracciones")
        monto_extra = input("Ingrese el monto a extraer: $")
        print("Su extracción de $"+monto_extra+" ha sido confirmada.")
        print("Ahora volverá al menú principal")
    elif opcion == "t" :
        print("Bienvenido a la sección de transferencias")
        monto_transfe = input("Ingrese el monto a transferir: $")
        cbu_transfe = input("Ingrese el CBU al cual desea transferir:")
        print("Su transferencia de $"+monto_extra+" al CBU "+cbu_transfe+" ha sido confirmada.")
        print("Ahora volverá al menú principal")
    elif opcion == "s" :
        print("=================================================================")
        print("++++++++++++++ Gracias por usar nuestros servicios ++++++++++++++")
        print("=================================================================")
        break
    elif opcion != "d" or "e" or "t" or "s" :
        print("Ha elegido una opción no disponible")
    else: opcion == ""
    opcion = "x"
# OK