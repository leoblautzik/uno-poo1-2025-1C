class Expresion:
    @classmethod
    def esta_balanceada(cls, expr: str) -> bool:
        expr = cls.despejar(expr)
        pila = []
        for leido in expr:
            # si es de abrir, apilar.
            if cls.es_de_abrir(leido):
                pila.append(leido)
            else:
                if len(pila) > 0:
                    desapilado = pila.pop()
                    if not cls.son_parejita(desapilado, leido):
                        return False
                else:
                    return False

        return len(pila) == 0

    @classmethod
    def es_de_abrir(cls, c) -> bool:
        son_de_abrir = ("{", "[", "(")
        return c in son_de_abrir

    @classmethod
    def son_parejita(cls, a, b) -> bool:
        diccionario = {"{": "}", "[": "]", "(": ")"}
        return diccionario[a] == b

    @classmethod
    def despejar(cls, expr) -> str:
        aux = ""
        son_validos = ("{", "}", "[", "]", "(", ")")
        for c in expr:
            if c in son_validos:
                aux += c

        return aux


def main():
    pass


if __name__ == "__main__":
    main()
