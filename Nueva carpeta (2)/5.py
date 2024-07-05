 
class Cliente:
 
    def __init__(self, nombre, cantidad_inicial=0):
        self.nombre = nombre
        self.cantidad = cantidad_inicial
 
    def depositar(self, monto):
        self.cantidad = self.cantidad + monto
        print(f"{self.nombre} depositó {monto}. Su saldo es de: {self.cantidad}")
 
    def extraer(self, monto):
        if self.cantidad >= monto:
            self.cantidad = self.cantidad - monto
            print(f"{self.nombre} extrajo {monto}. Su saldo es de: {self.cantidad}")
        else:
            print(f"{self.nombre} no tiene suficiente fondo para extraer {monto}. Su saldo es de: {self.cantidad}")
 
    def get_total(self):
        return self.cantidad
 
 
class Banco:
    def __init__(self):
        self.clientes = []
 
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
 
    def operar(self):
        for cliente in self.clientes:
            print("\n")
            print(f"Operaciones de {cliente.nombre}:")
            monto_deposito = float(input(f"Ingrese el monto a depositar para {cliente.nombre}: "))
            cliente.depositar(monto_deposito)
            monto_extraccion = float(input(f"Ingrese el monto a extraer para {cliente.nombre}: "))
            cliente.extraer(monto_extraccion)
 
    def deposito_total(self):
        total = sum(cliente.get_total() for cliente in self.clientes)
        print(f"\nEl total depositado en el banco es de: {total}")
        print("\n")
 
 
banco = Banco()
 
banco.agregar_cliente(Cliente("Rocio"))
banco.agregar_cliente(Cliente("Exequiel"))
banco.agregar_cliente(Cliente("Mariano"))
 
banco.operar()
banco.deposito_total()
