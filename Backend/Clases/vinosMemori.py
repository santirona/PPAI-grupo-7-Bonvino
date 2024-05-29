from clase_resena import Resena
from clase_pais import Pais
from clase_provincia import Provincia
from clase_bodega import Bodega
from clase_vino import Vino
from clase_region_vitivinicola import RegionVitivinicola
from clase_varietal import Varietal

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

vino1.resenas.append(resena1)
vino1.resenas.append(resena2)

print(vino1.getResenas())