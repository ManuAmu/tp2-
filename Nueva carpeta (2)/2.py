
class Triangulo():
    def __init__(self,cateto_opuesto,cateto_adyacente,hipotenusa):
        self.__cateto_opuesto=cateto_opuesto
        self.__cateto_adyacente=cateto_adyacente
        self.__hipotenusa=hipotenusa    

    @property
    def cateto_opuesto(self):
        return self.cateto_opuesto
    @property
    def cateto_adyacente(self):
        return self.cateto_adyacente
    @property
    def hipotenusa(self):
        return self.hipotenusa
    def magnitud_lado_mayor(self):
        return max([self.__cateto_opuesto,self.__cateto_adyacente,self.__hipotenusa])

   
    def tipo_triangulo(self):
        if self.__cateto_opuesto==self.__cateto_adyacente==self.__hipotenusa:
            return'triangulo equilatero'
        elif self.__cateto_adyacente==self.__cateto_opuesto or self.__cateto_opuesto==self.__hipotenusa or self.__cateto_adyacente==self.__hipotenusa:
            return f'Triangulo isoceles'
        else:
            return f'Triangulo escaleno'

def execute():
        
    triangulo=Triangulo(5,3,3)
    
    print(f'el mayor lado del triangulo es: {triangulo.magnitud_lado_mayor()}')
    
    print(f'el tipo de triangulo es: {triangulo.tipo_triangulo()}' )
        
if __name__ =='__main__':
    execute()