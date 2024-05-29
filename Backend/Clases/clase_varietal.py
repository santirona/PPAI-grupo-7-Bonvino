class Varietal:
    def __init__(self, descripcion, porcentaje_composicion):
        self.descripcion = descripcion
        self.porcentaje_composicion = porcentaje_composicion

    def conocerTipoUva(self):
        pass

    def esDeTipoUva(self, tipo_uva):
        return tipo_uva.lower() in self.descripcion.lower()

    def getDescripcion(self):
        return self.descripcion

    def mostrarPorcentaje(self):
        return self.porcentaje_composicion

# # Example usage
# varietal = Varietal.new("Cabernet Sauvignon", 85)
# print(varietal.getDescripcion())  # Output: Cabernet Sauvignon
# print(varietal.mostrarPorcentaje())  # Output: 85
# print(varietal.esDeTipoUva("Cabernet"))  # Output: True
