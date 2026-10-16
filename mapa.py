import random
from colorama import Fore
from elemento_mapa import ElementoMapa

mapa_base = ['░░░░░░░░░░',
             '░        ░',
             '░░░░░░░░░░']

class Mapa:
    def __init__(self, jugador):
        self.jugador = jugador
        self.paredes = []
        self.elementos = []
        self.monstruos = []
        self.fila_ini = 6
        self.col_ini = 2
        self.fila_fin = 24
        self.col_fin = 118
        self.mensaje = ""
        self.activo = True

        # Guarda las paredes del mapa

        def cargar_paredes(self):
            for fila in range(len(mapa_base)):
                for col in range(len(mapa_base[fila])):
                    if mapa_base[fila][col] == '░':
                        r = fila + self.fila_ini
                        c = col + self.col_ini
                        self.paredes.append((r, c))

        def obtener_elemento(self, r, c):
            for elemento in self.elementos:
                if elemento.r == r and elemento.c == c:
                    return elemento
            return None

