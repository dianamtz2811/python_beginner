#Escribe un programa que tome una lista de palabras ingresadas por el usuario. Luego, que muestre cada palabra una por una. Si la palabra es "salir", finaliza el programa. Si la palabra es "omitir", se pasa a la siguiente iteración. Al final, si ninguna palabra fue "salir", muestra un mensaje avisando la situación.

lista_palabras = input("Ingresa una lista de palabras: ").split()

for palabra in lista_palabras:
    if palabra == "salir":
        print("El programa finalizó")
        break
    elif palabra == "omitir":
        continue
    else:
        print(palabra)

else:
    print("No se encontró la palabra 'salir'")