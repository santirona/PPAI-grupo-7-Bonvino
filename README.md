# PPAI-grupo-7-Bonvino


# Proyecto de Ranking de Vinos

## Objetivo del Proyecto

El objetivo de este proyecto es crear una aplicación web que permita a los usuarios consultar un ranking de vinos basándose en diferentes criterios de reseñas y fechas. La aplicación recibe datos de entrada del usuario, realiza un procesamiento de estos datos y devuelve una respuesta que muestra el ranking de los vinos según las preferencias seleccionadas.

## Alcance del Proyecto

Hasta el momento, el proyecto permite:
- Ingresar fechas de inicio y fin para filtrar las reseñas.
- Seleccionar el tipo de reseña (normales, de sommelier, de amigos).
- Elegir la forma de visualización del resultado (PDF, Excel, mostrar en otra página).
- Enviar estos datos al servidor utilizando AJAX para recibir una respuesta en formato JSON.

## Herramientas Utilizadas

- **Flask**: Un microframework de Python para desarrollar aplicaciones web.
- **HTML/CSS**: Para la estructura y estilo de la página web.
- **JavaScript (AJAX)**: Para enviar datos al servidor sin recargar la página.
- **Bootstrap**: Un framework CSS para el diseño responsive.

## Estructura del Proyecto

### Archivos Principales

1. **app.py**: 
    - El archivo principal de la aplicación Flask.
    - Define las rutas y maneja las solicitudes HTTP.
    - Procesa los datos enviados desde el formulario y devuelve una respuesta en formato JSON.

2. **templates/index.html**: 
    - La página principal de la aplicación.
    - Muestra el formulario de entrada donde los usuarios pueden seleccionar las fechas, tipo de reseña y forma de visualización.

3. **static/js/script.js**: 
    - Contiene el código JavaScript para manejar el envío del formulario utilizando AJAX.
    - Envía los datos del formulario al servidor y maneja la respuesta.

### Funcionamiento del Código

#### app.py

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ranking', methods=['POST'])
def ranking():
    try:
        fecha_desde = request.form['fechaDesde']
        fecha_hasta = request.form['fechaHasta']
        tipo_resena_texto = request.form['tipo_resena_texto']
        forma_visualizacion_texto = request.form['forma_visualizacion_texto']

        print(f"Datos del formulario:\n  Fecha desde: {fecha_desde}\n  Fecha hasta: {fecha_hasta}\n  Tipo reseña: {tipo_resena_texto}\n  Forma visualización: {forma_visualizacion_texto}")

        return jsonify({'message': 'Datos del formulario recibidos correctamente!'})
    except KeyError as e:
        print(f"Error: Missing form field '{e.args[0]}'")
        return jsonify({'error': 'Faltan datos del formulario'}), 400

if __name__ == '__main__':
    app.run(debug=True)


#### funcionalidad javascript importante

```javascript
function botonBuscar() {
    var fechaDesde = document.getElementById("fechaDesde").value;
    var fechaHasta = document.getElementById("fechaHasta").value;
    var tipo_resena = document.getElementById("tipoReseña").value;
    var forma_visualizacion = document.getElementById("formaVisualizacion").value;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/ranking", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                console.log(data);
            } else {
                console.error("Error en la solicitud:", xhr.status);
            }
        }
    };
    var params = `fechaDesde=${fechaDesde}&fechaHasta=${fechaHasta}&tipo_resena=${tipo_resena}&forma_visualizacion=${forma_visualizacion}&tipo_resena_texto=${encodeURIComponent(tipo_resena)}&forma_visualizacion_texto=${encodeURIComponent(forma_visualizacion)}`;
    xhr.send(params);
}

## Explicación del Código

### Flask (app.py):

- **Flask**: Se crea una instancia de la aplicación Flask.
- **Rutas**: Se define la ruta principal ('/') que renderiza el template `index.html` y la ruta '/ranking' que maneja la solicitud POST.
- **Manejo de datos**: En la ruta '/ranking', se extraen los datos del formulario, se procesan y se imprime la información recibida.

### HTML (index.html):

- **Formularios**: Se crea un formulario HTML con campos para seleccionar las fechas, tipo de reseña y forma de visualización.
- **Botón de confirmación**: Al presionar el botón, se llama a la función `botonBuscar()` definida en el archivo JavaScript.

### JavaScript (script.js):

- **AJAX**: Se utiliza `XMLHttpRequest` para enviar los datos del formulario al servidor Flask sin recargar la página.
- **Manejo de respuesta**: Se procesa la respuesta del servidor y se muestra en la consola.

## Bibliografía

Para entender mejor el código y las tecnologías utilizadas, se recomienda consultar los siguientes recursos:

1. [Documentación de Flask](https://flask.palletsprojects.com/en/2.3.x/)
2. [Introducción a HTML](https://developer.mozilla.org/es/docs/Learn/HTML/Introduction_to_HTML)
3. [Introducción a CSS](https://developer.mozilla.org/es/docs/Learn/CSS/First_steps)
4. [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
5. [AJAX - MDN Web Docs](https://developer.mozilla.org/es/docs/Web/Guide/AJAX)
6. [XMLHttpRequest - MDN Web Docs](https://developer.mozilla.org/es/docs/Web/API/XMLHttpRequest)
