class Vino: 
    def __init__(self, anada, fecha_actualizacion, imagen_etiqueta, nombre, nota_de_cata_bodega, precio_ARS, bodega, varietales):
        self.anada = anada
        self.nombre = nombre
        self.bodega = bodega
        self.varietales = varietales
        self.precio_ARS = precio_ARS
        self.resenas = []
        self.imagen_etiqueta = imagen_etiqueta
        self.nota_de_cata_bodega = nota_de_cata_bodega
        self.fecha_actualizacion = fecha_actualizacion
        self.puntuacion_promedio = None
    
    def getVarietales(self):
        return [varietal.getDescripcion() for varietal in self.varietales]
    
    def getResenas(self):
        return [resena.getComentario() for resena in self.resenas]

    def obtener_info(self):
        return f"{self.nombre}, {self.varietales}, {self.bodega.nombre}, {self.provincia.nombre}, {self.pais.nombre}, {self.precio}"
    
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    def tenesResenaDeTipoEnPeriodo(self, tipo, desde, hasta):
        if tipo == "Reseñas de Sommelier":
            for resena in self.resenas:
                if (resena.sosDePeriodo(desde, hasta) and resena.sosDeSommelier()):
                    return(True)
                else:
                    return(False)
                
        elif tipo == "Reseñas Normales":
            for resena in self.resenas:
                if (resena.sosDePeriodo(desde, hasta)):
                    return(True)
                else:
                    return(False)
        
        else: 
            return(False)
            
    def calcularPuntajeDeSommelierEnPeriodo(self, fecha_desde, fecha_hasta):
        acumulador_puntaje = 0
        cantidad_resenas_sommelier = 0
        for resena in self.resenas:
            if (resena.sosDePeriodo(fecha_desde, fecha_hasta) and resena.sosDeSommelier()):
                acumulador_puntaje += resena.getPuntaje()
                cantidad_resenas_sommelier += 1
        
        self.calcularPuntajePromedio(acumulador_puntaje,cantidad_resenas_sommelier)
        
    def calcularPuntajeDeNormalesEnPeriodo(self, fecha_desde, fecha_hasta):
        acumulador_puntaje = 0
        cantidad_resenas = 0
        for resena in self.resenas:
            if (resena.sosDePeriodo(fecha_desde, fecha_hasta)):
                acumulador_puntaje += resena.getPuntaje()
                cantidad_resenas += 1
        
        self.calcularPuntajePromedio(acumulador_puntaje,cantidad_resenas)
        

    def calcularPuntajePromedio(self, acumulador, cantidad):
        self.puntuacion_promedio = round((acumulador / cantidad), 2)

        
    def agregarResenas(self, resena):
        self.resenas.append(resena)


    """
    def buscarinfoBodega(self):
        return (self.bodega.getNombre(self),self.bodega.obtenerRegionYPais(self))
    """