
class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    @property
    def num1(self):
        return self.__num1

    @num1.setter
    def num1(self, num1):
        self.__num1 = num1

    @property
    def num2(self):
        return self.__num2

    @num2.setter
    def num2(self, num2):
        self.__num2 = num2


    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir por cero"

def main():
        
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
       
        calculadora = Calculadora(num1, num2)

        print(f"Suma: {calculadora.suma()}")
        print(f"Resta: {calculadora.resta()}")
        print(f"Multiplicación: {calculadora.multiplicacion()}")
        print(f"División: {calculadora.division()}")

if __name__ == "__main__":
    main()