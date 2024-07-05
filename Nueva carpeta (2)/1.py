
class Estudiante():
    """Desafío 1. documentación del codigo"""

    def __init__(self, nombre, nota_evaluacion):
        
        self.__nombre = nombre
        self.__nota_evaluacion = nota_evaluacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def nota_evaluacion(self):
        return self.__nota_evaluacion

    @nota_evaluacion.setter
    def nota_evaluacion(self, nota_evaluacion):
        self.__nota_evaluacion = nota_evaluacion

    def is_aprobado(self):

        if self.__nota_evaluacion >= 6:
            return f"aprobo con: {self.__nota_evaluacion}"
        else:
            return f"desaprobo con: {self.__nota_evaluacion}"
        
def execute():
        
        estudiante=Estudiante("Corvalan Juan", 9)
        estudiante2= Estudiante("Rodriguez Milagros", 6)
        estudiante3= Estudiante("Anriquez Matias", 2)

        print(f" El estudiante {estudiante.nombre} {estudiante.is_aprobado()}\n")
        print(f" El estudiante {estudiante2.nombre} {estudiante2.is_aprobado()}\n")
        print(f" El estudiante {estudiante3.nombre} {estudiante3.is_aprobado()}")


if __name__ =='__main__':
    execute()
    

