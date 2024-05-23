function generarRankingVinos() {
    alert("Funcionalidad para generar el ranking de vinos");
    window.location.href = 'ranking.html';
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

function botonBuscar(){
    /* alert("Funcionalidad del botón buscar"); */
    //Tomar los datos del formulario
    var fechaDesde = document.getElementById("fechaDesde").value;
    var fechaHasta = document.getElementById("fechaHasta").value;
    //Mostrarlos por consola del navegador
    console.log("Fecha desde: " + fechaDesde);
    console.log("Fecha hasta: " + fechaHasta);
    //Ahora tenemos que validar que las fechas sean validas, son validas si la fechaHasta es mayor a la fechaDesde y ambas estan en formato de fecha.
    if (Date.parse(fechaDesde) > Date.parse(fechaHasta)){
        alert("La fecha desde no puede ser mayor que la fecha hasta.");
        //Si estamos en este flujo se valido el periodo con exito
        
    }

}