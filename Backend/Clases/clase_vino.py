from Clases.clase_bodega import Bodega
from Clases.clase_resena import Resena


class Vino: 
    def __init__(self, id, nombre, bodega, provincia, pais, precio):
        self.id = id
        self.nombre = nombre
        self.bodega = bodega
        self.provincia = provincia
        self.pais = pais
        self.varietales = []
        self.precio = precio
        self.resenas = []
        self.puntuacionPromedio = None
    
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
    
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    def tenesResenaDeTipoEnPeriodo(self, tipo, desde, hasta):
        for resena in self.resenas:
            if (resena.sosDePeriodo(desde, hasta) and resena.sosDeSommelier(tipo)):
                return(True)
            else:
                return(False)
            
    def calcularPuntajeDeSommelierEnPeriodo(self, fecha_desde, fecha_hasta):
        resenaEnPeriodo = []
        for resena in self.resenas:
            if (resena.sosDePeriodo(fecha_desde, fecha_hasta) and resena.sosDeSommelier()):
                resenaEnPeriodo.append(resena.getPuntaje())
        return resenaEnPeriodo


    def calcularPuntajePromedio(self, resenaEnPeriodo):
        """ puntuaciones = [reseña.getPuntaje() for reseña in self.reseñas
                        if reseña.sosDePeriodo(fecha_desde, fecha_hasta) and reseña.sosDeSommelier()]
        if puntuaciones:
            self.puntuacionPromedio = sum(puntuaciones) / len(puntuaciones) """
        suma = 0
        count = 0
        for puntaje in resenaEnPeriodo:
            suma += [puntaje]
            count += 1
        if count > 0:
            self.puntuacionPromedio = round((suma / count), 2)
        return self.puntuacionPromedio
        
    
    """
    def buscarinfoBodega(self):
        return (self.bodega.getNombre(self),self.bodega.obtenerRegionYPais(self))
    """