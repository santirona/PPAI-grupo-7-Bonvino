import json
import os
from Clases.clase_vino import Vino
from Clases.clase_bodega import Bodega
from Clases.clase_resena import Resena

def cargarVinos(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    vinos = []
    for idx, vino_data in enumerate(data['vinos']):
        bodega_data = vino_data['bodega']
        region_data = bodega_data['region']
        provincia_data = region_data['provincia']
        pais_data = provincia_data['pais']
        
        bodega = Bodega(
            coordenadaUbicacion=bodega_data['coordenadasUbicacion'],  # Aquí cambié el nombre del argumento
            descripcion=bodega_data['descripcion'],
            fechaUltimaActualizacion=bodega_data['fechaUltimaActualizacion'],
            historia=bodega_data['historia'],
            nombre=bodega_data['nombre'],
            periodoActualizacion=bodega_data['fechaUltimaActualizacion'],  # Esto asume que periodoActualizacion es igual a fechaUltimaActualizacion
            region_vitivinicola=region_data
        )
        
        vino = Vino(
            id=idx,
            nombre=vino_data['nombre'],
            bodega=bodega,
            provincia=provincia_data['nombre'],
            pais=pais_data['nombre'],
            precio=vino_data['precioARS']
        )
        
        vino.varietales = vino_data['varietal']
        for resena_data in vino_data['reseñas']:
            resena = Resena(
                comentario=resena_data['comentario'],
                es_premium=resena_data['esPremium'],  # Aquí cambié el nombre del argumento
                fecha_resena=resena_data['fechaReseña'],
                puntaje=resena_data['puntaje'],
                vino=vino
            )
            vino.resenas.append(resena)
        vinos.append(vino)
    return vinos

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'vinos.json')
    vinos = cargarVinos(file_path)
    
    for vino in vinos:
        print(vino.obtener_info())
        print("Reseñas:")
        for resena in vino.resenas:
            print(f"  {resena.comentario} - Puntaje: {resena.puntaje}")
        print("\n" + "-"*50 + "\n")
