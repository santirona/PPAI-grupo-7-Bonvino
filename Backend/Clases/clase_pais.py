from clase_provincia import Provincia

class Pais:
    def __init__(self, nombre, provinciaNombre):
        self.nombre = nombre
        self.provincia = Provincia(provinciaNombre)
    
    """ def contarBodegas(self):
        return len(self.) """ 

    def getNombre(self):
        return self.nombre
    
