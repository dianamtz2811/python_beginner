#Define una clase Figura con un método de instancia area que devuelve el área de la figura. Luego, crea clases hijas como Circulo y Rectangulo que hereden de Figura y proporcionen implementaciones diferentes del método area.

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base =  base
        self.altura = altura

    def area(self):
        return self.base * self.altura

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

print(f"El área del círculo es {circulo.area()}")
print(f"El área del rectángulo es {rectangulo.area()}")