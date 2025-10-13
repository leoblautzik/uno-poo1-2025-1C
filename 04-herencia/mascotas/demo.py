from conejo import Conejo
from gato import Gato
from mascota import Mascota
from perro import Perro


def vacunar(bicho: Mascota):
    bicho.vacunar()


def main():
    mascotas: list[Mascota] = []

    boby = Perro("Boby", 3, "collie")
    michi = Gato("Tomy", 12, "Smoking")
    rabito = Conejo("Rabito", 1, "Angora")
    mascotas.append(boby)
    mascotas.append(michi)
    mascotas.append(rabito)
    mascotas.append(Perro("Lucas", 4, "caniche"))
    vacunar(boby)
    vacunar(rabito)

    for m in mascotas:
        mensaje = str(m)
        if isinstance(m, Perro):
            mensaje += m.recordar_vacunar()

        print(mensaje)


if __name__ == "__main__":
    main()
