#Escribe un programa que permita al usuario ingresar el precio de un producto y un código de descuento. El programa debe validar si el precio es un número positivo y si el código de descuento es válido. Los errores posibles incluyen entradas no numéricas, números negativos y códigos de descuento no válidos. 
#Utiliza un bloque try-except con varios bloques except para manejar estos errores y mostrar mensajes de error específicos en cada caso. Ten en cuenta el uso de la instrucción raise comentada en la actividad anterior de ser necesario su uso.

#Los codigos de descuento son:

try:
    precio = float(input("Ingresa el precio del producto: "))
    codigo_descuento = input("Ingresa el código de descuento: ")

    if precio <= 0:
        raise ValueError("El precio debe ser un número positivo.")

    descuentos_validos = ["DESC10", "DESC20", "DESC30"]

    if codigo_descuento not in descuentos_validos:
        raise ValueError("Código de descuento no válido.")

    if codigo_descuento == "DESC10":
        precio_descuento = precio * 0.9
    elif codigo_descuento == "DESC20":
        precio_descuento = precio * 0.8
    else:
        precio_descuento = precio * 0.7

    print(f"El precio con descuento es: {precio_descuento}")

except ValueError as ve:
    print(f"Error de Valor: {ve}")
except TypeError:
    print("Error de tipo: El precio debe ser un número.")
except Exception as e:
    print(f"Error inesperado: {e}")