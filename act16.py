#Crea un programa que solicite al usuario ingresar una palabra. Luego, recorre la palabra y cuenta cuántas vocales contiene. Al final, si no se encontraron vocales, muestra un mensaje comunicando que la palabra ingresada solo contiene consonantes.

palabra = input("Ingresa una palabra: ")

def contador_vocales(palabra):
    contador = 0
    for i in palabra:
        if i in "AaEeIiOoUu":
            contador += 1
    return contador

vocales = contador_vocales(palabra)

if vocales > 0:
    print(f"La palabra '{palabra}' contiene {vocales} vocales")
else:
    print(f"La palabra '{palabra}' sólo contiene consonantes")

