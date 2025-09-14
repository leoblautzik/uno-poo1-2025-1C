"""Cuando una Cerradura se bloquea no puede volver a abrirse nunca más
class Cerradura {
   public Cerradura(int claveDeApertura,
        int cantidadDeFallosConsecutivosQueLaBloquean)
    public boolean abrir(int clave)
    public void cerrar()
    public boolean estaAbierta()
    public boolean estaCerrada()
    public boolean fueBloqueada()
    public int contarAperturasExitosas()
    public int contarAperturasFallidas()
}"""

from enum import Enum


class Estado(Enum):
    ABIERTA = 1
    CERRADA = 2
    BLOQUEADA = 3


class Cerradura:
    def __init__(self, clave, cfcqlb):
        self.__clave = clave
        self.__estado = Estado.ABIERTA
        self.__cfcqlb = cfcqlb
        self.__cant_fallos_consecutivos = 0
        self.__cant_fallos = 0
        self.__cant_aciertos = 0

    def fue_bloqueada(self) -> bool:
        return self.__estado == Estado.BLOQUEADA

    def esta_abierta(self) -> bool:
        return self.__estado == Estado.ABIERTA

    def esta_cerrada(self) -> bool:
        return self.__estado == Estado.CERRADA

    def abrir(self, clave) -> bool:
        if self.fue_bloqueada():
            raise RuntimeWarning("Cerradura bloqueada")
        if self.esta_cerrada():
            if self.__clave == clave:
                self.__estado = Estado.ABIERTA
                self.__cant_aciertos += 1
                self.__cant_fallos_consecutivos = 0
                return True
            else:
                self.__cant_fallos += 1
                self.__cant_fallos_consecutivos += 1
                if self.__cant_fallos_consecutivos == self.__cfcqlb:
                    self.__estado = Estado.BLOQUEADA
                return False
        return False

    def cerrar(self) -> None:
        self.__estado = Estado.CERRADA

    def contar_aperturas_exitosas(self) -> int:
        return self.__cant_aciertos

    def contar_aperturas_fallidas(self) -> int:
        return self.__cant_fallos


def main():
    pass


if __name__ == "__main__":
    main()
