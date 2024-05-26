class Vino: 
    def __init__(self, id, nombre, bodega, region_vitivinicola, provincia, pais, varietal, precio):
        self.id = id
        self.nombre = nombre
        self.bodega = bodega
        self.region_vitivinicola = region_vitivinicola
        self.provincia = provincia
        self.pais = pais
        self.varietal = varietal
        self.precio = precio
    
    def obtener_info(self):
        return f"{self.nombre}, {self.varietal}, {self.bodega.nombre}, {self.region_vitivinicola.nombre}, {self.provincia.nombre}, {self.pais.nombre}, {self.precio}"