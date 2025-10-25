"""Ejercicios de listas"""


def eliminar_duplicados(enteros: list[int]) -> list[int]:
    """Devuelve una nueva lista con los mismos elementos pero sin repetir,
    manteniendo el orden de aparición original."""
    sd: list[int] = []
    for e in enteros:
        if e not in sd:
            sd.append(e)

    return sd


def invertir_lista(enteros: list[int]) -> list[int]:
    """Recibe una lista de enteros y devuelve otra pero invertida"""
    # TODO
    li: list[int] = enteros[::-1]
    return li


def contiene_suma_dos(enteros: list[int]) -> bool:
    """Recibe una lista de enteros y devuelva true
    si la lista contiene dos elementos tales que el
    número resultante de sumarlos también sea un elemento de la lista.
    Por ejemplo si recibe la lista [1, 2, 3, 4, 5] devuelve true.
    """
    # TODO
    return True


def es_sublista(l1: list[int], l2: list[int]) -> bool:
    """Escriba un método que devuelva true si una lista de enteros
    es sublista de otra.
    Por ejemplo: si tenemos las listas L1 = [22, 14, 6]
    y L2 = [39, 41, 17, 22, 14, 6, 3, 11, 73, 81]
    entonces el método devolverá true porque L1 es una sublista de L2.
    Pero si tenemos otra lista L3 = [39, 41, 22, 17, 14, 3, 11, 73, 6, 81],
    vemos que L1 no es sublista de L3 por lo que el método
    llamado con L1 y L3 debe devolver false."""
    # TODO
    for i in range(len(l2) - len(l1) + 1):
        if l1 == l2[i : i + len(l1)]:
            return True

    return False
