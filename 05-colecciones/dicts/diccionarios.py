"""
============================================================
                    EJERCICIOS CON DICT
============================================================
"""


def contar_frecuencias(palabras: list[str]) -> dict[str, int]:
    """Recibe una lista de palabras y devuelve un diccionario donde
    las claves son palabras y los valores la cantidad de veces
    que aparece cada una.

    contar_frecuencias(["uno", "dos", "uno"]), {"uno": 2, "dos": 1}
    """

    d: dict[str, int] = {}
    for palabra in palabras:
        if palabra not in d:
            frecuencia = 1
        else:
            frecuencia = d[palabra] + 1
        d[palabra] = frecuencia

    return d


def palabra_mas_frecuente(dic: dict[str, int]) -> tuple[int, list[str]]:
    """devuelve la palabra con mayor frecuencia y su frecuencia.
    en caso de que haya empate, se debe retornar la frecuencia maxima y
    todas las palabras que se repiten ese numero de veces"""

    frec_max = 0
    palabras_mas_frecuentes = []

    for frecuencia in dic.values():
        if frecuencia > frec_max:
            frec_max = frecuencia

    for palabra in dic.keys():
        if dic[palabra] == frec_max:
            palabras_mas_frecuentes.append(palabra)

    return frec_max, palabras_mas_frecuentes

    # return max(dic.items(), key=lambda item: item[1])


def invertir_diccionario(dic_in: dict[str, int]) -> dict[int, list[str]]:
    """Recibe un diccionario de palabra, frecuencia y devuelve un nuevo
    diccionario donde las claves son las frecuencias y los valores son
    listas de palabras con esa frecuencia."""
    # TODO
    di: dict[int, list[str]] = {}

    for p, f in dic_in.items():
        lp = di.setdefault(f, [])
        lp.append(p)
        di[f] = lp

    # for p, f in dic_in.items():
    #     if f in di.keys():
    #         lp = di[f]
    #     else:
    #         lp = []
    #     lp.append(p)
    #     di[f] = lp

    return di


def fusionar_diccionarios(dic1: dict[str, int], dic2: dict[str, int]) -> dict[str, int]:
    """Devuelve un nuevo diccionario que contiene todas las claves de ambos.
    Si una clave aparece en ambos, el valor debe ser la suma de los dos."""
    # TODO
    fusionado: dict[str, int] = {}
    fusionado.update(dic1)

    for k, v in dic2.items():
        stock = fusionado.setdefault(k, 0) + v
        fusionado[k] = stock

    return fusionado


def filtrar_por_valor(dic: dict[str, int], minimo: int) -> dict[str, int]:
    """Devuelve un nuevo diccionario con solo las claves cuyo valor es mayor o igual que 'minimo'."""
    new_dic = {}

    for k, v in dic.items():
        if v >= minimo:
            new_dic[k] = v

    return new_dic


def clave_mas_larga(dic: dict[str, str]) -> str:
    """Recibe un diccionario cuyas claves y valores son strings.
    Devuelve la clave con mayor longitud.
    Si el diccionario está vacío, devuelve cadena vacía."""

    if dic == {}:
        return ""
    # clave_max = ""
    # for k in dic.keys():
    #     if len(k) > len(clave_max):
    #         clave_max = k
    #
    return max(dic.keys(), key=len)


def main():
    pass


if __name__ == "__main__":
    main()
