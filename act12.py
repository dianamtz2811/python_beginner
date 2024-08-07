#Escribe un programa que tome un número entero ingresado por el usuario y muestre "Es positivo" si el número es mayor que cero, de lo contrario, muestra "No es positivo".

#Solicitar un número al usuario
numero_1 = int(input("Ingresa un número entero: "))
numero_2 = int(input("Ingresa un segundo número entero: ")) #Importante el int porque gracias a eso reconoce el numero como tal y no como str

#Declarar función del menu
def menu():
    print("\nElige qué quieres hacer con esos números: ")
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("\nIngresa una opción: "))
    return opcion

#Funcion de la suma
def sumar(numero_1, numero_2):
    suma = numero_1 + numero_2
    return suma

#Funcion de la resta
def restar(numero_1, numero_2):
    resta = numero_1 - numero_2
    return resta

#Funcion de la multiplicacion
def multiplicar(numero_1, numero_2):
    multiplicacion = numero_1 * numero_2
    return multiplicacion

#Funcion de la division
def dividir(numero_1, numero_2):
    if numero_2 == 0:
        print("\nNo se puede dividir entre cero, sopenco") #Importante para que no haya error
    else:
        division = numero_1 / numero_2
        return division

#Funcion del menú
while True:
    opcion = menu()
    if opcion == 1:
        resultado = sumar(numero_1, numero_2)
        print("\nLa suma es: ", resultado)

    elif opcion == 2:
        resultado = restar(numero_1, numero_2)
        print("\nLa resta es: ", resultado)

    elif opcion == 3:
        resultado = multiplicar(numero_1, numero_2)
        print("\nLa multiplicación es: ", resultado)

    elif opcion == 4:
        resultado = dividir(numero_1, numero_2)
        print("\nLa división es: ", resultado)

    elif opcion == 5:
        print("\nGracias por usar el programa")
        break
    else:
        print("\nOpción incorrecta")
        continue

    if isinstance(resultado, (int, float)): 
        if resultado < 0 :
            print("\nEl resultado es negativo")
        else:
            print("\nEl resultado es positivo")
        if resultado % 2 == 0 :
            print("\nEl resultado es par")
        else:
            print("\nEl resultado es impar")
