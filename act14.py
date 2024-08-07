#Escribe un programa que tome un número entero positivo ingresado por el usuario y muestre la tabla de multiplicar de ese número. Repite la solicitud al usuario de ingresar un nuevo número hasta que ingrese un cero.


def tabla_multiplicar ():
    numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
    if numero == 0:
        print("Fin del programa")
    else:
        for i in range(1,11):
            print(numero,"x",i,"=",numero*i)

tabla_multiplicar()

