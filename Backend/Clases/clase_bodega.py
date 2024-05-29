""" from clase_region_vitivinicola import RegionVitivinicola """

class Bodega:
    def __init__(self, nombre, descripcion, historia, fechaUltimaActualizacion, periodoActualizacion, region_vitivinicola, coordenadasUbicacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.historia = historia
        self.fechaUltimaActualizacion = fechaUltimaActualizacion
        self.periodoActualizacion = periodoActualizacion
        self.coordenadasUbicacion = coordenadasUbicacion
        self.region_vitivinicola = region_vitivinicola

    def actualizarDatosVinos():
        pass

    def contarReseñas():
        pass
    
    def crearNuevoVino():
        pass

    def estaParaActualizarNovedadesVino():
        pass

    def getNombre(self):
        return self.nombre

    def mostrarTodosLosVinos():
        pass

    """ def obtenerRegionYPais(self):
        return(self.regionVitivinicola.__getNombre__(self),self.regionVitivinicola.obtenerPais(self)) """