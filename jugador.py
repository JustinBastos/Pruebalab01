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



def recibir_dano(self, cantidad):
        self.vida = self.vida - cantidad
        if self.vida < 0:
            self.vida = 0

    def curar(self, cantidad):
        self.vida = self.vida + cantidad
        if self.vida > self.vida_max:
            self.vida = self.vida_max



def sumar_puntos(self, cantidad):
        self.puntos = self.puntos + cantidad

    def esta_vivo(self):
        return self.vida > 0
