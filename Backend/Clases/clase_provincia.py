from clase_pais import Pais

class Provincia:
    def __init__(self, nombre, pais, regionVitivinicola):
        self.nombre = nombre
        self.pais = pais
        self.regionVitivinicola = regionVitivinicola

    def contarRegiones(self):
        pass

    def mostrarRegiones(self):
        pass

    def obtenerPais(self):
        return self.pais