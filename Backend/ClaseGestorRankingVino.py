from vinosMemori import get_vinos


class GestorRankingVino:
    def __init__(self):
        self.fechaDesde = None
        self.fechaHasta = None
        self.tipoRankingSeleccionado = None
        self.vinosOrdenados = []
        self.vinosQueCumplenFiltros = []
        self.VinosQueCumplenDatos = []

    def buscarVinosConResenasEnPeriodo(self, vinos): # Función para buscar vinos con reseñas dentro de un período de tiempo determinado
        vinosQueCumplenFiltros = []  # Lista para almacenar vinos que cumplen los filtros
        for vino in vinos:
            if vino.tenesResenaDeTipoEnPeriodo(self.tipoRankingSeleccionado, self.fechaDesde, self.fechaHasta):
                nombre = vino.getNombre()  # Extraer información relevante del vino y almacenar en un diccionario
                precio = vino.getPrecio()
                bodega,nombrePais,regionVitivinicola = vino.buscarinfoBodega()
                varietal = vino.buscarVarietales()
                vino_data = {
                    'vino': vino,  # Almacena la referencia al objeto vino
                    'nombre': nombre,
                    'precio': precio,
                    'bodega': bodega,
                    'regionVitivinicola': regionVitivinicola,
                    'nombrePais': nombrePais,
                    'varietal': varietal,
                    'puntuacion_promedio': 0
                }
                vinosQueCumplenFiltros.append(vino_data)
        self.vinosQueCumplenFiltros = vinosQueCumplenFiltros



    def calcularPuntajeDeSommelierEnPeriodo(self):
        for vino_data in self.vinosQueCumplenFiltros:
            vino = vino_data['vino'] # 'vino' es la referencia al objeto vino
            puntuacion = vino.calcularPuntajeDeSommelierEnPeriodo(self.fechaDesde, self.fechaHasta)
            if puntuacion is not None:  # Verificar si el puntaje es válido
                vino_data['puntuacion_promedio'] = puntuacion

    
    def calcularPuntajeDeNormalesEnPeriodo(self):
        for vino_data in self.vinosQueCumplenFiltros:
            vino = vino_data['vino'] # 'vino' es la referencia al objeto vino
            puntuacion= vino.calcularPuntajeDeNormalesEnPeriodo(self.fechaDesde, self.fechaHasta)
            if puntuacion is not None:  # Verificar si el puntaje es válido
                vino_data['puntuacion_promedio'] = puntuacion

            

    def finCU(self):
        pass

    def opcionGenerarRankingVinos(self):
        pass

    def ordenarVinosPor(self, vinos):
        vinos_ordenados = sorted(vinos, key=lambda vino: vino.resena, reverse=True)
        return vinos_ordenados

    def tomarConfirmacionGenReporte(self):
        pass

    def tomarSelFechaDesdeYHasta(self, fechaDesde, fechaHasta):
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta

    def tomarSelTipoResena(self, tipoResena):
        self.tipoRankingSeleccionado = tipoResena

    def tomarSelTipoVisualizacion(self, tipoVisualizacion):
        pass
    
    def ordenarVinos(self):
        self.vinosOrdenados = sorted(self.vinosQueCumplenFiltros, key=lambda vino_data: vino_data['puntuacion_promedio'], reverse=True)

    # def obtenerDatosDeVinosOrdenados(self):   
    #     for vino in self.vinosOrdenados:
    #         nombre = vino.getNombre()
    #         precio = vino.getPrecio()
    #         regionVitivinicola, nombrePais= vino.bodega.obtenerRegionYPais()
    #         varietal = vino.buscarVarietales()
    #         print('Nombre:',nombre, 'precio:',precio,'regionVitivinicola:', regionVitivinicola,'nombrePais:',nombrePais,'varietal:', varietal)

    def procesar_datos_formulario(self, fecha_desde, fecha_hasta, tipo_resena_texto, forma_visualizacion_texto):
        self.tomarSelFechaDesdeYHasta(fecha_desde, fecha_hasta)
        self.tomarSelTipoResena(tipo_resena_texto)
        self.tomarSelTipoVisualizacion(forma_visualizacion_texto)


        print("Procesado en GestorRankingVino:")
        print(self.fechaDesde)
        print(self.fechaHasta)
        print(self.tipoRankingSeleccionado)
        #print(f"Procesado en GestorRankingVino:\n  Fecha desde: {self.fechaDesde}\n  Fecha hasta: {self.fechaHasta}\n  Tipo reseña: {self.tipoRankingSeleccionado}\n  Forma visualización: {forma_visualizacion_texto}")
        vinos = get_vinos()

        self.buscarVinosConResenasEnPeriodo(vinos)
                 
        if self.tipoRankingSeleccionado == "Reseñas de Sommelier":
            self.calcularPuntajeDeSommelierEnPeriodo()
        elif self.tipoRankingSeleccionado == "Reseñas Normales":
            self.calcularPuntajeDeNormalesEnPeriodo()
        else:
            print("Error: Tipo de visualización no reconocido")


        print()
        print("Vinos ordenados:")
        print()
        self.ordenarVinos()
        for vino_data in self.vinosOrdenados:
            for clave, valor in vino_data.items():
                if clave != 'vino':
                    print(f"{clave}: {valor}")
            print()

    

        