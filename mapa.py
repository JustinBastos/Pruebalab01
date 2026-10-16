from colorama import Fore, Style
from posicion import print_at


def leer_tecla():
    tecla = input("Moverse (W=Arriba, S=Abajo, A=Izquierda, D=Derecha, Q=Salir): ")
    return tecla.strip().upper()


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



    def hay_pared(self, r, c):
        if r < self.fila_ini or r > self.fila_fin:
            return True
        if c < self.col_ini or c > self.col_fin:
            return True
        if (r, c) in self.paredes:
            return True
        return False

    def mover_jugador(self, tecla):
        movimientos = {'W': (-1, 0), 'S': (1, 0), 'A': (0, -1), 'D': (0, 1)}

        if tecla not in movimientos:
            return False

        dfila, dcolumna = movimientos[tecla]
        nueva_fila = self.jugador.r + dfila
        nueva_col = self.jugador.c + dcolumna

        if self.hay_pared(nueva_fila, nueva_col):
            self.mensaje = "¡Atención! No puedes atravesar la pared (░)."
            return False

        print_at(self.jugador.r, self.jugador.c, " ")
        self.jugador.mover(nueva_fila, nueva_col)
        print_at(nueva_fila, nueva_col, Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)
        self.mensaje = ""
        return True
