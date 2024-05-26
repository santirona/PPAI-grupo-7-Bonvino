""" from clase_region_vitivinicola import RegionVitivinicola """

class Bodega: 
    def __init__(self, coordenadaUbicacion, descripcion, fechaUltimaActualizacion, historia, nombre, periodoActualizacion, region_vitivinicola):
        self.coordenadaUbicacion = coordenadaUbicacion
        self.descripcion = descripcion
        self.fechaUltimaActualizacion = fechaUltimaActualizacion
        self.historia = historia
        self.nombre = nombre
        self.periodoActualizacion = periodoActualizacion
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