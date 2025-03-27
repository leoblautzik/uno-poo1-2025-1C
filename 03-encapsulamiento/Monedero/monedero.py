"""Defina una clase 'Monedero' que permita gestionar la cantidad de dinero de que una persona
dispone en un momento dado.
La clase deberá tener un constructor que permitirá crear un monedero con una cantidad de dinero
inicial y deberá definir un método para meter dinero en el monedero, otro para sacarlo
y finalmente, otro para consultar el disponible; solo podrá conocerse la cantidad de
dinero del monedero a través de este último método.
Por supuesto, no se podrá sacar más dinero del que haya en un momento dado en el monedero.
Para probar el funcionamiento de la clase, escriba un método 'main' con una serie de instrucciones
que hagan uso de los métodos definidos."""


class Monedero:
    """Class Monedero"""

    def __init__(self, saldo_inicial):
        """Inicializa el monedero con un saldo dado."""
        self.__saldo = max(0, saldo_inicial)  # Asegura que el saldo no sea negativo

    def meter_dinero(self, cantidad):
        """Agrega dinero al monedero."""
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def sacar_dinero(self, cantidad):
        """Saca dinero del monedero si hay saldo suficiente."""
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def consultar_saldo(self):
        """Devuelve el saldo disponible en el monedero."""
        return self.__saldo


def main():
    """Función principal para probar la clase Monedero."""
    mi_monedero = Monedero(100)  # Se inicia con 100
    print("Saldo inicial:", mi_monedero.consultar_saldo())

    mi_monedero.meter_dinero(50)
    print("Saldo después de meter 50:", mi_monedero.consultar_saldo())

    mi_monedero.sacar_dinero(30)
    print("Saldo después de sacar 30:", mi_monedero.consultar_saldo())

    mi_monedero.sacar_dinero(150)  # Intento de sacar más de lo que hay
    print("Saldo final:", mi_monedero.consultar_saldo())


if __name__ == "__main__":
    main()
