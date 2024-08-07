#Crea un programa que solicite al usuario ingresar nombres separados por comas. Luego, crea un conjunto con los nombres ingresados y muestra por pantalla la cantidad de nombres únicos en el conjunto.

#Ingresar nombres separados por comas
nombres = input("Ingresa los nombres separados por comas: ")

#Conjunto con los nombres ingresados
conjunto = set(nombres.split(","))
print(conjunto)

#Muestra la cantidad de nombres en el conjunto
cantidad_nombres = (len(conjunto))
print("Cantidad de nombres: ", cantidad_nombres)
