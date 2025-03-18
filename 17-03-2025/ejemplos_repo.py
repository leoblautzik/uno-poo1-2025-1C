print("python")
print("123")
print("True")

print("Hola", "\n", "Mundo")  # salto de linea
print("Hola", "\t", "Mundo")  # tabulador

# Acceso a caracteres
cadena = "python"
print(cadena[0])
print(cadena[-1])
print(cadena[1:4])
print(cadena[1:1])
print(cadena[2:])
print(cadena[:-2])
print(cadena[:])
print(cadena[0:6: 2])
x=2+3


cadena2 = "Lenguaje"
print(cadena + cadena2)  # concatena. Error cadena+numero
print(cadena * 3)  # concatena n copias de cadena
print("yth" in cadena)  # True si 'yth' contenida en cadena
print("pepe" not in cadena)  # True si 'pepe' no esta contenida en cadena

# utilizan orden en ASCII
print(cadena == cadena2)
print(cadena != cadena2)
print(cadena > cadena2)
print(cadena >= cadena2)
print(cadena < cadena2)
print(cadena <= cadena2)

# Funciones de cadenas
print(len(cadena))
print(min(cadena))
print(max(cadena))

print(cadena.count("t"))
print(cadena.find("abc"))

print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(cadena.title())

print(cadena.isdigit())
print(cadena.isalpha())
print(cadena.isalnum())

print(cadena.split("y"))
print(cadena.index("yt"))
print(cadena.strip())  # trimea
print(cadena.replace("ho", "zzzz"))
print("Un {} vale {} {}".format("U$", 1000, "$"))
