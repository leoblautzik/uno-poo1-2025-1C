from deportista import Deportista


class Tenista(Deportista):
    def get_cuota_mensual(self) -> float:
        return super().get_cuota_base() * (1 + super().dias * 0.1)


def main():
    vilas = Tenista(1, 3)
    print(vilas.get_cuota_mensual())


if __name__ == "__main__":
    main()
