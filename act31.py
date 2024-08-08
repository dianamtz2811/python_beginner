#Escribe un programa en Python que permita a un usuario registrar sus gastos diarios en un archivo de texto llamado "gastos.txt". El programa debe permitir al usuario ingresar la descripción del gasto y la cantidad gastada. Luego, debe guardar estos datos en el archivo en el siguiente formato:

#"Fecha: {fecha} - Descripción: {descripción} - Cantidad: {cantidad}"
#Donde fecha es la fecha actual y descripción y cantidad son los datos ingresados por el usuario.

import datetime
import os

def registrar_gasto():
    while True:
        #Solicitar al usuario la descripcion y la cantidad del gasto
        descripcion = input("Ingrese la descripción del gasto (o 'Salir' para terminar): ")
        if descripcion.lower() == 'salir':
            print("Finalizando registro de datos.")
            break

        while True:
            try:
                cantidad = float(input("Ingrese la cantidad gastada: "))
                break
            except ValueError:
                print("Error: La cantidad debe ser un número.")

        #Obtener la fecha actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Formato al texto a guardar
        registro = f"Fecha: {fecha_actual} - Descripción: {descripcion} - Cantidad: {cantidad:.2f}\n"

        #Especificar la ruta en donde se va a guardar el archivo
        carpeta_base = os.path.expanduser("~/Desktop/Python/guia de ejercicios complementarios")
        carpeta_txts = os.path.join(carpeta_base, "txts")
        ruta_archivo = os.path.join(carpeta_txts, "gastos.txt")

        try:
            with open(ruta_archivo, "a", encoding="utf-8") as archivo:
                archivo.write(registro)
            print("Gasto registrado con éxito.")
        except Exception as e:
            print(f"Error: {e}")

#Llamar función
registrar_gasto()