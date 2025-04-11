"""Class Soldado"""

from unidad import Unidad


class Soldado(Unidad):
    def __init__(self, posicion):
        super().__init__(200, 10, posicion)
        self.energia = 100

    def atacar(self, enemigo: Unidad):
        if self.puede_atacar(enemigo):
            self.energia -= 10
            enemigo.recibir_danio(10)

    def puede_atacar(self, enemigo: Unidad) -> bool:
        return (
            super().distancia(enemigo) == 0
            and not enemigo.esta_muerto()
            and self.energia >= 10
        )
