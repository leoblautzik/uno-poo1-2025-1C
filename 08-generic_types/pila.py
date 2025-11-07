from typing import Optional, TypeVar, Generic


class NoHayElementosException(Exception):
    pass


T = TypeVar("T")


class Pila:
    """Pila NO GENERICA"""

    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        """apilar"""
        self.items.append(item)

    def pop(self):
        """desapilar"""
        if self.is_empty():
            raise NoHayElementosException
        return self.items.pop()

    def peek(self):
        """desapilar"""
        if self.is_empty():
            raise NoHayElementosException
        return self.items[len(self.items) - 1]

    def is_empty(self) -> bool:
        """pila vacia"""
        return len(self.items) == 0


class Stack(Generic[T]):
    """Pila Generica"""

    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        """apila un elemento de tipo T"""
        self.items.append(item)

    def pop(self) -> T:
        """desapila el tope de la pila y devuelve un elemento de tipo T"""
        if self.is_empty():
            raise NoHayElementosException
        return self.items.pop()

    def peek(self) -> T:
        """devuelve el tope de la pila de tipo T, sin desapilarlo"""
        if self.is_empty():
            raise NoHayElementosException
        return self.items[len(self.items) - 1]

    def is_empty(self) -> bool:
        """pila vacia"""
        return len(self.items) == 0


def main():
    pass


if __name__ == "__main__":
    main()
