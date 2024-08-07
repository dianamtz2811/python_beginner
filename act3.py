#Crea un programa que inicie con una lista de números enteros. Luego, solicita al usuario un número entero y un índice para reemplazar un elemento en la lista por el nuevo número ingresado en el índice ingresado. 
#Imprime la lista resultante.

#Corrobora que el índice que solicitas al usuario no exceda los índices que maneja la lista de números enteros.
#La lista de números inicial es a elección del programador

enteros = [1, 2, 3, 4, 5, 6]
num_usuario = int(input("Inserta el número que desees agregar "))

while True:
    posicion_num = int(input("Inserta la posición en la que quieres poner tu número "))
    if posicion_num > len(enteros):
        print("La posición que has insertado es mayor que la longitud de la lista")
    else:
        break

enteros.insert(posicion_num, num_usuario)
print(enteros)
