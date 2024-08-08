#Crea una clase Producto con atributos de instancia como nombre, precio, cantidad_disponible y codigo_producto. Luego, crea una clase CarritoCompras que permita a los clientes agregar productos, eliminar productos y calcular el total de la compra. Utiliza un atributo de clase para rastrear la cantidad total de productos en el carrito de compras de todos los clientes. Crea instancias de ambas clases y simula operaciones de compra.

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible, codigo_producto):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.codigo_producto = codigo_producto

    def __repr__(self):
        return f"Producto('{self.nombre}', Precio: ${self.precio}, Código: {self.codigo_producto})"

class Carrito_Compras:
    cantidad_total_productos = 0

    def __init__ (self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto.cantidad_disponible > 0:
            self.productos.append(producto)
            Carrito_Compras.cantidad_total_productos += 1
            producto.cantidad_disponible -= 1
        else:
            print(f"Producto '{producto.nombre}' no está disponible.")

    def eliminar_producto(self, codigo_producto):
        for producto in self.productos:
            if producto.codigo_producto == codigo_producto:
                self.productos.remove(producto)
                Carrito_Compras.cantidad_total_productos -= 1
                return f"Producto: '{producto.nombre}' ha sido eliminado del carrito."
        return f"No se encontró el producto con el código '{codigo_producto}' en el carrito."

    def calcular_total_compra(self):
        if not self.productos:
            return "Carrito vacío."
        total = sum([producto.precio for producto in self.productos])
        return f"Total de compra: ${total}"

    def productos_en_carrito(self):
        return self.productos

#Instanciando objetos
producto1 = Producto("Laptop", 800, 5, "LP001")
producto2 = Producto("Tablet", 400, 10, "TB002")

carrito = Carrito_Compras()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

print(carrito.eliminar_producto("LP001"))
print(carrito.calcular_total_compra())
print(carrito.productos_en_carrito())
