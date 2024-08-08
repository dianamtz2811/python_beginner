#Crea un programa que permita a un usuario configurar la red de una computadora. El programa debe aceptar argumentos clave para configurar la dirección IP, la máscara de subred y la puerta de enlace. Luego, muestra la configuración de red completa.

def configurar_red(**kwargs):
    print("\nConfiguración de Red: ")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

while True:
    print("\n 1. Configurar Red")
    print(" 2. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        ip = input("Ingrese la dirección IP: ")
        mascara = input("Ingrese la máscara de subred: ")
        puerta_enlace = input("Ingresa la puerta de enlace: ")
        configurar_red(IP=ip, Máscara=mascara, Puerta_enlace=puerta_enlace)
    elif opcion == "2":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, ingrese 1 o 2")