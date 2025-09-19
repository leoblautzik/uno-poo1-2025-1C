# guerrero.py


class Guerrero:
    def __init__(
        self,
        nombre: str,
        energia: int,
        salud: int,
        costo_ataque: int,
        danio: int,
        energia_max: int,
    ):
        self.nombre = nombre
        self.energia = energia
        self.salud = salud
        self.costo_ataque = costo_ataque
        self.danio = danio
        self.energia_max = energia_max

    def atacar(self, otro: "Guerrero") -> None:
        """Ataca a otro guerrero si tiene suficiente energía
        y no está derrotado."""
        if (
            self.energia >= self.costo_ataque
            and not self.esta_derrotado()
            and not otro.esta_derrotado()
        ):
            self.energia -= self.costo_ataque
            otro.salud -= self.danio

    def recibir_racion(self) -> None:
        """Recupera energía al recibir una ración de agua."""
        if self.energia < self.energia_max:
            self.energia += 20
        if self.energia > self.energia_max:
            self.energia = self.energia_max

    def esta_derrotado(self) -> bool:
        """Devuelve True si la salud llegó a 0 o menos."""
        return self.salud <= 0

    def estado(self) -> str:
        """Devuelve un string con nombre, salud y energía."""
        return f"Nombre: {self.nombre}, Salud: {self.salud}, Energía: {self.energia}"


class Soldado(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre, 100, 200, 10, 10, 100)

    def recibir_racion(self) -> None:
        """Recupera energía al recibir una ración de agua."""
        if self.energia < self.energia_max:
            self.energia += 20
        if self.energia > self.energia_max:
            self.energia = self.energia_max


class Orco(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(
            nombre, energia=120, salud=250, costo_ataque=15, danio=20, energia_max=120
        )


class Elfo(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(
            nombre, energia=80, salud=150, costo_ataque=5, danio=15, energia_max=80
        )


def main():
    ares = Soldado("Ares")
    grom = Orco("Grom")
    legolas = Elfo("Legolas")

    ares.atacar(grom)  # Ares ataca a Grom
    grom.atacar(ares)  # Grom responde
    print(ares.estado())
    print(grom.estado())
    grom.atacar(legolas)
    legolas.atacar(ares)
    print(ares.estado())
    print(grom.estado())
    print(legolas.estado())


if __name__ == "__main__":
    main()
