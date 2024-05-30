
class Pais:
    def __init__(self, nombre):
        self.nombre = nombre
        self.provincias = []

    def contarBodegas(self):
        total_bodegas = 0
        for provincia in self.provincias:
            for region in provincia.mostrarRegiones():
                total_bodegas += region.contarBodegas()
        return total_bodegas

    def getNombre(self):
        return self.nombre