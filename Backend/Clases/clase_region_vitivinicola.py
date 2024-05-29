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
        if self.provincias:
            return self.provincias[0].obtenerPais()
        return None
