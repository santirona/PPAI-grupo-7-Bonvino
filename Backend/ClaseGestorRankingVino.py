""" from flask import Flask, render_template, request, jsonify # type: ignore

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

@app.route('/')  # Define una ruta para la página principal
def index():
    return render_template('index.html')  # Renderiza el template index.html al acceder a la ruta /

@app.route('/ranking', methods=['GET', 'POST'])  # Define una ruta para la página de ranking, acepta tanto GET como POST
def ranking():
    if request.method == 'POST':  # Si la solicitud es de tipo POST
        try:
            fecha_desde = request.form['fechaDesde']  # Obtiene el valor del campo 'fechaDesde' del formulario
            fecha_hasta = request.form['fechaHasta']  # Obtiene el valor del campo 'fechaHasta' del formulario
            tipo_resena_texto = request.form['tipo_resena_texto']  # Obtiene el valor del campo 'tipo_resena_texto' del formulario
            forma_visualizacion_texto = request.form['forma_visualizacion_texto']  # Obtiene el valor del campo 'forma_visualizacion_texto' del formulario

            # Procesar los datos obtenidos del formulario
            print(f"Datos del formulario:\n  Fecha desde: {fecha_desde}\n  Fecha hasta: {fecha_hasta}\n  Tipo reseña: {tipo_resena_texto}\n  Forma visualización: {forma_visualizacion_texto}")

            # Devolver una respuesta JSON indicando que los datos del formulario fueron recibidos correctamente
            return jsonify({'message': 'Datos del formulario recibidos correctamente!'})
        except KeyError as e:
            # Manejar el caso de que falte algún campo en el formulario
            print(f"Error: Falta el campo del formulario '{e.args[0]}'")
            return jsonify({'error': 'Faltan datos del formulario'}), 400  # Devolver una respuesta de error indicando que faltan datos, con código de estado 400 (Bad Request)

    return render_template('ranking.html')  # Si la solicitud es de tipo GET, renderiza el template ranking.html

if __name__ == '__main__':
    app.run(debug=True)  # Inicia el servidor de desarrollo de Flask en modo debug si se ejecuta este archivo directamente """
from vinosMemori import get_vinos
from Clases.clase_vino import Vino
from flask import Flask, render_template, request, jsonify # type: ignore
import json
import os

class GestorRankingVino:
    def __init__(self, app):
        self.app = app
        self.setup_routes()
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

    def calcularPuntajeDeSommelierEnPeriodo(self):
        for vino in self.vinosQueCumplenFiltros: 
            vino.calcularPuntajeDeSommelierEnPeriodo(self.fechaDesde, self.fechaHasta)
            
        

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
        

    def setup_routes(self):
        @self.app.route('/')
        def index_page():
            return render_template('index.html')
        @self.app.route('/ranking', methods=['GET', 'POST'])
        def ranking_page():
            if request.method == 'POST':
                try:
                    fecha_desde = request.form['fechaDesde']
                    fecha_hasta = request.form['fechaHasta']
                    tipo_resena_texto = request.form['tipo_resena_texto']
                    forma_visualizacion_texto = request.form['forma_visualizacion_texto']

                    # Procesar los datos obtenidos del formulario
                    print(f"Datos del formulario:\n  Fecha desde: {fecha_desde}\n  Fecha hasta: {fecha_hasta}\n  Tipo reseña: {tipo_resena_texto}\n  Forma visualización: {forma_visualizacion_texto}")

                    # Devolver una respuesta JSON indicando que los datos del formulario fueron recibidos correctamente
                    return jsonify({
                        'message': 'Datos del formulario recibidos correctamente!',
                        'fecha_desde': fecha_desde,
                        'fecha_hasta': fecha_hasta
                    })

                except KeyError as e:
                    # Manejar el caso de que falte algún campo en el formulario
                    print(f"Error: Falta el campo del formulario '{e.args[0]}'")
                    return jsonify({'error': 'Faltan datos del formulario'}), 400  # Devolver una respuesta de error indicando que faltan datos, con código de estado 400 (Bad Request)

            return render_template('ranking.html')

    

# Crear la instancia de Flask
app = Flask(__name__)

# Crear la instancia de GestorRankingVino y pasarle la aplicación Flask
gestor = GestorRankingVino(app)



if __name__ == '__main__':
    app.run(debug=True)  # Inicia el servidor de desarrollo de Flask en modo debug si se ejecuta este archivo directamente