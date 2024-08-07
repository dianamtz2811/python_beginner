#Imagina que estás administrando un pequeño almacén y deseas realizar un seguimiento de los productos en tu inventario. Escribe un programa que te permita ingresar el nombre y la cantidad de varios productos. Utiliza un bucle para recorrer los productos y mostrar su nombre y cantidad. Al final, muestra el total de productos en el inventario.

def main ():
    inventario = {}
    while True:
        nombre_producto = input("Ingrese el nombre del producto o 'salir' para terminar y hacer el recuento de productos: ")
        if nombre_producto.lower() == "salir" :
            break
        cantidad_producto = int(input(f"Ingrese la cantidad de {nombre_producto}: "))
        if nombre_producto in inventario:
            inventario[nombre_producto] += cantidad_producto
        else:
            inventario[nombre_producto] = cantidad_producto

    print("\nInventario: ")
    total_productos = 0
    for producto, cantidad in inventario.items():
        print(f"\n{producto}: {cantidad}")
        total_productos += cantidad

    print(f"\nTotal de productos en el inventario: {total_productos}")

if __name__=="__main__":
    main()



