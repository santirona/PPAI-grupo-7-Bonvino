function generarRankingVinos() {
    console.log("Generar ranking de vinos")
    alert("Funcionalidad para generar el ranking de vinos");
    window.location.href = '/ranking'; // Ruta absoluta de la vista 'ranking'
}


function boton2() {
    alert("Funcionalidad del botón 2");
}

function boton3() {
    alert("Funcionalidad del botón 3");
}

function boton4() {
    alert("Funcionalidad del botón 4");
}


function botonBuscar() {
    var fechaDesde = document.getElementById("fechaDesde").value;
    var fechaHasta = document.getElementById("fechaHasta").value;

    var tipoResenaElement = document.getElementById("tipoReseña");
    var tipo_resena = tipoResenaElement.value;
    var tipo_resena_texto = tipoResenaElement.selectedOptions[0].text;

    var formaVisualizacionElement = document.getElementById("formaVisualizacion");
    var forma_visualizacion = formaVisualizacionElement.value;
    var forma_visualizacion_texto = formaVisualizacionElement.selectedOptions[0].text;

    // Realizar la solicitud AJAX al servidor Flask
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/ranking", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Manejar la respuesta del servidor
                var data = JSON.parse(xhr.responseText);
                console.log(data);                
            } else {
                // Manejar errores en la solicitud
                console.error("Error en la solicitud:", xhr.status);
            }
        }
    };

    // Enviar los datos del formulario como cadena de consulta
    var params = "fechaDesde=" + encodeURIComponent(fechaDesde) +
                 "&fechaHasta=" + encodeURIComponent(fechaHasta) +
                 "&tipo_resena=" + encodeURIComponent(tipo_resena) +
                 "&tipo_resena_texto=" + encodeURIComponent(tipo_resena_texto) +
                 "&formaVisualizacion=" + encodeURIComponent(forma_visualizacion) +
                 "&forma_visualizacion_texto=" + encodeURIComponent(forma_visualizacion_texto);

    console.log(params);
    xhr.send(params);
}


