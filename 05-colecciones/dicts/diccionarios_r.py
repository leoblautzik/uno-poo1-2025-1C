"""
============================================================
                    EJERCICIOS CON DICT
============================================================
"""


def contar_frecuencias(palabras: list[str]) -> dict[str, int]:
    """Recibe una lista de palabras y devuelve un diccionario donde
    las claves son palabras y los valores la cantidad de veces
    que aparece cada una."""
    dpf: dict[str, int] = {}

    # for cada_palabra in palabras:
    #     if cada_palabra in dpf.keys():
    #         valor_actual = dpf[cada_palabra]
    #         valor_actual += 1
    #     else:
    #         valor_actual = 1
    #
    #     dpf[cada_palabra] = valor_actual

    for cada_palabra in palabras:
        frecuencia = dpf.setdefault(cada_palabra, 0) + 1
        dpf[cada_palabra] = frecuencia

    return dpf


def invertir_diccionario(dic: dict[str, int]) -> dict[int, list[str]]:
    """Recibe un diccionario de palabra, frecuencia y devuelve un nuevo
    diccionario donde las claves son las frecuencias y los valores son
    listas de palabras con esa frecuencia."""
    # TODO
    di: dict[int, list[str]] = {}
    for p, f in dic.items():
        lp = di.setdefault(f, [])
        lp.append(p)
        di[f] = lp

    return di


def fusionar_diccionarios(dic1: dict[str, int], dic2: dict[str, int]) -> dict[str, int]:
    """Devuelve un nuevo diccionario que contiene todas las claves de ambos.
    Si una clave aparece en ambos, el valor debe ser la suma de los dos."""
    # TODO
    fus: dict[str, int] = {}
    fus.update(dic1)
    for k2, v2 in dic2.items():
        fus[k2] = fus.setdefault(k2, 0) + v2

    return fus


def filtrar_por_valor(dic: dict[str, int], minimo: int) -> dict[str, int]:
    """Devuelve un nuevo diccionario con solo las claves cuyo valor es mayor o igual que 'minimo'."""
    # TODO
    return {}


def clave_mas_larga(dic: dict[str, str]) -> str:
    """Recibe un diccionario cuyas claves y valores son strings.
    Devuelve la clave con mayor longitud.
    Si el diccionario está vacío, devuelve cadena vacía."""
    # TODO
    return ""


def main():
    pass


if __name__ == "__main__":
    main()
