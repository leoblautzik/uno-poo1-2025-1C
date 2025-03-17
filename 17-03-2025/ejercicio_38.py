"""Desarrollar un programa que le permita al usuario ingresar un conjunto
de 10 valores enteros. Luego se debe imprimir el conjunto que el
usuario ingresó, primero en el orden original y luego en el inverso.

Por ejemplo, si el usuario ingresa:
12, 43, 5, 26, 7, 98, 1, 32, 18, 9
la salida del programa debe ser la siguiente:

Orden original: 12 43 5 26 7 98 1 32 18 9
Orden inverso: 9 18 32 1 98 7 26 5 43 12
"""

numeros_original = []
numeros_inverso = []
lista_de_10 = [0 for x in range(1, 11)]
print(lista_de_10)

for i in range(5):
    numeros_original.append(int(input("Ingrese un entero: ")))
# for i in range(10):
#     numeros_inverso[i] = numeros_original[9 - i]

print(numeros_original)
# print(numeros_inverso)
for i in reversed(range(len(numeros_original))):
    print(numeros_original[i], end=",")

print("\n")
