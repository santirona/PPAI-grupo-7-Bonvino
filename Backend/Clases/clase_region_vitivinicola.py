from clase_bodega import Bodega
from clase_pais import Pais

class RegionVitivinicola:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre

    def __getNombre__(self):
        return self.nombre
    
    def contarBodega(self):
        pass

"""     def obtenerPais(self):
        return self.pais """