function generarRankingVinos() {
    // Imprime un mensaje en la consola
    console.log("Generar ranking de vinos");
    // Muestra una alerta al usuario
    alert("Funcionalidad para generar el ranking de vinos");
    // Redirige la ventana actual a la ruta '/ranking'
    window.location.href = '/ranking'; // Ruta absoluta de la vista 'ranking'
}

function boton2() {
    // Muestra una alerta al usuario
    alert("Funcionalidad del botón 2");
}

function boton3() {
    // Muestra una alerta al usuario
    alert("Funcionalidad del botón 3");
}

function boton4() {
    // Muestra una alerta al usuario
    alert("Funcionalidad del botón 4");
}

//valida la fecha
function validarPeriodo(fechaDesde, fechaHasta){
    if(fechaDesde > fechaHasta){
        alert("La fecha desde no puede ser mayor que la fecha hasta");
        return true;
    } else {
        return false;}
}

function botonBuscar() {
    // Obtiene los valores de los elementos 'fechaDesde' y 'fechaHasta' del documento HTML
    var fechaDesde = document.getElementById("fechaDesde").value;
    var fechaHasta = document.getElementById("fechaHasta").value;

    if(validarPeriodo(fechaDesde, fechaHasta)){
        return;
    };

    // Obtiene el elemento 'tipoResena' del documento HTML
    var tipoResenaElement = document.getElementById("tipoReseña");
    // Obtiene el valor y el texto del elemento seleccionado en 'tipoResena'
    var tipo_resena = tipoResenaElement.value;
    var tipo_resena_texto = tipoResenaElement.selectedOptions[0].text;

    // Obtiene el elemento 'formaVisualizacion' del documento HTML
    var formaVisualizacionElement = document.getElementById("formaVisualizacion");
    // Obtiene el valor y el texto del elemento seleccionado en 'formaVisualizacion'
    var forma_visualizacion = formaVisualizacionElement.value;
    var forma_visualizacion_texto = formaVisualizacionElement.selectedOptions[0].text;

    // Crea una nueva solicitud AJAX
    var xhr = new XMLHttpRequest();
    // Abre una conexión POST hacia la ruta '/ranking' en modo asíncrono}
    xhr.open("POST", "/ranking", true);
    // Configura la cabecera 'Content-Type' de la solicitud
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    // Define la función a ejecutar cuando cambia el estado de la solicitud
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Si la solicitud es exitosa (estado 200), maneja la respuesta del servidor
                var data = JSON.parse(xhr.responseText);
                console.log(data);
            } else {
                // Si hay un error en la solicitud, muestra un mensaje de error en la consola
                console.error("Error en la solicitud:", xhr.status);
            }
        }
    };

    // Construye una cadena de consulta con los datos del formulario
    var params = "fechaDesde=" + encodeURIComponent(fechaDesde) +
                 "&fechaHasta=" + encodeURIComponent(fechaHasta) +
                 "&tipo_resena=" + encodeURIComponent(tipo_resena) +
                 "&tipo_resena_texto=" + encodeURIComponent(tipo_resena_texto) +
                 "&formaVisualizacion=" + encodeURIComponent(forma_visualizacion) +
                 "&forma_visualizacion_texto=" + encodeURIComponent(forma_visualizacion_texto);

    // Imprime en la consola los parámetros enviados en la solicitud
    console.log(params);
    // Envía la solicitud AJAX con los parámetros construidos
    xhr.send(params);
}


function botonFinCU(){
    // Muestra una alerta al usuario
    alert("Funcionalidad del botón Fin de CU");
    document.getElementById("fechaDesde").value = "";
    document.getElementById("fechaHasta").value = "";
    document.getElementById("tipoReseña").value = "";
    document.getElementById("formaVisualizacion").value = "";
}
