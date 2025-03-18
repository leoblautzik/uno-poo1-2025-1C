"""Se ingresa un valor numérico de 8 dígitos que 
representa una fecha con el siguiente formato aaaammdd. 
Se pide informar por separado el día, el mes y el año 
de la fecha ingresada
"""

fecha = int(input("Ingrese una fecha con formato aaaammdd: "))

print("Año: ", fecha // 10000)
print("Mes: ", fecha % 10000 // 100)
print("Día: ", fecha % 100)
