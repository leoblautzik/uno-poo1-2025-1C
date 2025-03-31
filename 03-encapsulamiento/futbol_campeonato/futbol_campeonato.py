import json
import random


class Jugador:
    def __init__(self, goles, infracciones, partidos):
        self.__goles = goles
        self.__infracciones = infracciones
        self.__partidos = partidos

    def es_buen_jugador(self):
        """Retorna True si hizo al menos 10 goles y cometió menos de 5 infracciones."""
        return self.__goles >= 10 and self.__infracciones < 5

    def get_goles(self):
        """Devuelve la cantidad de goles."""
        return self.__goles

    def get_infracciones(self):
        """Devuelve la cantidad de infracciones."""
        return self.__infracciones

    def get_partidos(self):
        """Devuelve la cantidad de partidos jugados."""
        return self.__partidos


class Equipo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__jugadores = [
            Jugador(random.randint(0, 20), random.randint(0, 10), random.randint(1, 20))
            for _ in range(11)
        ]

    def obtener_goles_jugador(self, jugador):
        """Devuelve la cantidad de goles de un jugador."""
        return jugador.get_goles()

    def una_figura(self):
        """Devuelve el número del jugador más goleador entre los buenos jugadores."""
        buenos_jugadores = [
            jugador for jugador in self.__jugadores if jugador.es_buen_jugador()
        ]
        if not buenos_jugadores:
            return None  # No hay buenos jugadores
        return max(buenos_jugadores, key=self.obtener_goles_jugador)

    def juego_sucio(self):
        """Retorna True si todos los jugadores con goles y más de 2 partidos cometieron alguna infracción."""
        jugadores_validos = [
            j for j in self.__jugadores if j.get_goles() > 0 and j.get_partidos() > 2
        ]
        return all(j.get_infracciones() > 0 for j in jugadores_validos)

    def get_nombre(self):
        """Devuelve el nombre del equipo."""
        return self.__nombre

    def get_jugadores(self):
        """Devuelve la lista de jugadores."""
        return self.__jugadores


class Campeonato:
    def __init__(self):
        self.__equipos = [Equipo(f"Equipo {i + 1}") for i in range(10)]

    def equipo_juego_sucio(self):
        """Determina cuál es el equipo que hizo juego sucio."""
        equipos_sucios = [equipo for equipo in self.__equipos if equipo.juego_sucio()]
        return equipos_sucios if equipos_sucios else None

    def guardar_datos(self, archivo="campeonato.json"):
        """Guarda los datos del campeonato en un archivo JSON."""
        datos = {
            equipo.get_nombre(): [
                {
                    "goles": j.get_goles(),
                    "infracciones": j.get_infracciones(),
                    "partidos": j.get_partidos(),
                }
                for j in equipo.get_jugadores()
            ]
            for equipo in self.__equipos
        }
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)

    def mostrar_resultados(self):
        """Muestra los resultados del campeonato."""
        for equipo in self.__equipos:
            figura = equipo.una_figura()
            print(
                f"Equipo: {equipo.get_nombre()} - Figura: {'Sin buenos jugadores' if figura is None else figura.get_goles()}"
            )
        print("\nEquipos con juego sucio:")
        equipos_sucios = self.equipo_juego_sucio()
        if equipos_sucios:
            for equipo in equipos_sucios:
                print(equipo.get_nombre())
        else:
            print("Ningún equipo hizo juego sucio.")


def main():
    campeonato = Campeonato()
    campeonato.mostrar_resultados()
    campeonato.guardar_datos()


if __name__ == "__main__":
    main()
