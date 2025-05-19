from collections import deque


def main():
    cola = deque()

    # Encolar O(1)
    cola.append("a")
    cola.append("b")

    print(cola)  # deque(['b'])

    # Desencolar O(1)
    primero = cola.popleft()

    print(primero)  # "a"
    print(cola)  # deque(['b'])


if __name__ == "__main__":
    main()
