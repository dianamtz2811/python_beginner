#Desarrolla un programa que permita a un usuario registrar información de contactos (nombre, número de teléfono y correo electrónico). El programa debe almacenar estos contactos y permitir al usuario buscar contactos por nombre o número de teléfono. 

def mostrar_menu():
    print("\nElija una opción del menú:")
    print("\n1. Agregar un contacto")
    print("2. Ver lista de contactos")
    print("3. Buscar un contacto")
    print("4. Borrar un contacto")
    print("5. Salir")

def agregar_contacto(lista_contactos):
    nombre = input("\nIngrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")
    lista_contactos.append({'nombre':nombre, 'telefono': telefono, 'correo': correo})
    print("\nContacto agregado con éxito")

def ver_contactos(lista_contactos):
    print("\n=== Lista de contactos ===")
    for contacto in lista_contactos:
        print(f"Nombre: {contacto['nombre']}")
        print(f"Teléfono: {contacto['telefono']}")
        print(f"Correo: {contacto['correo']}")
        print("=" * 20)

def buscar_contacto(lista_contactos):
    criterio = input("\nIngrese el nombre del contacto a buscar: ").lower()
    encontrado = False
    print("\n=== Resultados de la búsqueda ===")
    for contacto in lista_contactos:
        if criterio in contacto['nombre'].lower() or criterio in contacto['telefono']:
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Correo: {contacto['correo']}")
            print("-" * 20)
            encontrado = True
        if not encontrado:
            print("\nNo se encontró ningún contacto con ese nombre")

def borrar_contacto(lista_contactos):
    criterio = input("\nIngrese el nombre del contacto que desea borrar: ").lower()
    for i, contacto in enumerate(lista_contactos):
        if criterio == contacto['nombre'].lower() or criterio == contacto['telefono']:
            del lista_contactos[i]
            print("\nContacto borrado con éxito")
            return
    print("\nNo se encontró ningún contacto con ese nombre")

def principal():
    lista_contactos = []
    while True:
        mostrar_menu()
        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            agregar_contacto(lista_contactos)
        elif opcion == "2":
            ver_contactos(lista_contactos)
        elif opcion == "3":
            buscar_contacto(lista_contactos)
        elif opcion == "4":
            borrar_contacto(lista_contactos)
        elif opcion == "5":
            print("\nSaliendo...")
            break
        else:
            print("Opción inválida, escoge otra.")

if __name__ == "__main__":
    principal() 