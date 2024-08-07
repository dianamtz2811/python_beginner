#Escribe un programa que tome un número entero ingresado por el usuario y determine si es un número par, divisible por 3 y 5 al mismo tiempo, o ninguno de los anteriores.

#Solicita un numero entero al usuario
numero = int(input("Ingresa un número entero: "))

#Variables para almacenar resultados
es_par = (numero % 2 == 0)
divisible_entre_3_y_5 = (numero % 3 == 0 and numero % 5 == 0)

#Determina si es par, divisible entre 3 y 5, o ninguno de los anteriores
if es_par:
    print("El número es par")
if divisible_entre_3_y_5:
    print("El número es divisible entre 3 y 5")
if not es_par and divisible_entre_3_y_5:
    print("El número no es par, ni divisible entre 3 ni 5")

