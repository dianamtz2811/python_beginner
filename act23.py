#Desarrolla un programa que permita al usuario buscar información sobre ciudades. Tendrás un diccionario llamado ciudades_info que contiene información sobre algunas ciudades, como su país, población y puntos de interés. El programa debe permitir al usuario ingresar el nombre de una ciudad y mostrar la información correspondiente. El programa debe poder manejar el caso en el que la ciudad no existe en el diccionario y mostrando un mensaje avisando del error.

ciudades_info = {
    'Paris': {
        'Pais': 'Francia',
        'Poblacion': 2187526,
        'Puntos_de_Interes': ['Torre Eiffel', 'Louvre', 'Catedral de Notre-Dame']
    },
    'Nueva York': {
        'Pais': 'Estados Unidos',
        'Poblacion': 8398748,
        'Puntos_de_Interes': ['Estatua de la Libertad', 'Central Park', 'Times Square']
    },
    'Tokio': {
        'Pais': 'Japón',
        'Poblacion': 13929286,
        'Puntos_de_Interes': ['Torre de Tokio', 'Templo Senso-ji', 'Palacio Imperial']
    }
}

while True:
    ciudad = input("\nIngrese la ciudad de la que quiera obtener información: ")
    ciudad = ciudad.strip().title()

    if ciudad == 'Salir':
        print("¡Gracias por usar el buscador!")
        break

    try:
        informacion = ciudades_info[ciudad]
        print(f"Información sobre {ciudad}")
        print(f"Pais: {informacion['Pais']}")
        print(f"Poblacion: {informacion['Poblacion']}")
        print(f"Puntos de Interes: {', '.join(informacion['Puntos_de_Interes'])}")
    except KeyError:
        print(f"La ciudad {ciudad} no se encuentra en la base de datos")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
