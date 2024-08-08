#main

from gestion_calificaciones import cargar_calificaciones, guardar_calificaciones
from utilidades import calcular_promedio

def main():
    calificaciones = cargar_calificaciones()

    while True:
        nombre = input("Nombre del estuadiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break

        if nombre not in calificaciones:
            calificaciones[nombre] = []

        while True:
            calificacion = input(f"Ingrese la calificacion de {nombre} (o 'hecho' para terminar): ")
            if calificacion.lower() == 'hecho':
                break
            try:
                calificacion = float(calificacion)
                calificaciones[nombre].append(calificacion)
            except ValueError:
                print("Por favor, ingrese una calificación válida")

    guardar_calificaciones(calificaciones)
    mostrar_promedio(calificaciones)

def mostrar_promedio(calificaciones):
    print("\nPromedios de los estudiantes:")
    for nombre, notas in calificaciones.items():
        if not isinstance(notas, list):
            print(f"Error: El dato para {nombre} no es una lista.")
            continue
        promedio = calcular_promedio(notas)
        print(f"{nombre}: {promedio:.2f}")
    print("Calificaciones guardadas en 'calificaciones.json'.")

if __name__ == "__main__":
    main()

