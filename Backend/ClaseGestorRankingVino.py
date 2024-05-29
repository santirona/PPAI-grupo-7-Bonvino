from vinosMemori import get_vinos
from Clases.clase_vino import Vino


class GestorRankingVino:
    def __init__(self):
        self.fechaDesde = None
        self.fechaHasta = None
        self.tipoRankingSeleccionado = None
        self.vinosOrdenados = []
        self.vinosQueCumplenFiltros = []

    def buscarVinosConResenasEnPeriodo(self, vinos):
        vinosQueCumplenFiltros = []
        for vino in vinos:          
            if vino.tenesResenaDeTipoEnPeriodo(self.tipoRankingSeleccionado, self.fechaDesde, self.fechaHasta):
                vinosQueCumplenFiltros.append(vino)
        self.vinosQueCumplenFiltros = vinosQueCumplenFiltros
        for vino in self.vinosQueCumplenFiltros:
            print(vino.nombre)


    def calcularPuntajeDeSommelierEnPeriodo(self):
        for vino in self.vinosQueCumplenFiltros: 
            vino.calcularPuntajeDeSommelierEnPeriodo(self.fechaDesde, self.fechaHasta)
            
    def calcularPuntajeDeNormalesEnPeriodo(self):
        for vino in self.vinosQueCumplenFiltros: 
            vino.calcularPuntajeDeNormalesEnPeriodo(self.fechaDesde, self.fechaHasta)

    def finCU(self):
        # Implement logic to finalize the control use case
        pass

    def opcionGenerarRankingVinos(self):
        # Implement logic to generate wine ranking options
        pass

    def ordenarVinosPor(self, vinos):
        vinos_ordenados = sorted(vinos, key=lambda vino: vino.resena, reverse=True)
        return vinos_ordenados

    def tomarConfirmacionGenReporte(self):
        # Implement logic to take report generation confirmation
        pass

    def tomarSelFechaDesdeYHasta(self, fechaDesde, fechaHasta):
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta

    def tomarSelTipoResena(self, tipoResena):
        self.tipoRankingSeleccionado = tipoResena

    def tomarSelTipoVisualizacion(self, tipoVisualizacion):
        # Implement logic to set the type of visualization
        pass
    
    def ordenarVinos(self):
        self.vinosOrdenados = sorted(self.vinosQueCumplenFiltros, key=lambda vino: vino.puntuacion_promedio, reverse=True)
    
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
"""         if self.tomarSelTipoResena == "Sommelier":
            self.calcularPuntajeDeSommelierEnPeriodo()
        elif self.tomarSelTipoResena == "Normales":
            self.calcularPuntajeDeNormalesEnPeriodo()
        else:
            print("Error: Tipo de visualización no reconocido") """