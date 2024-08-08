#Crea una clase Calculadora con un método de clase llamado suma que acepte dos números como argumentos y devuelva la suma de ellos. Luego, utiliza este método para realizar algunas operaciones de suma.

class Calculadora:
    @classmethod
    def suma(cls, num1, num2):
        return num1 + num2

resultado = Calculadora.suma(5, 6)
print(f"El resultado de la suma es {resultado}")  # Salida: 11