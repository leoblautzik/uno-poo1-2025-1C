class Vehiculo:
    valor_base = 1000.00

    def __init__(self, marca, patente):
        self.marca = marca
        self.patente = patente

    @property
    def patente(self):
        return self.__patente

    @patente.setter
    def patente(self, p):
        if p == "":
            raise ValueError("Valor incorrecto")
        self.__patente = p

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, p):
        if p == "":
            raise ValueError("Valor incorrecto")
        self.__marca = p

    def costo_mantenimiento(self) -> float:
        return Vehiculo.valor_base

    def __str__(self):
        return (
            f"Marca: {self.__marca}, "
            f"Patente: {self.patente}, "
            f"Costo M: {self.costo_mantenimiento()}"
        )


class Moto(Vehiculo):
    def __init__(self, marca, patente, cilindrada):
        super().__init__(marca, patente)
        self.__cilindrada = cilindrada

    def costo_mantenimiento(self):
        return super().costo_mantenimiento() + 0.5 * self.__cilindrada


class Auto(Vehiculo):
    def __init__(self, marca, patente, cantidad_puertas):
        super().__init__(marca, patente)
        self.__cantidad_puertas = cantidad_puertas

    def costo_mantenimiento(self):
        return super().costo_mantenimiento() + 200.00 * self.__cantidad_puertas


class Conductor:
    def __init__(self, nombre, dni, veh):
        self.__nombre = nombre
        self.__dni = dni
        self.vehiculo = veh

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, v):
        self.__vehiculo = v

    def mostrar_info(self):
        return (
            f"Nombre: {self.__nombre}, DNI: {self.__dni}, Vehiculo: {self.__vehiculo}, "
        )


def main():
    auto = Auto("Renault", "AA123BB", 4)
    juancito = Conductor("Juan", 123456, auto)
    print(juancito.mostrar_info())
    juancito.vehiculo = Moto("Zanella", "JK123L", 1000)
    print(juancito.mostrar_info())


if __name__ == "__main__":
    main()
