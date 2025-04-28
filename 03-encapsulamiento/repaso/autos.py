class Motor:
    def __init__(self, tipo: str):
        self.__tipo = tipo

    @property
    def tipo(self) -> str:
        return self.__tipo


class Auto:
    def __init__(self, marca, tipo_motor):
        self.__marca = marca
        self.__motor = Motor(tipo_motor)

    @property
    def marca(self):
        return self.__marca

    @property
    def tipo_motor(self):
        return self.__motor.tipo

    def __str__(self):
        return f"Marca: {self.__marca}, Tipo de motor: {self.tipo_motor}"


def main():
    autos = [
        Auto("Renault", "naftero"),
        Auto("Tesla", "electrico"),
        Auto("Toyota", "hibrido"),
        Auto("Peugeot", "diesel"),
    ]
    for auto in autos:
        print(auto)


if __name__ == "__main__":
    main()
