from nave import Bombardero, BombarderoBlindado, Caza, Nave


class Artilugio(Nave):
    def __init__(self, nave: Nave) -> None:
        self.__nave = nave

    @property
    def nave(self) -> Nave:
        return self.__nave

    @property
    def danio(self):
        return self.__nave.danio

    @danio.setter
    def danio(self, d):
        self.__nave.danio = d

    @property
    def nombre(self):
        return self.__nave.nombre

    @property
    def salud(self):
        return self.__nave.salud

    @salud.setter
    def salud(self, s):
        self.__nave.salud = s

    def atacar(self, otra):
        self.nave.atacar(otra)


class ArtilugioBlindado(Artilugio):
    def recibir_danio(self, atacante: Nave):
        danio_reducido = atacante.danio * 0.8
        self.nave.salud -= danio_reducido


class ArtilugioCamuflado(Artilugio):
    def __init__(self, nave: Nave):
        super().__init__(nave)
        self.__ataques_esquivados = 0

    def esquivar(self) -> bool:
        """Tiene un 30% de probabilidad de esquivar el ataque."""
        import random

        return random.random() < 0.3

    def recibir_danio(self, atacante: "Nave") -> None:
        # puede esquivar el ataque
        if self.esquivar():
            self.__ataques_esquivados += 1
            return  # esqivó, no recibe daño
        self.salud -= atacante.danio
        if self.salud < 0:
            self.salud = 0

    def estado(self) -> str:
        return (
            f"{self.nave.estado()} -> "
            f"Ataques esquivados: {self.__ataques_esquivados}"
        )


class ArtilugioRecargado(Artilugio):
    def atacar(self, otra):
        self.danio = self.danio * 1.25
        self.nave.atacar(otra)


def main():
    cazita = Caza("Furtivo")
    bombita = BombarderoBlindado("Bombardin")

    bombin = Bombardero("SuperBomba")
    bombin_blindado = ArtilugioBlindado(bombin)
    cazita.atacar(bombin_blindado)

    cazita.atacar(bombita)
    print(bombita.estado())
    print(bombin_blindado.estado())

    caza_blindado = ArtilugioCamuflado(Caza("Caza-Camuflado"))
    cazita.atacar(caza_blindado)
    print(caza_blindado.estado())

    super_caza = ArtilugioBlindado(ArtilugioCamuflado(Caza("Sigilo")))
    cazita.atacar(super_caza)
    super_caza.atacar(cazita)
    print(super_caza.estado())
    print(cazita.estado())

    cazita_plus = ArtilugioRecargado(cazita)
    cazita_plus.atacar(bombin_blindado)
    print(bombin_blindado.estado())
    super_caza_plus = ArtilugioRecargado(super_caza)
    cazita.atacar(super_caza_plus)


if __name__ == "__main__":
    main()
