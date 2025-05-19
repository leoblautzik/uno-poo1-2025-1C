class Pila:
    def __init__(self):
        self.__p = []

    def apilar(self, dato):
        self.__p.append(dato)

    def desapilar(self):
        if not self.vacia():
            return self.__p.pop()

    def vacia(self):
        return len(self.__p) == 0

    def tope(self):
        return self.__p[len(self.__p) - 1]

    def clear(self):
        self.__p.clear()


def main():
    p = Pila()
    p.apilar(3)
    p.apilar(4)
    print(p.tope())


if __name__ == "__main__":
    main()
