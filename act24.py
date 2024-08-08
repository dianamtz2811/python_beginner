#Escribe un programa que permita al usuario ingresar su edad. El programa debe validar si la edad ingresada está dentro del rango de 18 a 65 años, y mostrar un mensaje correspondiente. Utiliza un bloque try-except con múltiples bloques except para manejar posibles errores relacionados con la entrada del usuario, como una entrada no numérica o una edad fuera del rango válido.
#Tip: puedes usar la funcionalidad 'raise' para que se genere una excepción.
#La función raise se utiliza para generar manualmente una excepción en Python. Puedes especificar el tipo de excepción que deseas generar y opcionalmente proporcionar un mensaje de error personalizado. Por ejemplo:
# Generar una excepción ValueError con un mensaje personalizado
#raise ValueError("Este es un mensaje de error personalizado.")
#En el ejemplo anterior, se genera una excepción ValueError con el mensaje "Este es un mensaje de error personalizado." Esta funcionalidad puede ser útil cuando deseas controlar el flujo de tu programa y generar excepciones específicas en función de condiciones personalizadas.

while True:
    try:
        edad = int(input("Ingrese su edad: "))

        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        elif edad < 18 or edad > 65:
            raise ValueError("La edad debe estar entre los 18 y 65 años.")
        else:
            print(f"Tu edad {edad} años, está dentro del rango de edad permitido.")
            breakpoint

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")