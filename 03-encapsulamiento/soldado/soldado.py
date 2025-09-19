# soldado.py

from __future__ import annotations


class Soldado:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.energia = 100
        self.salud = 200

    def atacar(self, otro: Soldado) -> None:
        """Un soldado ataca a otro si tiene energía suficiente."""
        if (
            self.energia >= 10
            and not self.esta_derrotado()
            and not otro.esta_derrotado()
        ):
            self.energia -= 10
            otro.salud -= 10

    def recibir_racion(self) -> None:
        """El soldado recupera energía al recibir una ración de agua."""
        if self.energia < 100:
            self.energia += 20
        if self.energia > 100:
            self.energia = 100

    def esta_derrotado(self) -> bool:
        """Devuelve True si la salud del soldado llegó a 0 o menos."""
        return self.salud <= 0

    def estado(self) -> str:
        """Devuelve un string con el nombre, la salud y la energía.
        Por ejemplo: Nombre: Rambo, Salud: 100, Energía: 50
        """
        return f"Nombre: {self.nombre}, Salud: {self.salud}, Energía: {self.energia}"


def main():
    rambo = Soldado("Rambo")
    conan = Soldado("Conan")
    for _ in range(20):  # 20 ataques de 10 de daño = 200
        rambo.atacar(conan)
    print(rambo.estado())
    print(conan.estado())


if __name__ == "__main__":
    main()
