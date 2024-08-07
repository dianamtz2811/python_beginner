#Crea un programa que solicite dos números enteros al usuario y determine si ambos son números pares.

#Pide dos numeros al usuario
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

#Comprueba si ambos son pares
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos numeros son pares")
else:
    print("Al menos uno de los numeros no es par")