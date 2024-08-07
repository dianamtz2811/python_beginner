#Crea un programa que simule un inventario de productos en una tienda. Inicia con un diccionario que contenga algunos productos y sus cantidades. Luego, permite al usuario agregar un nuevo producto con su cantidad y actualizar la cantidad de un producto existente. Muestra el inventario actualizado.

#Productos y cantidades:
#Manzanas => 50
#Bananas => 30
#Peras => 40

# Crea un inventario
inventario = { 
    "Manzanas":50,
    "Bananas":30,
    "Peras":40
}

#Agregar un nuevo producto al inventario
def agregar_nuevo_producto ():
    nuevo_producto = input("\nIngresa el nombre del nuevo producto: ")
    cantidad_nuevo_producto = int(input("\nIngresa la cantidad del nuevo producto: "))
    inventario[nuevo_producto] = cantidad_nuevo_producto

    print("\nEl producto ha sido agregado al inventario")
    print("\nEl inventario ha quedado de la siguiente manera: ", inventario)

#Cambiar la cantidad de un producto ya existente
def cambiar_cantidad_producto ():
    producto_existente = input("\nIngresa el nombre del producto existente que quieres modificar: ")
    cantidad_producto_existente = int(input("\nIngresa la nueva cantidad del producto existente: "))
    inventario[producto_existente] = cantidad_producto_existente

    print("\nLa cantidad del producto", producto_existente, "ha sido actualizada")
    print("\nEl inventario ha quedado de la siguiente manera: ", inventario)

#Menu
def menu ():
    while True:
        print("\n1. Agregar un nuevo producto al inventario")
        print("\n2. Cambiar la cantidad de un producto ya existente")
        print("\n3. Salir")
        opcion = int(input("\nIngresa una opción: "))
        if opcion == 1:
            agregar_nuevo_producto()
        elif opcion == 2:
            cambiar_cantidad_producto()
        elif opcion == 3:
            print("\nGracias por usar el programa")
            break
        else:
            print("\nOpción incorrecta, ingresa el número de opción que quieres desarrollar")


#Imprimir el nuevo inventario actualizado
menu()
