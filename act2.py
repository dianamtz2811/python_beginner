#Crea un programa que tome una cadena de texto como entrada del usuario. Luego, muestra por pantalla los primeros tres caracteres de la cadena, seguidos por los tres últimos caracteres. Además, concatena ambos subconjuntos y muestra el resultado.

#Pedirle al usuario una oración
texto = input("Escribe una oración ")

#Obtener los primeros tres caracteres
primeros_tres = (texto[:3])

#Obtener los últimos tres caracteres
ultimos_tres = (texto[-3:])

#Concatenar ambos subconjuntos
concatenados = (texto[:3] + texto[-3:])

#prints
print("Primeros tres caracteres: ", primeros_tres)
print("Últimos tres caracteres: ", ultimos_tres)
print("Concatenados: ", concatenados)
