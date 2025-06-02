import csv
import random


def main():
    # Lista de códigos de eventos de ejemplo
    codigos_evento = [
        "EVT001",
        "EVT002",
        "EVT003",
        "EVT004",
        "EVT005",
        "EVT006",
        "EVT007",
        "EVT008",
        "EVT009",
        "EVT010",
    ]

    # Crear archivo CSV con 100 líneas de datos aleatorios
    with open("eventos_gen.csv", mode="w", newline="") as archivo:
        escritor = csv.writer(archivo)
        # Escribir encabezado si lo necesitás:
        # escritor.writerow(['Código del Evento', 'Número de puerta', 'Cantidad de Espectadores'])

        for _ in range(500):
            codigo = random.choice(codigos_evento)
            puerta = random.randint(1, 15)
            espectadores = random.randint(1, 200)
            escritor.writerow([codigo, puerta, espectadores])


if __name__ == "__main__":
    main()
