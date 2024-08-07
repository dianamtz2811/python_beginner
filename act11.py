#Crea un programa que solicite un número entero al usuario y determine si es un número negativo, positivo o igual a cero. En caso de ser positivo, verifica si es par o impar.

#Solicitar un numero al usuario
numero = int(input("Ingrese un numero: "))

#Verificar si es negativo
if numero < 0:
    print("El numero es negativo")
#Verificar si es positivo
elif numero > 0:
    print("El numero es positivo")

#Verificar si es cero
if numero == 0:
    print("El numero es cero")

#Verificar si es par
if numero % 2 == 0:
    print("El numero es par")
#Verificar si es impar
else:
    print("El numero es impar")