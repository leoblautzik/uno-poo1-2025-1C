# calculadora.py


class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b

    def potencia(self, a, b):
        # return math.pow(a, b)
        return a**b


def main():
    c = Calculadora()
    print(c.sumar(10, 15))
    print(c.multiplicar(10, 15))
    print(c.potencia(10, 2))


if __name__ == "__main__":
    main()
