from Estanteria import *


class Participante:
    """
    Persona que participa en la liga.
    Se le asocia sus Juegos de Mesa y Expansiones.
    """

    # nombre = ''
    # juegos = set()
    # expansiones = set()

    def __init__(self, alias, juegos, expansiones):
        """
        Constructor.

        :param alias:       Nombre con el que identificar al Participante.
        :param juegos:      Conjunto de Juegos de Mesa que tiene.
        :param expansiones: Conjunto de Expansiones que tiene.
        """

        self.nombre = alias

        self.juegos = set()

        if juegos is not None:
            if isinstance(juegos, JuegoMesa):
                self.juegos.add(juegos)
            else:
                self.juegos = juegos

        self.expansiones = set()

        if expansiones is not None:
            if isinstance(expansiones, Expansion):
                self.expansiones.add(expansiones)
            else:
                self.expansiones = expansiones

    def agregar_juego(self, juego):
        """
        Relaciona el Juego de Mesa con el Participante de forma consistente:
        añadiendo el juego a los juegos del Participante, y añadiendo al Participante
        a los dueños del juego.

        :param juego:
        :return:
        """

        duenos = juego.duenos
        duenos.add(self)
        
        if juego not in self.juegos:
            self.juegos.add(juego)
        else:
            print("El juego '{}' ya está asociado al jugador '{}'".format(juego.nombre, self.nombre))

    def datos(self):
        linea = lambda texto: texto + "\n"

        informacion = linea(self.nombre)
        informacion += linea("\tJuegos:")

        if len(self.juegos) > 0:
            for juego in self.juegos:
                informacion += "\t\t" + linea(str(juego))
        else:
            informacion += linea("\t\tNinguno")

        informacion += linea("\tExpansiones:")

        if len(self.expansiones) > 0:
            for expansion in self.expansiones:
                informacion += "\t\t" + linea(str(expansion))
        else:
            informacion += linea("\t\tNinguna")

        return informacion

    def __str__(self):
        informacion = "{} : {} ; {}"

        # Guardar solo el nombre de los juegos y expansiones
        juegos = []
        expansiones = []

        for juego in self.juegos:
            juegos.append(juego.nombre)

        for expansion in self.expansiones:
            expansiones.append(expansion.nombre)

        return informacion.format(self.nombre, ", ".join(juegos), ", ".join(expansiones))
