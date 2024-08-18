import json
from Clases.clase_resena import Resena
from Clases.clase_pais import Pais
from Clases.clase_provincia import Provincia
from Clases.clase_bodega import Bodega
from Clases.clase_vino import Vino
from Clases.clase_region_vitivinicola import RegionVitivinicola
from Clases.clase_varietal import Varietal

def get_vinos():
    
    vinos = []
    
    vino1 = Vino(
        anada=2020,
        fecha_actualizacion="2024-05-01",
        imagen_etiqueta="imagen1.jpg",
        nombre="Vino Ejemplo 1",
        nota_de_cata_bodega="Aromas frutales con notas a madera",
        precio_ARS=1500,
        bodega=Bodega(
            coordenadasUbicacion="34.6037,-58.3816",
            descripcion="Una bodega histórica",
            fechaUltimaActualizacion="2024-05-01",
            historia="Fundada en 1920",
            nombre="Bodega Ejemplo",
            periodoActualizacion="2024-05-01",
            region_vitivinicola=RegionVitivinicola(
                nombre="Region Vitivinicola Ejemplo",
                descripcion="Una región conhecida por sus vinos tintos",
                provincia=Provincia(
                    nombre="Provincia Ejemplo",
                    pais=Pais(nombre="Pais Ejemplo")
                )
            )
        ),
        varietales=[
            Varietal(descripcion="Malbec", porcentaje_composicion=100)
        ],
    )

    resena1 = Resena(
        comentario="Me encanta este vino",
        es_premium=True,
        fecha_resena="2020-01-01",
        puntaje=8,
        vino=vino1
    )
    resena2 = Resena(
        comentario="No me encanta este vino",
        es_premium=True,
        fecha_resena="2020-01-01",
        puntaje=2,
        vino=vino1
    )

    vino2 = Vino(
        anada=2021,
        fecha_actualizacion="2024-05-01",
        imagen_etiqueta="imagen2.jpg",
        nombre="Vino Ejemplo 2",
        nota_de_cata_bodega="Aromas florales con notas a frutas",
        precio_ARS=2000,
        bodega=Bodega(
            coordenadasUbicacion="34.6037,-58.3816",
            descripcion="Una bodega moderna",
            fechaUltimaActualizacion="2024-05-01",
            historia="Fundada en 1950",
            nombre="Bodega Ejemplo 2",
            periodoActualizacion="2024-05-01",
            region_vitivinicola=RegionVitivinicola(
                nombre="Region Vitivinicola Ejemplo 2",
                descripcion="Una región conocida por sus vinos blancos",
                provincia=Provincia(
                    nombre="Provincia Ejemplo 2",
                    pais=Pais(nombre="Pais Ejemplo 2")
                )
            )
        ),
        varietales=[
            Varietal(descripcion="Chardonnay", porcentaje_composicion=100)
        ],
    )

    resena3 = Resena(
        comentario="Me encanta este vino",
        es_premium=True,
        fecha_resena="2020-01-01",
        puntaje=9,
        vino=vino2
    )
    resena4 = Resena(
        comentario="No me gusta este vino",
        es_premium=False,
        fecha_resena="2020-02-01",
        puntaje=6,
        vino=vino2
    )

    vino3 = Vino(
        anada=2022,
        fecha_actualizacion="2024-05-01",
        imagen_etiqueta="imagen3.jpg",
        nombre="Vino Ejemplo 3",
        nota_de_cata_bodega="Aromas a frutas y flores",
        precio_ARS=1800,
        bodega=Bodega(
            coordenadasUbicacion="34.6037,-58.3816",
            descripcion="Una bodega histórica",
            fechaUltimaActualizacion="2024-05-01",
            historia="Fundada en 1920",
            nombre="Bodega Ejemplo 3",
            periodoActualizacion="2024-05-01",
            region_vitivinicola=RegionVitivinicola(
                nombre="Region Vitivinicola Ejemplo 3",
                descripcion="Una región conocida por sus vinos tintos",
                provincia=Provincia(
                    nombre="Provincia Ejemplo 3",
                    pais=Pais(nombre="Pais Ejemplo 3")
                )
            )
        ),
        varietales=[
            Varietal(descripcion="Malbec", porcentaje_composicion=100)
        ],
    )

    resena5 = Resena(
        comentario="Me encanta este vino",
        es_premium=False,
        fecha_resena="2020-01-01",
        puntaje=8,
        vino=vino3
    )
    resena6 = Resena(
        comentario="No me gusta este vino",
        es_premium=False,
        fecha_resena= "2020-02-01",
        puntaje=6,
        vino=vino3
    )

    vino1.resenas.append(resena1)
    vino1.resenas.append(resena2)

    vino2.resenas.append(resena3)
    vino2.resenas.append(resena4)

    vino3.resenas.append(resena5)
    vino3.resenas.append(resena6)

    vinos = [vino1, vino2, vino3]
    
    return vinos

def crear_vinos_desde_json(json_data):
    vinos = []
    
    for vino_data in json_data['vinos']:
        # Crear el objeto Pais
        pais = Pais(nombre=vino_data['bodega']['region_vitivinicola']['provincia']['pais']['nombre'])
        
        # Crear el objeto Provincia
        provincia = Provincia(nombre=vino_data['bodega']['region_vitivinicola']['provincia']['nombre'], pais=pais)
        
        # Crear el objeto RegionVitivinicola
        region_vitivinicola = RegionVitivinicola(
            nombre=vino_data['bodega']['region_vitivinicola']['nombre'],
            descripcion=vino_data['bodega']['region_vitivinicola']['descripcion'],
            provincia=provincia
        )
        
        # Crear el objeto Bodega
        bodega = Bodega(
            coordenadasUbicacion=vino_data['bodega']['coordenadasUbicacion'],
            descripcion=vino_data['bodega']['descripcion'],
            fechaUltimaActualizacion=vino_data['bodega']['fechaUltimaActualizacion'],
            historia=vino_data['bodega']['historia'],
            nombre=vino_data['bodega']['nombre'],
            periodoActualizacion=vino_data['bodega']['periodoActualizacion'],
            region_vitivinicola=region_vitivinicola
        )
        
        # Crear los objetos Varietal
        varietales = [
            Varietal(descripcion=varietal['descripcion'], porcentaje_composicion=varietal['porcentaje_composicion'])
            for varietal in vino_data['varietales']
        ]
        
        # Crear el objeto Vino
        vino = Vino(
            anada=vino_data['anada'],
            fecha_actualizacion=vino_data['fecha_actualizacion'],
            imagen_etiqueta=vino_data['imagen_etiqueta'],
            nombre=vino_data['nombre'],
            nota_de_cata_bodega=vino_data['nota_de_cata_bodega'],
            precio_ARS=vino_data['precio_ARS'],
            bodega=bodega,
            varietales=varietales
        )
        
        # Crear las Resenas asociadas a este Vino
        resenas = [
            Resena(
                comentario=resena['comentario'],
                es_premium=resena['es_premium'],
                fecha_resena=resena['fecha_resena'],
                puntaje=resena['puntaje'],
                vino=vino
            )
            for resena in vino_data['resenas']
        ]
        
        # Añadir las resenas al vino
        vino.resenas = resenas
        
        # Añadir el vino a la lista
        vinos.append(vino)
    
    return vinos

ruta_json = 'Data/vinos.json'
with open(ruta_json, 'r') as file:
    json_data = json.load(file)
    
vinos = crear_vinos_desde_json(json_data)

print(vinos[0].resenas[0].comentario)