#Crea dos conjuntos con números ingresados por el usuario y separados por coma. 
#Luego, muestra cuáles elementos tienen en común los conjuntos y crea un nuevo conjunto que contenga la unión de ambos.

#Solicitar dos conjuntos de números al usuario
conjunto_1 = input("Ingresa un conjunto de números separados por una coma: ")
conjunto_2 = input("Ingresa un segundo conjunto de números separados por una coma: ")

#Separar los conjuntos en listas
conjunto_1 = conjunto_1.split(",")
conjunto_2 = conjunto_2.split(",")

#Crear un conjunto con los elementos comunes
conjunto_comun = set(conjunto_1).intersection(set(conjunto_2))
print("Los elementos comunes son: ", conjunto_comun)

#Crear un conjunto con la unión de ambos
conjunto_union = set(conjunto_1).union(set(conjunto_2))
print("El nuevo conjunto es: ", conjunto_union)