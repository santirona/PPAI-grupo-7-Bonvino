from flask import Flask, render_template, request, jsonify # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ranking', methods=['GET', 'POST'])
def ranking():
    if request.method == 'POST':
        try:
            fecha_desde = request.form['fechaDesde']
            fecha_hasta = request.form['fechaHasta']
            tipo_resena_texto = request.form['tipo_resena_texto']
            forma_visualizacion_texto = request.form['forma_visualizacion_texto']

            # Procesar los datos
            print(f"Datos del formulario:\n  Fecha desde: {fecha_desde}\n  Fecha hasta: {fecha_hasta}\n  Tipo reseña: {tipo_resena_texto}\n  Forma visualización: {forma_visualizacion_texto}")

            # Devolver una respuesta de éxito
            return jsonify({'message': 'Datos del formulario recibidos correctamente!'})
        except KeyError as e:
            # Manejar la falta de datos en el formulario
            print(f"Error: Falta el campo del formulario '{e.args[0]}'")
            return jsonify({'error': 'Faltan datos del formulario'}), 400  # Bad request

    return render_template('ranking.html')

if __name__ == '__main__':
    app.run(debug=True)

