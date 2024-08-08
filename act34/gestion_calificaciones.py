#Con las funciones de los ejercicios anteriores, sepáralas en 2 o más módulos y genera un paquete que incluya estos módulos.
#Recuerda que en los módulos deben ir solo código que sea de definición y, en caso de querer agregar código de ejecución en alguno de los módulos, debe agregarse dentro de la siguiente condicional

#if __name__ == '__main__':

#Gestion de calificaciones

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
    with open(file_name, "w") as file:
        json.dump(calificaciones, file, indent=4)



