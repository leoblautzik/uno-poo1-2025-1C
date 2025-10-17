from dataclasses import dataclass


@dataclass(order=True)
class Punto:
    x: float
    y: float


def main():
    p1 = Punto(3, 4)
    print(p1)
    p2 = Punto(3, -4)
    print(p1 == p2)
    p4 = Punto(-1, -1)
    p3 = Punto(5, 6)

    l = [p3, p2, p1, p4]
    print(l)
    print(sorted(l))


if __name__ == "__main__":
    main()
