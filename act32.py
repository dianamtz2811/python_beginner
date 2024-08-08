#Basándonos en el ejercicio 1 de funciones, edita el código para que el programa guarde el listado de tareas en un json al terminar la ejecución del programa y lo recupere al iniciarse el mismo.

import json
import os

def mostrar_menu():
        print("\nElija una opción del menú: ")
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Listar tareas pendientes")
        print("4. Salir")

def agregar_tarea(tareas):
    descripcion = input("\nIngrese la tarea a agregar: ")
    tareas.append({'descripcion': descripcion, 'completada': False})
    print("\nTarea agregada.")

def marcar_completada(tareas):
    listar_tareas(tareas, mostrar_completadas=False)
    try: 
        indice = int(input("\nIngresa el número de la tarea que completaste: ")) -1
        if 0 <= indice < len(tareas) and not tareas [indice]['completada']:
            tareas [indice]['completada'] = True
            print("\nTarea marcada como completada")
        else:
            print("\nNúmero de tarea inválido o la tarea ya está completada")
    except ValueError:
        print("\nPor favor, ingresa un número válido.")

def listar_tareas(tareas, mostrar_completadas=True):
    print("\n=== Tareas Pendientes ===")
    for i, tarea in enumerate(tareas):
        estado = "✓" if tarea['completada'] else "✗"
        if not tarea['completada'] or mostrar_completadas:
            print(f"{i + 1}. [{estado}] {tarea['descripcion']}")

def cargar_tareas():
    ruta_archivo = os.path.expanduser('~/Desktop/Python/guia de ejercicios complementarios/txts/tareas.json')
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r') as archivo:
                return json.load(archivo)
        return[]
    except Exception as e:
        print(f"Error al cargar tareas: {e}")
        return []


def guardar_tareas(tareas):
    ruta_archivo = os.path.expanduser('~/Desktop/Python/guia de ejercicios complementarios/txts/tareas.json')
    try:
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        with open(ruta_archivo, 'w', encoding = "utf-8") as archivo:
            json.dump(tareas, archivo, indent=4)
    except Exception as e:
        print("Error al guardar tareas: {e}")

def principal ():
    tareas = cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("\nIngrese el número de la opción elegida: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            marcar_completada(tareas)
        elif opcion == "3":
            listar_tareas(tareas, mostrar_completadas=False)
        elif opcion == "4":
            guardar_tareas(tareas)
            print("¡Hasta luego!")
            break
        else:
            print("\nOpción no válida, elige otra")

if __name__ == "__main__":
    principal()