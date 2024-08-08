#Crea un programa que permita a un usuario llevar un registro de tareas pendientes. El programa debe:
#Permitir al usuario agregar tareas.
#Marcar tareas como completadas. agregámdole un tilde o algo que identifique que se completó al principio de la tarea.
#Listar las tareas pendientes. 

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

def principal ():
    tareas = []
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
            print("¡Hasta luego!")
            break
        else:
            print("\nOpción no válida, elige otra")

if __name__ == "__main__":
    principal()



