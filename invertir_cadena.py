def invertir_cadena(s):
    s_invertida = ""
    for letra in s:
        s_invertida = letra + s_invertida

    return s_invertida


def main():
    s1 = "programacion"
    print(invertir_cadena(s1))
    s2 = "supercalifragilisticoespialidoso"
    print(invertir_cadena(s2))


if __name__ == "__main__":
    main()
