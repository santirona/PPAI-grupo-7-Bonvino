class Provincia:
    def __init__(self, nombre,pais):
        self.nombre = nombre
        self.regiones = []
        self.pais = pais

    def contarRegiones(self):
        return len(self.regiones)

    def mostrarRegiones(self):
        return self.regiones

    def obtenerPais(self):
        return self.pais

    def __str__(self):
        return f"\nNombre Provincia: {self.nombre}"#, Pais de Provincia= {self.pais}"

