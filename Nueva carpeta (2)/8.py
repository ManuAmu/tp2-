
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

if __name__ == "__main__":
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    rectangulo = Rectangulo(base, altura)
    area = rectangulo.calcular_area()

    print()
    print(f"El área del rectángulo es de: {area}")