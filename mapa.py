import random
from colorama import Fore
from elemento_mapa import ElementoMapa

# Laberinto de prueba (cada texto es una fila). Lo definitivo se acuerda con el grupo.
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
