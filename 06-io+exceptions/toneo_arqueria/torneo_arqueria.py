"""Torneo de Arquería"""


class LineaMalFormadaException(Exception):
    pass


class ParticipanteInvalidoException(Exception):
    pass


class PuntajeInvalidoException(Exception):
    pass


class ParticipanteDuplicadoException(Exception):
    pass


class Torneo:
    def __init__(self, archivo: str) -> None:
        self.__participantes: dict[int, int] = {}
        self.__cargar_datos(archivo)

    def __cargar_datos(self, archivo: str) -> None:
        validos = (50, 100, 200, 500, 1000)
        with open(archivo, "r") as tiros:
            for cada_linea in tiros:
                datos = cada_linea.strip().split(",")
                try:
                    if len(datos) != 6:
                        raise LineaMalFormadaException()
                    nro_part = int(datos[0])
                    if nro_part in self.__participantes.keys():
                        raise ParticipanteDuplicadoException(datos[0])
                    if nro_part < 100 or nro_part > 999:
                        raise ParticipanteInvalidoException(datos[0])
                    puntaje = 0
                    for i in range(1, 6):
                        if int(datos[i]) not in validos:
                            raise PuntajeInvalidoException()
                        puntaje += int(datos[i])

                    self.__participantes[nro_part] = puntaje

                except LineaMalFormadaException:
                    print("Linea inválida")
                except ValueError:
                    print("Valor no numérico")
                except ParticipanteInvalidoException as e:
                    print("Número de participante fuera de rango: ", e)
                except ParticipanteDuplicadoException as pd:
                    print("Participante duplicado: ", pd)
                except PuntajeInvalidoException:
                    print("Puntaje inválido")
        tiros.close()

    def obtener_podio(self):
        aux: dict[int, list[int]] = {}

        for participante, puntaje in self.__participantes.items():
            if puntaje in aux.keys():
                lp = aux[puntaje]
            else:
                lp = []
            lp.append(participante)
            aux[puntaje] = lp

        ganadores = sorted(aux.keys(), reverse=True)
        ganadores = ganadores[:3]

        print("Primer puesto: ", aux[ganadores[0]], " con: ", ganadores[0])
        print("Segundo puesto: ", aux[ganadores[1]], " con: ", ganadores[1])
        print("Tercer puesto: ", aux[ganadores[2]], " con: ", ganadores[2])


def main():
    try:
        t = Torneo("tiros.csv")
        t.obtener_podio()

    except FileNotFoundError:
        print("Archivo no encontrado")


if __name__ == "__main__":
    main()
