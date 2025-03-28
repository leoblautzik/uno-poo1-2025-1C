"""class TarjetaBaja {

    /**
     * post: saldo de la Tarjeta en saldoInicial.
     */
    public TarjetaBaja(double saldoInicial) { }

    /**
     * post: devuelve el saldo actual de la Tarjeta
     */
    public double obtenerSaldo() { }

    /**
     * post: agrega el monto al saldo de la Tarjeta.
     */
    public void cargar(double monto) { }

    /**
     * pre : saldo suficiente.
     * post: utiliza 21.50 del saldo para un viaje en colectivo.
     */
    public void pagarViajeEnColectivo() { }

    /**
     * pre : saldo suficiente.
     * post: utiliza 19.50 del saldo para un viaje en subte.
     */
    public void pagarViajeEnSubte() { }

    /**
     * post: devuelve la cantidad de viajes realizados.
     */
    public int contarViajes() { }

    /**
     * post: devuelve la cantidad de viajes en colectivo.
     */
    public int contarViajesEnColectivo() { }

    /**
     * post: devuelve la cantidad de viajes en subte.
     */
    public int contarViajesEnSubte() { }
}"""


class TarjetaBaja:
    """Modelamos la Tarjeta Baja"""

    BONDI = 21.50
    SUBTE = 19.50

    def __init__(self, saldo_inicial):
        if saldo_inicial <= 0:
            raise ValueError("Importe incorrecto")
        self.__saldo = saldo_inicial
        self.__viajes_en_colectivo = 0
        self.__viajes_en_subte = 0

    def obtener_saldo(self):
        """Devuelve el saldo actual  de la tarjeta"""
        return self.__saldo

    def cargar(self, monto):
        """Cargamos la tarjeta, el monto debe ser mayor que cero"""
        if monto <= 0:
            raise ValueError("Importe incorrecto")
        self.__saldo += monto

    def pagar_viaje_en_colectivo(self):
        if self.obtener_saldo() > TarjetaBaja.BONDI:
            self.__saldo -= TarjetaBaja.BONDI
            self.__viajes_en_colectivo += 1

    def pagar_viaje_en_subte(self):
        if self.obtener_saldo() > TarjetaBaja.SUBTE:
            self.__saldo -= TarjetaBaja.SUBTE
            self.__viajes_en_subte += 1

    def contar_viajes_en_colectivo(self):
        return self.__viajes_en_colectivo

    def contar_viajes_en_subte(self):
        return self.__viajes_en_subte

    def contar_viajes(self):
        return self.__viajes_en_subte + self.__viajes_en_subte


def main():
    tb = TarjetaBaja(100)
    tb.pagar_viaje_en_colectivo()
    print(tb.obtener_saldo())


if __name__ == "__main__":
    main()
