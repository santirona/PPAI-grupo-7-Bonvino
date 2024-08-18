class Resena:
    def __init__(self, comentario, es_premium, fecha_resena, puntaje, vino):
        self.comentario = comentario
        self.es_premium = es_premium
        self.fecha_resena = fecha_resena
        self.puntaje = puntaje
        self.vino = vino

    def getComentario(self):
        return self.comentario
    
    def esPremium(self):
        # Devuelve True si la reseña es premium, False en caso contrario.
        return self.es_premium

    def getPuntaje(self):
        # Devuelve el puntaje de la reseña.
        return self.puntaje
    
    def sosDeEnofilo(self):
        # Devuelve True si la reseña no es premium ni de sommelier, False en caso contrario.
        return not (self.es_premium or self.sosDeSommelier())

    def sosDePeriodo(self, fecha_desde, fecha_hasta):
        # Devuelve True si la fecha de la reseña pertenece a un periodo de fechas, False en caso contrario.
        return (self.fecha_resena is not None and
                fecha_desde is not None and
                fecha_hasta is not None and
                self.fecha_resena >= fecha_desde and
                self.fecha_resena <= fecha_hasta)

    def sosDeSommelier(self):
        # Devuelve True si la reseña es premium y tiene fecha de reseña, False en caso contrario.
        return self.es_premium and self.fecha_resena is not None
    
    def __str__(self):
        return f"Comentario: {self.comentario}, Es Premium: {self.es_premium}, {self.fecha_resena}, {self.puntaje}, {self.vino}"
