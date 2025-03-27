"""Class Nota"""


class Nota:
    def __init__(self, valor):
        """Valor inicial debe estar comprendido entre 0 y 10"""
        self.valor = valor

    @property
    def valor(self):
        """Obtener valor"""
        return self.__valor

    @valor.setter
    def valor(self, valor_inicial):
        """Setear el valor"""
        if valor_inicial < 0 or valor_inicial > 10:
            raise ValueError("Valor incorrecto")
        self.__valor = valor_inicial

    def aprobado(self):
        return self.valor >= 4

    def desaprobado(self):
        return not self.aprobado()

    def recuperar(self, nuevo_valor: int):
        """
        nuevoValor está comprendido entre 0 y 10.
        modifica el valor numérico de la Nota, cambiándolo por nuevoValor,
        siempre y cuando nuevoValor sea superior al valor numérico actual de la Nota.
        """
        self.valor = max(nuevo_valor, self.valor)


def main():
    n = Nota(10)
    print(n.valor)
    print(n.aprobado())
    print(n.valor, n.aprobado())
    n1 = Nota(4)
    print(n1.valor, n1.aprobado())
    n2 = Nota(2)
    print(n2.valor, n2.aprobado(), n2.desaprobado())
    n2.recuperar(5)
    print(n2.valor, n2.aprobado(), n2.desaprobado())


if __name__ == "__main__":
    main()
