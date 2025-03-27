from invertir_cadena import invertir_cadena


def es_palindromo(s) -> bool:
    s = ajustar(s)
    invertida = invertir_cadena(s)

    return s == invertida


def ajustar(s) -> str:
    s = s.lower()
    a_reemplazar = ["á", "é", "í", "ó", "ú", "ü", " ", ",", ";", ".", ":"]
    reemplazo = ["a", "e", "i", "o", "u", "u", "", "", "", "", ""]
    aux = ""
    for letra in s:
        if letra in a_reemplazar:
            i = a_reemplazar.index(letra)
            letra = reemplazo[i]
        aux = aux + letra

    return aux


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
