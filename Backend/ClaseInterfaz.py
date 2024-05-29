from flask import Flask, render_template, request, jsonify
from ClaseGestorRankingVino import GestorRankingVino

class ClaseInterfaz:
    def __init__(self):
        self.app = Flask(__name__)
        self.gestor_ranking_vino = GestorRankingVino()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/ranking', methods=['GET', 'POST'])
        def ranking():
            if request.method == 'POST':
                try:
                    fecha_desde = request.form['fechaDesde']
                    fecha_hasta = request.form['fechaHasta']
                    tipo_resena_texto = request.form['tipo_resena_texto']
                    forma_visualizacion_texto = request.form['forma_visualizacion_texto']

                    # Procesar los datos obtenidos del formulario
                    #print(f"Datos del formulario recibidos en ClaseInterfaz:\n  Fecha desde: {fecha_desde}\n  Fecha hasta: {fecha_hasta}\n  Tipo reseña: {tipo_resena_texto}\n  Forma visualización: {forma_visualizacion_texto}")

                    # Llama al método de GestorRankingVino para procesar los datos
                    self.gestor_ranking_vino.procesar_datos_formulario(fecha_desde, fecha_hasta, tipo_resena_texto, forma_visualizacion_texto)

                    # Devolver una respuesta JSON indicando que los datos del formulario fueron recibidos correctamente
                    return jsonify({'message': 'Datos del formulario recibidos correctamente!'})
                except KeyError as e:
                    # Manejar el caso de que falte algún campo en el formulario
                    print(f"Error: Falta el campo del formulario '{e.args[0]}'")
                    return jsonify({'error': 'Faltan datos del formulario'}), 400  # Devolver una respuesta de error indicando que faltan datos, con código de estado 400 (Bad Request)

            return render_template('ranking.html')

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    interfaz = ClaseInterfaz()
    interfaz.run()

    