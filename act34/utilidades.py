#Utilidades

def calcular_promedio(calificaciones):
    if not isinstance(calificaciones, list):
        raise ValueError("Se esperaba una lista de calificaciones.")
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)
