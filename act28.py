#Crea una clase Empleado que tenga los siguientes atributos de instancia: nombre, apellido, edad, salario. Luego, crea una clase Gerente que herede de Empleado y tenga un atributo adicional departamento. Define métodos de instancia para ambas clases, como mostrar_informacion para mostrar los detalles de un empleado y aumentar_salario para aumentar el salario de un empleado en un porcentaje dado. Crea instancias de ambas clases y realiza algunas operaciones.

class Empleado:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}")
        print(f"Salario: {self.salario}")

    def aumentar_salario(self, porcentaje):
        incremento = self.salario * (porcentaje / 100)
        self.salario += incremento
        print(f"Salario aumentado en un porcentaje de {porcentaje}%. Nuevo salario: {self.salario}")

class Gerente(Empleado):
    def __init__(self, nombre, apellido, edad, salario, departamento):
        super().__init__(nombre, apellido, edad, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")

#Instanciando Empleado y Gerente
empleado1 = Empleado("Diana", "Martínez", 25, 8000)
gerente1 = Gerente("Angélica", "Pérez", 60, 15000, "gerencia")

#Mostrar información de los empleados
print("Mostrando información del empleado: ")
empleado1.mostrar_informacion()

print("Mostrando información del gerente: ")
gerente1.mostrar_informacion()

#Aumentar salario de los empleados
print("Aumentar salario del empleado: ")
empleado1.aumentar_salario(10)

print("Aumentar salario del gerente: ")
gerente1.aumentar_salario(20)

