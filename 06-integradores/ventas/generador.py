import random


def main():
    # Lista de códigos de productos de ejemplo
    productos = ["A123X", "B456Y", "C789Z", "D321W", "E654V", "A234Z", "FZZ45", "G33AA"]

    # Crear archivo con 100 líneas de datos aleatorios
    with open("ventas.txt", "w") as f:
        for _ in range(1000):
            codigo = random.choice(productos)
            cantidad = random.randint(1, 1000)
            f.write(f"{codigo} {cantidad}\n")


if __name__ == "__main__":
    main()
