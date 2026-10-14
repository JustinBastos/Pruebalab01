class Jugador:
    def __init__(self, nombre, r, c):
        self.nombre = nombre
        self.r = r
        self.c = c
        self.vida = 100
        self.vida_max = 100
        self.puntos = 0
        self.inventario = {}

    def mover(self, r, c):
        self.r = r
        self.c = c
