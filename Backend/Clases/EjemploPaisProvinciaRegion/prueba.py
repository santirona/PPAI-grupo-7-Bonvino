from clase_pais import Pais
from clase_provincia import Provincia
from clase_region_vitivinicola import RegionVitivinicola

# Crear instancias de País, Provincia y Región Vitivinícola para el primer país
pais_argentina = Pais("Argentina")
provincia_mendoza = Provincia("Mendoza")
region_valle_uco = RegionVitivinicola("Valle de Uco", "Región conocida por sus vinos de alta calidad.")
provincia_san_juan = Provincia("San Juan")
region_valle_tulum = RegionVitivinicola("Valle del Tulum", "Otra importante región vinícola.")

# Establecer relaciones para el primer país
provincia_mendoza.pais = pais_argentina
provincia_san_juan.pais = pais_argentina
pais_argentina.provincias.extend([provincia_mendoza, provincia_san_juan])
provincia_mendoza.regiones.append(region_valle_uco)
provincia_san_juan.regiones.append(region_valle_tulum)
region_valle_uco.provincias.append(provincia_mendoza)
region_valle_tulum.provincias.append(provincia_san_juan)

# Agregar bodegas a las regiones del primer país
region_valle_uco.bodegas.extend(["Bodega A", "Bodega B"])
region_valle_tulum.bodegas.append("Bodega C")

# Crear instancias de País, Provincia y Región Vitivinícola para el segundo país
pais_chile = Pais("Chile")
provincia_valparaiso = Provincia("Valparaíso")
region_casablanca = RegionVitivinicola("Valle de Casablanca", "Región famosa por sus vinos blancos.")
provincia_maule = Provincia("Maule")
region_valle_maule = RegionVitivinicola("Valle del Maule", "Una de las regiones vinícolas más antiguas de Chile.")

# Establecer relaciones para el segundo país
provincia_valparaiso.pais = pais_chile
provincia_maule.pais = pais_chile
pais_chile.provincias.extend([provincia_valparaiso, provincia_maule])
provincia_valparaiso.regiones.append(region_casablanca)
provincia_maule.regiones.append(region_valle_maule)
region_casablanca.provincias.append(provincia_valparaiso)
region_valle_maule.provincias.append(provincia_maule)

# Agregar bodegas a las regiones del segundo país
region_casablanca.bodegas.extend(["Bodega D", "Bodega E"])
region_valle_maule.bodegas.append("Bodega F")

# Probar métodos para ambos países
print(f"Nombre del país 1: {pais_argentina.getNombre()}")
print(f"Número de bodegas en {region_valle_uco.getNombre()}: {region_valle_uco.contarBodegas()}")
print(f"Número de bodegas en {region_valle_tulum.getNombre()}: {region_valle_tulum.contarBodegas()}")
print(f"Número de bodegas en {pais_argentina.getNombre()}: {pais_argentina.contarBodegas()}")
print(f"Nombre del país obtenido desde la región {region_valle_uco.getNombre()}: {region_valle_uco.obtenerPais().getNombre()}")

print(f"Nombre del país 2: {pais_chile.getNombre()}")
print(f"Número de bodegas en {region_casablanca.getNombre()}: {region_casablanca.contarBodegas()}")
print(f"Número de bodegas en {region_valle_maule.getNombre()}: {region_valle_maule.contarBodegas()}")
print(f"Número de bodegas en {pais_chile.getNombre()}: {pais_chile.contarBodegas()}")
print(f"Nombre del país obtenido desde la región {region_casablanca.getNombre()}: {region_casablanca.obtenerPais().getNombre()}")

