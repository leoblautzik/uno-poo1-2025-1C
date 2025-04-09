from cuenta import Cuenta


class CajaDeAhorro:
    """Modelamos una Caja de Ahorro usando composicion.
    CajaAhorro contiene una Cuenta
    """

    def __init__(self, titular):
        self.__cuenta = Cuenta(titular, 0)
        self.__reserva = 0

    def consultar_saldo(self):
        """Devulelve el saldo de la cuenta"""
        return self.__cuenta.consultar_saldo()

    def obtener_titular(self):
        """Devulelve el titular de la cuenta"""
        return self.__cuenta.obtener_titular()

    def depositar(self, monto):
        """Deposita en monto en la cuenta si es un valor positivo"""
        self.__cuenta.depositar(monto)

    def extraer(self, monto) -> float:
        """Retira dinero si hay suficiente saldo"""
        return self.__cuenta.extraer(monto)

    def reservar(self, monto):
        if self.consultar_saldo() >= monto:
            self.__reserva += self.extraer(monto)

    def consultar_reserva(self):
        return self.__reserva

    def retirar_de_reserva(self, monto):
        if monto <= self.__reserva:
            self.__reserva -= monto
            self.depositar(monto)

    def transferir(self, destino, monto):
        destino.depositar(self.extraer(monto))


def main():
    pass


if __name__ == "__main__":
    main()
