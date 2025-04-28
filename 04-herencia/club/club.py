"""Club de deportistas"""

from deportista import Deportista, Futbolista, Tenista


class Club:
    def __init__(self):
        self.__socios = []
        self.__prox_num_socio = 0

    def get_prox_num_socio(self) -> int:
        self.__prox_num_socio += 1
        return self.__prox_num_socio

    @classmethod
    def set_cuota_base(cls, nuevo_valor):
        Deportista.set_cuota_base(nuevo_valor)

    def agregar_socio(self, nuevo_socio):
        nuevo_socio.set_numero_socio(self.get_prox_num_socio())
        self.__socios.append(nuevo_socio)

    def get_total_mensual_de_cuotas(self) -> float:
        total_mensual_cuotas = 0
        for socio in self.__socios:
            total_mensual_cuotas += socio.get_cuota_mensual()

        return total_mensual_cuotas

    def listar_planilla_socios(self):
        for socio in self.__socios:
            print(socio)


def main():
    club = Club()
    vilas = Tenista(4)
    messi = Futbolista(7)
    club.agregar_socio(vilas)
    club.agregar_socio(messi)
    club.listar_planilla_socios()

    print(club.get_total_mensual_de_cuotas())
    club.set_cuota_base(500)

    club.listar_planilla_socios()
    print(club.get_total_mensual_de_cuotas())


if __name__ == "__main__":
    main()
