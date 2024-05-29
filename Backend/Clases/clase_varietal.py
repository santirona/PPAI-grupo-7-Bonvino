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
    
    def __str__(self):
        return f"Descripcion Varietal: {self.descripcion}, \nPorcentaje Composicion: {self.porcentaje_composicion}"


