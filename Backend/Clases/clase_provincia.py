from clase_region_vitivinicola import RegionVitivinicola
from clase_pais import Pais

class Provincia:
    def __init__(self, nombre, regionVitivinicola):
        self.nombre = nombre
        self.region = RegionVitivinicola(regionVitivinicola)

    def contarRegiones(self):
        pass

    def mostrarRegiones(self):
        pass

    def obtenerPais(self):
        return self.pais