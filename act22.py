#Crea un programa que permita calcular el promedio de un número variable de notas ingresadas por el usuario. La función calcular_promedio puede recibir un número variable de notas. 
#Luego, muestra el promedio de las notas ingresadas.

def calcular_promedio(notas):
#Calcula el promedio de una lista de notas
    if len(notas) == 0:
        return 0 #Evita que se haga una división si no hay notas
    return sum(notas) / len(notas)

def obtener_notas():
#Obtiene las notas hasta que el usuario ingrese 'Fin'
    notas = []
    print("\nIngresa tu notas separadas por una coma y escribe 'Fin' para terminar")

    while True:
        entrada = input("\nNota: ")

        if entrada.strip().lower() == "fin":
            break

        try:
            nota = float(entrada)
            notas.append(nota)
        
        except ValueError:
            print("\nEntrada no válida, Ingresa un número o 'fin' para terminar.")

    return notas

def main():
#Funcion principal
    notas = obtener_notas()
    promedio = calcular_promedio(notas)
    print(f"\nEl promedio de las notas es {promedio:.2f}")

if __name__ == "__main__":
    main()



