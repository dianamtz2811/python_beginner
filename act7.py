#Crea un programa que tome una oración ingresada por el usuario y realice las siguientes operaciones: convierte la oración a mayúsculas, cuenta cuántas veces aparece la letra "o", y muestra la oración sin espacios en blanco al inicio y al final.

#Obtener una oración del usuario
oracion = input("Escribe una oración: ")

#Convertir la oración a mayúsculas
mayuscula = oracion.upper()
print(f"Tu oracion convertida en mayúsculas: ", mayuscula)

#Contar las letras o
print(f"La letra 'o' aparece {oracion.count('o')} veces en tu oración.")

#Mostrar la oración sin espacios en blanco al inicio y al final
print(f"Tu oración sin espacios en blanco al inicio y al final: {oracion.strip()}")