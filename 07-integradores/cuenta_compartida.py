class ComensalFueraDeLaMesaException(Exception):
    pass


class Consumo:
    def __init__(self, desc, precio) -> None:
        self.descripcion = desc
        self.precio = precio

    def __repr__(self):
        return f"{self.descripcion} -> {self.precio}"


class CuentaCompartida:
    def __init__(self, tam: int, cubierto: float):
        self.mesa: list[list[Consumo]] = []
        for _ in range(tam):
            self.mesa.append([])
        self.tam = tam
        self.cubierto = cubierto

    def agregar_consumo(self, comensal: int, consumo: Consumo) -> None:
        comensal = comensal - 1
        if 0 > comensal or comensal > self.tam:
            raise ComensalFueraDeLaMesaException()

        lc = self.mesa[comensal]
        lc.append(consumo)

    def consultar_consumos(self, comensal):
        comensal = comensal - 1
        if 0 > comensal or comensal > self.tam:
            raise ComensalFueraDeLaMesaException()
        print(
            "Comensal nro: ",
            comensal + 1,
        )
        print(self.mesa[comensal])
        print("\nImporte a abonar: ")
        importe = 0
        for c in self.mesa[comensal]:
            importe += c.precio
        print(importe + self.cubierto)


def main():
    cc = CuentaCompartida(2, 500)
    cc.agregar_consumo(1, Consumo("Arroz con pollo", 18000))
    cc.consultar_consumos(1)
    cc.agregar_consumo(2, Consumo("Ensalada Caesar", 21000))
    cc.consultar_consumos(2)


if __name__ == "__main__":
    main()
