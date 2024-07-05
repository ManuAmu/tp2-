import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))

    circulo = Circulo(radio)
    area = circulo.calcular_area()
    perimetro = circulo.calcular_perimetro()


    print(f"\nEl area del ciculo es: {area}")
    print(f"\nEl perimetro del circulo es: {perimetro}")
    print()

