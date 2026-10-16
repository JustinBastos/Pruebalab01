from jugador import Jugador
from mapa import Mapa

nombre = input("Nombre del jugador: ")
jugador = Jugador(nombre, 7, 3)
juego = Mapa(jugador)
juego.ejecutar()
