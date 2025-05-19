from collections import deque


class ExpresionBalanceada:
    def es_de_abrir(self, c) -> bool:
        return c in "{[("

    def es_de_cerrar(self, c) -> bool:
        return c in "}])"

    def son_parejita(self, leido, desapilado) -> bool:
        dicc = {"}": "{", "]": "[", ")": "("}
        return desapilado == dicc[leido]

    def esta_balanceada(self, expresion) -> bool:
        pila = deque()
        for c in expresion:
            if self.es_de_abrir(c):
                pila.append(c)

            elif self.es_de_cerrar(c):
                if len(pila) == 0 or not self.son_parejita(c, pila.pop()):
                    return False
            else:
                return False

        return len(pila) == 0


def main():
    eb = ExpresionBalanceada()
    print(eb.esta_balanceada("()"))


if __name__ == "__main__":
    main()
