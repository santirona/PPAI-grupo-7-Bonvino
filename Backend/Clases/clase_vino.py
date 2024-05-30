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
    
    def buscarVarietales(self):
        return [varietal.getDescripcion() for varietal in self.varietales]
    
    def getResenas(self):
        return [resena.getComentario() for resena in self.resenas]

    def obtener_info(self):
        return f"{self.nombre}, {self.varietal}, {self.bodega.nombre}, {self.provincia.nombre}, {self.pais.nombre}, {self.precio}"
    
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio_ARS
    
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
        
        return self.calcularPuntajePromedio(acumulador_puntaje,cantidad_resenas)
        

    def calcularPuntajePromedio(self, acumulador, cantidad):
        self.puntuacion_promedio = round((acumulador / cantidad), 2)
        return self.puntuacion_promedio

        
    def agregarResenas(self, resena):
        self.resenas.append(resena)



    def buscarinfoBodega(self):
        pais ,region=self.bodega.obtenerRegionYPais()
        return (self.bodega.getNombre(),region, pais)

    #Funcion para mostrar datos de los vinos. 
    def __str__(self):
        #return f"\nNombre de Vino: {self.nombre}, \nVarietal: {self.varietales}, \nBodega: {self.bodega.nombre},  \n{self.bodega.region_vitivinicola}, {self.bodega.region_vitivinicola.provincia.pais}, \nPrecio: {self.precio_ARS}" 
        
        #Esta opcion es mejor, ya q muestra todos los datos de los vinos posta, pero es media raringa.
        atributos = "\n".join(f"{key.capitalize():<10}: {value}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}:\n{atributos}" 
