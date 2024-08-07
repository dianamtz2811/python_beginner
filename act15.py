#Escribe un programa que tome una lista de nombres ingresados por el usuario separados por un espacio y los liste mostrando su ubicacion.

nombres = input("Ingresa una lista de nombres separados por un espacio: ").split()

for indice, nombres in enumerate (nombres):
    print(f"Nombre {indice + 1}: {nombres} " )
