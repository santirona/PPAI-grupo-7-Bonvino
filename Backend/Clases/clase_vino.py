from clase_bodega import Bodega

class Vino: 
    def __init__(self, id, nombre, bodega, provincia, pais, varietales, precio, reseñas):
        self.id = id
        self.nombre = nombre
        self.bodega = bodega
        self.provincia = provincia
        self.pais = pais
        self.varietales = varietales
        self.precio = precio
        self.reseñas = reseñas
    
    def getVarietales(self):
        return [varietal.getDescripcion() for varietal in self.varietales]
    
    ###
    # ejemplo
        varietal1 = Varietal.new("Cabernet Sauvignon", 85)
        varietal2 = Varietal.new("Merlot", 15)
        vino = Vino(1, "Gran Reserva", "Bodega XYZ", "Mendoza", "Mendoza", "Argentina", [varietal1, varietal2], 25.50)
    ###
    
    
    def obtener_info(self):
        return f"{self.nombre}, {self.varietales}, {self.bodega.nombre}, {self.provincia.nombre}, {self.pais.nombre}, {self.precio}"
    
    def tenes_reseñas_de_tipo_en_periodo(self, tipo, desde, hasta):
        pass
    
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    """
    def buscarinfoBodega(self):
        return (self.bodega.getNombre(self),self.bodega.obtenerRegionYPais(self))
    """