from cuenta import Cuenta


class CajaAhorro:
    """Modelamos una Caja de Ahorro usando composicion.
    CajaAhorro contiene una Cuenta
    """

    def __init__(self, titular):
        self.__cuenta = Cuenta(titular, 0)

    def consultar_saldo(self):
        """Devulelve el saldo de la cuenta"""
        return self.__cuenta.consultar_saldo()

    def obtener_titular(self):
        """Devulelve el titular de la cuenta"""
        return self.__cuenta.obtener_titular()

    def depositar(self, monto):
        """Deposita en monto en la cuenta si es un valor positivo"""
        self.__cuenta.depositar(monto)

    def extraer(self, monto):
        """Retira dinero si hay suficiente saldo"""
        self.__cuenta.extraer(monto)


def main():
    pass


if __name__ == "__main__":
    main()
