from Estanteria import *
from Participante import Participante


help(JuegoMesa)
help(Expansion)
help(Participante)


def mostrar_datos(lista):
    for elemento in lista:
        print(elemento.datos())


def mostrar_info():
    mostrar_datos(participantes)
    print("--------------------------------------------------------------------------------")
    mostrar_datos(juegos)
    print("--------------------------------------------------------------------------------")
    mostrar_datos(expansiones)
    print("================================================================================")


# Variables comunes
participantes = []
juegos = []
expansiones = []


# 1 participante y 1 juego
participante1 = Participante("Galán", None, None)
juego1 = JuegoMesa("Railroad Ink Challenge: Shining Yellow", participante1, None, (2, 4), (15, 30), 50)

participantes.append(participante1)
juegos.append(juego1)

mostrar_info()


# 2 participantes
participante2 = Participante("Javi", None, None)

participantes.append(participante2)

mostrar_info()


# 2 participantes y 3 juegos
juego2 = JuegoMesa("Railroad Ink Challenge: Green Lush", participante1, None, (2, 4), (15, 30), 25)
juego3 = JuegoMesa("Muffin Time!", set(participantes), None, (2, 10), (15, 30), None)
juego4 = JuegoMesa("Soulgivers", participante1, None, (2, 4), (30, 60), 100)

juegos += [juego2, juego3, juego4]

mostrar_info()


# 2 participantes, 4 juegos y 3 expansiones
expansion1 = Expansion("Storage Box", participante1, {juego1, juego2}, 0, 0, None)
expansion2 = Expansion("Rainbow Pack", set(participantes), juego3, 0, 0, None)
expansion3 = Expansion("Pie Flavor Pack", set(participantes), juego3, 0, 0, None)

expansiones += [expansion1, expansion2, expansion3]

mostrar_info()
