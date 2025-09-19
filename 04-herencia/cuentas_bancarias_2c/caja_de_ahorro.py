from cuenta import Cuenta


class CajaAhorro(Cuenta):
    def __init__(self, titular):
        super().__init__(titular)
        self.__reserva = 0

    def dinero_disponible(self):
        return super().consultar_saldo() + self.__reserva

    def reservar(self, monto):
        if not self.es_monto_valido(monto):
            raise ValueError("Monto inválido")
        if self.consultar_saldo() >= monto:
            self.__reserva += monto
            self.extraer(monto)

    def retirar(self, monto):
        if not self.es_monto_valido(monto):
            raise ValueError("Monto inválido")
        if self.__reserva >= monto:
            self.__reserva -= monto
            self.depositar(monto)


def main():
    cajita_de_ahorrito = CajaAhorro("Leo")
    print(cajita_de_ahorrito.consultar_saldo())
    cajita_de_ahorrito.depositar(100000)
    cajita_de_ahorrito.reservar(50000)
    print(cajita_de_ahorrito.consultar_saldo())
    print(cajita_de_ahorrito.dinero_disponible())
    cajita_de_ahorrito.retirar(60000)
    print(cajita_de_ahorrito.dinero_disponible())
    print(cajita_de_ahorrito.consultar_saldo())


if __name__ == "__main__":
    main()
