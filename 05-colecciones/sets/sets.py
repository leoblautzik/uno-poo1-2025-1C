"""Ejercicios básicos de conjuntos"""


def elementos_unicos(lista: list[int]) -> set[int]:
    """Recibe una lista de enteros y devuelve un conjunto con los elementos únicos de la lista."""
    # TODO
    return set(lista)


def todos_pares(conjunto: set[int]) -> bool:
    """Devuelve True si todos los elementos del conjunto son números pares."""
    # TODO
    for e in conjunto:
        if e % 2 != 0:
            return False
    return True


def interseccion_unica(conjunto1: set[int], conjunto2: set[int]) -> set[int]:
    """Devuelve un nuevo conjunto con los elementos que aparecen
    en ambos conjuntos.
    No debe modificar los conjuntos originales."""
    # TODO
    interseccion: set[int] = set()
    for e in conjunto1:
        if e in conjunto2:
            interseccion.add(e)

    return interseccion


def diferencia_simetrica(conjunto1: set[str], conjunto2: set[str]) -> set[str]:
    """Devuelve un conjunto con los elementos que están en uno de los conjuntos pero no en ambos."""
    dif_sim: set[str] = set()

    for e in conjunto1:
        if e not in conjunto2:
            dif_sim.add(e)

    for e in conjunto2:
        if e not in conjunto1:
            dif_sim.add(e)

    return dif_sim


def tiene_elemento_comun(conjuntos: list[set[int]]) -> bool:
    """Recibe una lista de conjuntos y devuelve True si hay al menos
    un elemento que está presente en todos los conjuntos."""
    if len(conjuntos) == 0:
        return False

    inter: set[int] = conjuntos[0]
    for i in range(1, len(conjuntos)):
        inter = interseccion_unica(inter, conjuntos[i])

    return len(inter) != 0


def main():
    pass


if __name__ == "__main__":
    main()
