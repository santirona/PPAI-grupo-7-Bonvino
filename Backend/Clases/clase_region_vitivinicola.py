
class RegionVitivinicola:
    def __init__(self, nombre, descripcion, provincia):
        self.nombre = nombre
        self.descripcion = descripcion
        self.bodegas = []
        self.provincia = provincia 

    def contarBodegas(self):
        return len(self.bodegas)

    def getNombre(self):
        return self.nombre

    def obtenerPais(self):
        if self.provincia:
            return self.provincia.obtenerNombrePais()
        return None
    
    def __str__(self):
        return f"Nombre Region: {self.nombre}, \nDescripcion region: {self.descripcion}, {self.provincia}"
