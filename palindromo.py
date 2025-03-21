from invertir_cadena import invertir_cadena


def es_palindromo(s) -> bool:
    s = s.lower()
    s = quitar_acentos(s)
    s = quitar_espacios_signos(s)
    invertida = invertir_cadena(s)

    return s == invertida


def quitar_espacios_signos(s) -> str:
    s = s.replace(" ", "")
    s = s.replace(",", "")
    return s


def quitar_acentos(s) -> str:
    s = s.replace("á", "a")
    s = s.replace("é", "e")
    s = s.replace("í", "i")
    s = s.replace("ó", "o")
    s = s.replace("ú", "u")
    s = s.replace("ü", "u")
    return s


def main():
    print(es_palindromo("reconocer"))
    print(es_palindromo("Neuquén"))
    print(
        es_palindromo(
            "Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida"
        )
    )


if __name__ == "__main__":
    main()
