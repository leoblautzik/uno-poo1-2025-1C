"""Class Caja de Ahorro"""

from cuenta import Cuenta


class CajaDeAhorro(Cuenta):
    """Class Caja de Ahorro: Las cuentas de ahorro no pueden tener números rojos.
    Ademas del saldo, tienen una reserva donde el titular reserva dinero.
    Ese pozo de reserva no se informa como parte del saldo disponible,
    pero de allí se puede recuperar dinero y pasarlo al saldo.
    """

    def __init__(self, dni):
        super().__init__(dni)
        self.__reserva = 0.00

    def hay_dinero_suficiente(self, monto) -> bool:
        """Devuelve true o false, segun alcance el saldo para
        hacer la operacion"""
        return super().consultar_saldo() >= monto

    def reservar(self, monto):
        """Reserva en la reservarva una parte del saldo"""
        if monto <= self.consultar_saldo():
            self.__reserva += self.extraer(monto)

    def recuperar(self, monto):
        """Incorpora al saldo el monto indicado, desde la reserva"""
        if monto <= self.__reserva:
            self.__reserva -= monto
            self.depositar(monto)

    def get_reserva(self):
        """Devuelve cuanto dinero hay disponible en la reserva"""
        return self.__reserva

    def get_dinero_disponible(self) -> float:
        return super().consultar_saldo() + self.get_reserva()

    def extraer(self, monto) -> float:
        if self.hay_dinero_suficiente(monto):
            self._saldo -= monto

        return monto

    def __str__(self) -> str:
        return super().__str__() + ", Reserva: " + str(self.__reserva)
