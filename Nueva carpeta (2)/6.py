
class Cuenta:
    def __init__(self, titular, cantidad, tipo_cuenta):
        self.titular = titular
        self.cantidad = cantidad
        self.tipo_cuenta = tipo_cuenta
    
    def consultar_titular(self):
        return f"Titular: {self.titular}"
    
    def consultar_cantidad(self):
        return f"Cantidad en cuenta: {self.cantidad}"
    
    def consultar_tipo_cuenta(self):
        return f"Tipo de cuenta: {self.tipo_cuenta}"

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad, tipo_cuenta="Caja de Ahorro")
 

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad, tipo_cuenta="Plazo Fijo")
        self.plazo = plazo
        self.interes = interes
    
    def calcular_interes(self):
        return self.cantidad * self.interes / 100
    
    def consultar_plazo(self):
        return f"Plazo: {self.plazo} dias"
    
    def consultar_interes(self):
        return f"Tasa de interes: {self.interes}%"
    
    def consultar_total_interes(self):
        return f"Total de interes a pagar: {self.calcular_interes()}"

caja_ahorro1 = CajaAhorro("Cuevas Valentina", 3000)
caja_ahorro2 = CajaAhorro("Gomez Alvaro", 7000)

plazo_fijo1 = PlazoFijo("Cuevas Valentina", 5000, 45, 3.5)
plazo_fijo2 = PlazoFijo("Gomez Alvaro", 15000, 120, 6.0)


print("\n")
print(caja_ahorro1.consultar_titular())
print(caja_ahorro1.consultar_cantidad())
print(caja_ahorro1.consultar_tipo_cuenta())
print()


print(plazo_fijo2.consultar_titular())
print(plazo_fijo2.consultar_cantidad())
print(plazo_fijo2.consultar_tipo_cuenta())
print(plazo_fijo2.consultar_plazo())
print(plazo_fijo2.consultar_interes())
print(plazo_fijo2.consultar_total_interes())
print()