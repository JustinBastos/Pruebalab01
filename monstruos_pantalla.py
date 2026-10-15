import random
from colorama import Fore, Style


class monstruos_pantalla:
  

    def posicion_libre(self, r, c):
       
        if (r, c) in self.paredes:
            return False

        
        if not (
            self.fila_ini <= r <= self.fila_fin
            and self.col_ini <= c <= self.col_fin
        ):
            return False

        
        for elemento in self.elementos:
            if elemento.r == r and elemento.c == c:
                return False

            for monstruo in self.monstruos:
                if monstruo.r == r and monstruo.c == c:
                     return False

        if self.jugador.r == r and self.jugador.c == c:
             return True

        return True

 

    def mover_monstruos(self):
        for monstruo in self.monstruos:

            
            print_at(monstruo.r, monstruo.c, " ")

           
            posiciones_libres = []

            for r in range(self.fila_ini, self.fila_fin + 1):
                for c in range(self.col_ini, self.col_fin + 1):

                   
                    if (r, c) == (self.jugador.r, self.jugador.c):
                        posiciones_libres.append((r, c))

                    else:
                        
                        otros_monstruos = [
                            m for m in self.monstruos
                            if m is not monstruo
                        ]

                        if (r, c) in self.paredes:
                            continue

                        if any(
                            e.r == r and e.c == c
                            for e in self.elementos
                        ):
                            continue

                        if any(
                            m.r == r and m.c == c
                            for m in otros_monstruos
                        ):
                            continue

                        posiciones_libres.append((r, c))

           
            if not posiciones_libres:
                monstruo.dibujar()
                continue

            
            nueva_r, nueva_c = random.choice(posiciones_libres)

            monstruo.r = nueva_r
            monstruo.c = nueva_c

           
            monstruo.dibujar()

            
            if (
                monstruo.r == self.jugador.r
                and monstruo.c == self.jugador.c
            ):
                self.jugador.vida = 0
                self.mensaje = "¡Un monstruo te ha atrapado!"

    def dibujar_mapa(self):
        
        marco(
            self.fila_ini - 1,
            self.col_ini - 1,
            self.col_fin - self.col_ini + 3,
            self.fila_fin - self.fila_ini + 3
        )

       
        for r, c in self.paredes:
            print_at(
                r,
                c,
                Fore.WHITE +  "░" + Style.RESET_ALL
            )

       
        for elemento in self.elementos:
            elemento.dibujar()

        # Dibujar los monstruos.
        for monstruo in self.monstruos:
            monstruo.dibujar()

       
        print_at(
            self.jugador.r,
            self.jugador.c,
            Fore.CYAN + "@" + Style.RESET_ALL
        )

    def dibujar_panel(self):
        jugador = self.jugador
        fila_panel = self.fila_fin + 2

       
        print_at(
            fila_panel,
            self.col_ini,
            Fore.CYAN
            + f"Jugador: {jugador.nombre} | "
            + f"Vida: {jugador.vida} | "
            + f"Oro: {jugador.puntos} | "
            + f"Posición: ({jugador.r}, {jugador.c})"
            + Style.RESET_ALL
        )

        
        print_at(
            fila_panel + 1,
            self.col_ini,
            f"Mensaje: {self.mensaje}"
        )

       
        print_at(
            fila_panel + 2,
            self.col_ini,
            "Instrucciones: " \
            "W=Arriba, " \
            "S=Abajo, "
            "A=Izquierda, " \
            "D=Derecha, " \
            "Q=Salir"
        )