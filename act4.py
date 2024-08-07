#Crea un programa que, teniendo en cuenta la siguiente tupla, muestre el valor del segundo elemento de la misma. Además, debe mostrar cuántas veces se repite este valor y cuál es el índice del valor repetido.

palabras_tupla = ("manzana", "pera", "uva", "naranja", "sandía", "manzana", "plátano", "kiwi", "pera", "fresa", "mango", "uva", "cereza", "manzana", "durazno")

segundo_valor = (palabras_tupla[1])

repeticiones = (palabras_tupla.count(segundo_valor))

indice = palabras_tupla.index(segundo_valor, 2)

print("El segundo valor de la tupla es: ", segundo_valor)
print("Ese valor se repite ",repeticiones, " veces.")
print("El índice del valor repetido es: ", indice)
