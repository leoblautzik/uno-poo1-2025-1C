class Practica:
    @classmethod
    def eliminar_duplicados(cls, enteros) -> []:
        aux = []
        for e in enteros:
            if e not in aux:
                aux.append(e)

        return aux

    @classmethod
    def invertir_lista(cls, enteros) -> []:
        aux = []
        for e in enteros:
            aux.insert(0, e)

        return aux

    @classmethod
    def suma_dos(cls, enteros) -> bool:
        for i in range(len(enteros)):
            for j in range(i + 1, len(enteros) - 1):
                if enteros[i] + enteros[j] in enteros:
                    return True
        return False

    @classmethod
    def es_sublista(cls, l1, l2) -> bool:
        for i in range(len(l2) - len(l1) + 1):
            print(l2[i : i + len(l1)])
            if l2[i : i + len(l1)] == l1:
                return True
        return False


def main():
    l1 = [1, 2, 2, 1, 4, 2, 4, 3]
    print(Practica.eliminar_duplicados(l1))
    l1.reverse()
    print(l1)
    print(Practica.invertir_lista(l1))
    l2 = [1, 6, 2, 1, 4]
    l3 = [1, 3, 5, 7, 9]
    print(Practica.suma_dos(l2))
    print(Practica.suma_dos(l3))

    l4 = [22, 14, 6]
    l5 = [39, 41, 17, 23, 15, 6, 3, 22, 14, 6]
    print(Practica.es_sublista(l4, l5))


if __name__ == "__main__":
    main()
