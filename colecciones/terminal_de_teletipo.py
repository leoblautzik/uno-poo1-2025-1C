from collections import deque


class TerminalDeTeletipo:
    @classmethod
    def procesar(cls, cadena):
        pila = deque()
        for c in cadena:
            if c not in "/&":
                pila.append(c)
            elif c == "/" and pila:
                pila.pop()
            elif c == "&":
                pila.clear()
        s = ""
        while pila:
            s = pila.pop() + s

        return s


def main():
    print(TerminalDeTeletipo.procesar("abcd//ef/gh///x"))


if __name__ == "__main__":
    main()
