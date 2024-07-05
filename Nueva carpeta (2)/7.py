
class Persona:
 
      def __init__(self, nombre='', edad=None, dni=''):
            self._nombre = nombre
            self._edad = edad
            self._dni = dni
 
      def __str__(self):
            return f"Hola {self.nombre}"
 
      #Setters & Getters
      @property #Getter
      def nombre(self):
            return self._nombre
 
      @nombre.setter
      def nombre(self, nuevoNombre):
            self._nombre = nuevoNombre
 
      @property
      def edad(self):
            return self._edad
 
      @edad.setter
      def edad(self, nuevaEdad):
            self._edad = nuevaEdad
 
      @property
      def dni(self):
            return self._dni
 
      @dni.setter
      def dni(self, nuevoDni):
            self._dni = nuevoDni
 
      def mostrar(self):
            print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")
 
      def es_mayor_de_edad(self):
            return self.edad is not None and self.edad >= 18


persona = Persona("Carabajal Nahuel", 15,53356225 )
persona2 = Persona("Diaz Carlos", 28, 40356225 )
 
print() 
persona.mostrar()
print(f"Es mayor de edad: {persona.es_mayor_de_edad()}")

print()
persona2.mostrar()
print(f"Es mayor de edad: {persona2.es_mayor_de_edad()}")
print()