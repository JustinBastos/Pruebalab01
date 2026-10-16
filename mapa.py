import random
from colorama import Fore, Style
from elemento_mapa import ElementoMapa
from posicion import print_at

# Laberinto de prueba (cada texto es una fila). Lo definitivo se acuerda con el grupo.
mapa_base = ['░░░░░░░░░░',
             '░        ░',
             '░░░░░░░░░░']


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

    # Guarda las paredes del mapa
    def cargar_paredes(self):
        for fila in range(len(mapa_base)):
            for col in range(len(mapa_base[fila])):
                if mapa_base[fila][col] == '░':
                    r = fila + self.fila_ini
                    c = col + self.col_ini
                    self.paredes.append((r, c))

    # Busca un elemento en esa posicion
    def obtener_elemento(self, r, c):
        for elemento in self.elementos:
            if elemento.r == r and elemento.c == c:
                return elemento
        return None

    # Crea tesoros, pociones, trampas y monstruos
    def cargar_objetos(self):
        datos = [{'tipo': 'tesoro', 'simbolo': '$', 'color': Fore.YELLOW, 'cantidad': 5, 'valor': 50},
                 {'tipo': 'pocion', 'simbolo': '+', 'color': Fore.GREEN, 'cantidad': 3, 'valor': 20},
                 {'tipo': 'trampa', 'simbolo': 'X', 'color': Fore.MAGENTA, 'cantidad': 4, 'valor': 20},
                 {'tipo': 'monstruo', 'simbolo': 'M', 'color': Fore.RED, 'cantidad': 4, 'valor': 0}]

        for dato in datos:
            for i in range(dato['cantidad']):
                libre = False
                while not libre:
                    r = random.randint(self.fila_ini, self.fila_fin)
                    c = random.randint(self.col_ini, self.col_fin)
                    libre = self.posicion_libre(r, c)
                    if r == self.jugador.r and c == self.jugador.c:
                        libre = False
                nuevo = ElementoMapa(dato['tipo'], dato['simbolo'], dato['color'], r, c, dato['valor'])
                if dato['tipo'] == 'monstruo':
                    self.monstruos.append(nuevo)
                else:
                    self.elementos.append(nuevo)

    # Revisa que hay en la posicion del jugador
    def procesar_colision(self):
        elemento = self.obtener_elemento(self.jugador.r, self.jugador.c)
        if elemento != None:
            if elemento.tipo == 'tesoro':
                self.jugador.sumar_puntos(elemento.valor)
                self.jugador.inventario['tesoros'] = self.jugador.inventario.get('tesoros', 0) + 1
                self.mensaje = '¡Encontraste un tesoro!'
            elif elemento.tipo == 'pocion':
                self.jugador.curar(elemento.valor)
                self.jugador.inventario['pociones'] = self.jugador.inventario.get('pociones', 0) + 1
                self.mensaje = '¡Tomaste una poción!'
            elif elemento.tipo == 'trampa':
                self.jugador.recibir_dano(elemento.valor)
                self.mensaje = '¡Caíste en una trampa!'
            self.elementos.remove(elemento)

        for monstruo in self.monstruos:
            if monstruo.r == self.jugador.r and monstruo.c == self.jugador.c:
                self.jugador.vida = 0
                self.mensaje = '¡Un monstruo te atrapó!'

    # Dice si todavia queda algun tesoro
    def quedan_tesoros(self):
        for elemento in self.elementos:
            if elemento.tipo == 'tesoro':
                return True
        return False



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
