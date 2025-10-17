from typing import TypeVar

T = TypeVar("T")


def process_numbers(numbers: list[int]) -> list[int]:
    return [number + 1 for number in numbers]


def process_elements(elements: list[T]) -> list[T]:
    return [e for i, e in enumerate(elements) if i % 2 != 0]


# def process_elements(elements) -> list:
#     return [e for i, e in enumerate(elements) if i % 2 != 0]


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    elements = ["Ana", "Laura", "Julia", "Mary"]

    processed = process_numbers(numbers)
    print(type(processed))
    print(processed)

    processed = process_elements(elements)
    print(type(processed))
    print(processed)

    processed = process_elements(numbers)
    print(type(processed))
    print(processed)


if __name__ == "__main__":
    main()
