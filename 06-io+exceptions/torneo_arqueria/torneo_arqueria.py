"""
Torneo de arquería
"""


class LineaIncorrectaException(Exception):
    pass


class PuntajeInvalidoException(Exception):
    pass


class ParticipanteDuplicadoException(Exception):
    pass


class Torneo:
    def __init__(self) -> None:
        self.participantes: dict[int, int] = {}

    def leer_puntajes(self, tiros) -> None:
        puntos_validos = (1000, 500, 200, 100, 50)
        with open(tiros, "r") as tiros:
            for linea in tiros:
                datos = linea.strip().split(",")
                try:
                    if len(datos) != 6:
                        raise LineaIncorrectaException(datos[0])

                    participante = int(datos[0])
                    if participante in self.participantes.keys():
                        raise ParticipanteDuplicadoException()
                    puntaje = 0
                    for i in range(1, 6):
                        t = int(datos[i])
                        if t not in puntos_validos:
                            raise PuntajeInvalidoException()
                        puntaje += int(datos[i])

                    self.participantes[participante] = puntaje

                except ValueError:
                    print("Valor leído no numérico.")
                except ParticipanteDuplicadoException:
                    print("Participante ya cargado.")
                except PuntajeInvalidoException:
                    print("Puntaje inválido para el  participante: ", participante)
                except LineaIncorrectaException as e:
                    print("Linea mal formada: ", e)

            tiros.close()

    def podio(self):
        aux: dict[int, list[int]] = {}

        for participante, puntaje in self.participantes.items():
            lp = aux.setdefault(puntaje, [])
            lp.append(participante)
            aux[puntaje] = lp

        podio = sorted(aux.keys(), reverse=True)
        podio = podio[:3]
        salida = (
            "Primer puesto: "
            + str(aux[podio[0]])
            + " con "
            + str(podio[0])
            + " puntos. \n"
        )
        salida += (
            "Segundo puesto: "
            + str(aux[podio[1]])
            + " con "
            + str(podio[1])
            + " puntos. \n"
        )
        salida += (
            "Tercer puesto: "
            + str(aux[podio[2]])
            + " con "
            + str(podio[2])
            + " puntos. \n"
        )
        return salida


def main():
    torneo = Torneo()
    torneo.leer_puntajes("tiros.csv")
    print("\nPodio: \n")
    print(torneo.podio())


if __name__ == "__main__":
    main()
