"""Desarrollar un programa que le permita al usuario ingresar un conjunto
de 10 valores enteros. Luego se debe imprimir el conjunto que el
usuario ingresó, primero en el orden original y luego en el inverso.

Por ejemplo, si el usuario ingresa:
12, 43, 5, 26, 7, 98, 1, 32, 18, 9
la salida del programa debe ser la siguiente:

Orden original: 12 43 5 26 7 98 1 32 18 9
Orden inverso: 9 18 32 1 98 7 26 5 43 12
"""

# Version con dos listas
numeros_original = []
numeros_inverso = []

for i in range(5):
    numeros_original.append(int(input("Ingrese un entero: ")))

for i in range(len(numeros_original)):
    numeros_inverso.append(numeros_original[len(numeros_original) - 1 - i])

print(numeros_original)
aux = list(reversed(numeros_original))
print(numeros_inverso)
print(aux)
print(numeros_inverso)


for i in reversed(range(len(numeros_original))):
    print(numeros_original[i], end=",")
print("\n")
