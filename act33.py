#Escribe un programa que permita a un profesor registrar las calificaciones de sus estudiantes en un archivo json llamado "calificaciones.json".
#El programa debe permitir al profesor ingresar nombres de estudiantes y sus calificaciones. Luego, debe guardar estos datos en el archivo cuando termine el programa para
#Persistir estos datos para futuras ejecuciones del programa. Utilizar los nombres de los alumnos como claves y las notas como valores.

#Ten en cuenta que el modo read del open genera un error al querer abrir un archivo que no existe.
#Y, a diferencia del read en los txt, el json.load también genera un error si el archivo no tiene nada.

import json
import os

#Ruta archivo
ruta_carpeta = os.path.expanduser("~/Desktop/Python/guia de ejercicios complementarios/txts/")
file_name = os.path.join(ruta_carpeta, "calificaciones.json")

#Crear la carpeta si no existe
os.makedirs(ruta_carpeta, exist_ok = True)

#Funcion para cargar las calificaciones desde el archivo
def cargar_calificaciones():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return{}

#Funcion para guardar calificaciones en el archivo
def guardar_calificaciones(calificaciones):
    with open(file_name, "w", encoding = "utf-8") as file:
        json.dump(calificaciones, file, indent=4)

def calcular_promedio(calificaciones):
    if not isinstance(calificaciones, list):
        raise ValueError("Se esperaba una lista de calificaciones.")
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)

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

    #Promedio de cada estudiante
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
