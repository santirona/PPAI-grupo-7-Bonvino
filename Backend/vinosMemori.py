from Clases.clase_resena import Resena
from Clases.clase_pais import Pais
from Clases.clase_provincia import Provincia
from Clases.clase_bodega import Bodega
from Clases.clase_vino import Vino
from Clases.clase_region_vitivinicola import RegionVitivinicola
from Clases.clase_varietal import Varietal

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
    puntaje=8,
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
    puntaje=8,
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
    es_premium=True,
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



print(vino1.resenas[0].sosDeSommelier())
print(vino2.getResenas())
print(vino3.getResenas())