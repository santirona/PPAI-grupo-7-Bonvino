from clase_vino import Vino

class Resena:
    def __init__(self, comentario, es_premium, fecha_resena, puntaje):
        self.comentario = comentario
        self.es_premium = es_premium
        self.fecha_resena = fecha_resena
        self.puntaje = puntaje
        self.Vino = Vino

    def esPremium(self):
        return self.es_premium

    def getPuntaje(self):
        return self.puntaje
    
    def sosDeEnofilo(self):
        # Devuelve True si la reseña no es premium ni de sommelier
        return not (self.es_premium or self.sosDeSommelier())

    def sosDePeriodo(self, fecha_desde, fecha_hasta):
        # Devuelve True si la fecha de la reseña pertenece o no a un periodo de fechas
        return (self.fecha_resena is not None and
                fecha_desde is not None and
                fecha_hasta is not None and
                self.fecha_resena >= fecha_desde and
                self.fecha_resena <= fecha_hasta)

    def sosDeSommelier(self):
        # Devuelve Solo si la reseña es premium y tiene fecha de resena
        return self.es_premium and self.fecha_resena is not None
    

"""
    Pruebas sin Vino funciona bien
    prueba_resena = Resena('Me encanta este vino', False, '2020-01-01', 8)
    print(prueba_resena.sosDeEnofilo()) # True
    print(prueba_resena.sosDeSommelier()) # False
    print(prueba_resena.sosDePeriodo('2019-01-01', '2020-01-01')) 
"""
