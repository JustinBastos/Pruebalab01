# ----------------------------------------------------------
# Clase ElementoMapa: tesoros, pociones, trampas y monstruos
# ----------------------------------------------------------
from colorama import Style
from posicion import print_at


class ElementoMapa:

    # ------------------------------------------------------
    # Constructor
    # ------------------------------------------------------
    def __init__(self, tipo, simbolo, color, r, c, valor):
        self.tipo = tipo
        self.simbolo = simbolo
        self.color = color
        self.r = r
        self.c = c
        self.valor = valor

    # ------------------------------------------------------
    # Dibuja el elemento en pantalla
    # ------------------------------------------------------
    def dibujar(self):
        print_at(self.r, self.c, self.color + self.simbolo + Style.RESET_ALL)