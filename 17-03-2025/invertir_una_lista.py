"""Varias formas de invertir una lista en python"""

"""
1. Usando reverse() (modifica la lista en su lugar)
El método .reverse() invierte la lista directamente sin crear una nueva.
"""
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)  # Salida: [5, 4, 3, 2, 1]

"""
2. Usando [::-1] (copia invertida de la lista)
La forma más rápida y concisa es usando slicing ([::-1]), 
que devuelve una nueva lista invertida.

NOTA: la lista original no se mo
"""
lista = [1, 2, 3, 4, 5]
inversa = lista[::-1]
print(inversa)  # Salida: [5, 4, 3, 2, 1]

""" 
3. Usando
reversed() (iterador sobre la lista)
La función reversed() devuelve un iterador en orden inverso. 
Se puede convertir en una lista con list().

NOTA: la lista original no se mo
"""
lista = [1, 2, 3, 4, 5]
inversa = list(reversed(lista))
print(inversa)

"""
4. Usando for para invertir manualmente
Se puede usar un bucle para invertir la lista manualmente:
"""
lista = [1, 2, 3, 4, 5]
inversa = []
for i in range(len(lista) - 1, -1, -1):
    inversa.append(lista[i])
print(inversa)
