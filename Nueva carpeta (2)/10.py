import unittest
 
class Vehiculo:
      def __init__(self, nombre):
            self.nombre = nombre;
 
      def mover(self):
            return f"{self.nombre} se está moviendo"
 
class VehiculoTerrestre(Vehiculo):
 
      def __init__(self, nombre, ruedas):
            super().__init__(nombre)
            self.ruedas = ruedas;
 
      def mover(self):
            return f"{self.nombre} se está moviendo en la tierra/calle con {self.ruedas} ruedas"
 
class Auto(VehiculoTerrestre):
 
      def __init__(self, nombre, ruedas, tipo):
            super().__init__(nombre, ruedas)
            self.tipo = tipo
 
class AutoPolicia(Auto):
 
      def __init__(self, nombre = 'Auto de Policía', ruedas=4, tipo='policia'):
            super().__init__(nombre, ruedas, tipo)
 
class Remis(Auto):
 
      def __init__(self, nombre = 'Remis', ruedas=4, tipo='Remis'):
            super().__init__(nombre, ruedas, tipo)
 
class Bicicleta(VehiculoTerrestre):
 
      def __init__(self, nombre='Bicicleta', ruedas=2):
            super().__init__(nombre, ruedas)
 
class Barco(Vehiculo):
 
      def __init__(self, nombre='Barco'):
            super().__init__(nombre)
 
      def mover(self):
            return f"{self.nombre} está navegando"
 
 
# Test unitario de funcionalidad
 
class Test(unittest.TestCase):
      def testVehiculo(self):
            vehiculo = Vehiculo("Vehículo")
            self.assertEqual(vehiculo.mover(), "Vehículo se está moviendo")
 
      def testVehiculoTerrestre(self):
            vehiculo = VehiculoTerrestre("Vehículo Terrestre", 4)
            self.assertEqual(vehiculo.mover(), "Vehículo Terrestre se está moviendo en la tierra/calle con 4 ruedas")
 
      def testAuto(self):
            vehiculo = Auto("Auto", 4, "personal")
            self.assertEqual(vehiculo.mover(), "Auto se está moviendo en la tierra/calle con 4 ruedas")
 
      def testAutoPolicia(self):
            vehiculo = AutoPolicia()
            self.assertEqual(vehiculo.mover(), "Auto de Policía se está moviendo en la tierra/calle con 4 ruedas")
 
      def testRemis(self):
            vehiculo = Remis()
            self.assertEqual(vehiculo.mover(), "Remis se está moviendo en la tierra/calle con 4 ruedas")
 
      def testBicicleta(self):
            vehiculo = Bicicleta()
            self.assertEqual(vehiculo.mover(), "Bicicleta se está moviendo en la tierra/calle con 2 ruedas")
 
      def testBarco(self):
            vehiculo = Barco()
            self.assertEqual(vehiculo.mover(), "Barco está navegando")
 
unittest.main()