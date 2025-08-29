class TarjetaBaja:
    SUBTE: float = 19.50
    COLECTIVO: float = 21.50

    def __init__(self, saldo_inicial: float):
        self.__saldo: float = saldo_inicial
        self.__cantidad_viajes_colectivo = 0
        self.__cantidad_viajes_subte = 0

    def obtener_saldo(self) -> float:
        return self.__saldo

    def cargar(self, monto):
        self.__saldo += monto

    def pagar_colectivo(self):
        if self.obtener_saldo() >= TarjetaBaja.COLECTIVO:
            self.__saldo -= TarjetaBaja.COLECTIVO
            self.__cantidad_viajes_colectivo += 1

    def contar_viajes_colectivo(self):
        return self.__cantidad_viajes_colectivo

    def contar_viajes_subte(self):
        return self.__cantidad_viajes_subte

    def contar_viajes(self):
        return self.__cantidad_viajes_subte + self.__cantidad_viajes_colectivo
