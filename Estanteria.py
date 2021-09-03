from Participante import Participante


class JuegoMesa:
    """
    Juego de mesa e información relacionada.
    """

    def __init__(self, nombre, duenos, expansiones, jugadores, duracion, porcentaje):
        """
        Constructor.

        :param nombre:         Nombre del Juego de Mesa.
        :param duenos:         Participantes que tienen una copia de este juego.
        :param expansiones:    Expansiones de este juego.
        :param jugadores:      Intervalo de jugadores mínimos y máximos por partida.
        :param duracion:       Intervalo de tiempo estimado (en minutos) mínimo y máximo por partida.
        :param porcentaje:     Probabilidad de que este juego sea escogido para un Encuentro.
        """

        self.nombre = nombre

        self.__aduenar(duenos)
        self.__expandir(expansiones)

        self.jugadores = jugadores
        self.duracion = duracion

        self.__porcentuar(porcentaje)

        self.__puntuar(duracion)

    def __aduenar(self, duenos):
        """
        Vincula este juego con sus dueños, de forma que queden relacionados entre sí.

        :param duenos:  Dueño(s) de una copia de este juego.
        """

        # Inicializar los dueños
        self.duenos = set()

        if duenos is not None:
            # Añade este dueño a la lista de dueños de este objeto
            if isinstance(duenos, Participante):
                self.duenos.add(duenos)
            else:
                self.duenos.update(duenos)

            # Añade este juego a la lista de juegos de todos sus dueños
            for dueno in self.duenos:
                dueno.juegos.add(self)

    # TODO: Revisar
    def __expandir(self, expansiones):
        """
        Vincula expansiones a este juego, de forma que queden relacionadas
        entre sí; y a los dueños que tengan una copia de las expansiones.

        :param expansiones:     Expansión(es) compatible(s) con este juego.
        """

        # Inicializar las expansiones
        self.expansiones = set()

        if expansiones is not None:
            # Añade esta expansion a la lista de expansiones de este objeto
            if isinstance(expansiones, Expansion):
                self.expansiones.add(expansiones)
            else:
                self.expansiones.update(expansiones)

    def __porcentuar(self, porcentaje):
        """
        Asigna una probabilidad de que este juego sea elegido para un Encuentro.
        Si se inserta un valor erróneo, se establecerá un 0 % por defecto.

        :param porcentaje:  Probabilidad de que este juego sea elegido para un Encuentro.
        """

        # Inicializar el porcentaje
        if porcentaje is not None and porcentaje >= 0:
            self.porcentaje = porcentaje
        else:
            self.porcentaje = 0

    def __puntuar(self, duracion):
        """
        Asigna una cantidad de puntos entre 1 y 3 en función de la duración de las partidas.
        Estos puntos son los que recibe un Participante al ganar una partida de este juego.

        :param duracion:     Tiempo máximo estimado de duración de una partida.
        """

        # Inicializar los puntos
        if duracion[1] <= 30:
            self.puntos = 1
        elif duracion[1] <= 60:
            self.puntos = 2
        else:
            self.puntos = 3

    def datos(self):
        """
        Muestra información de todos los campos de este juego en forma de árbol.

        :return:    Cadena con todos los valores de la clase.
        """

        linea = lambda texto: texto + "\n"

        datos = linea(self.nombre)
        datos += linea("\tDueños:")

        if len(self.duenos) > 0:
            for dueno in self.duenos:
                datos += "\t\t" + linea(dueno.nombre)
        else:
            datos += linea("\t\tNinguno")

        datos += linea("\tExpansiones:")

        if len(self.expansiones) > 0:
            for expansion in self.expansiones:
                datos += "\t\t" + linea(expansion.nombre)
        else:
            datos += linea("\t\tNinguna")

        datos += linea("\tJugadores:\t {} - {}".format(self.jugadores[0], self.jugadores[1]))
        datos += linea("\tDuracion:\t {} - {} minutos".format(self.duracion[0], self.duracion[1]))

        datos += linea("\tProbabilidad: {} %".format(self.porcentaje))
        datos += linea("\tPuntos:\t\t{}".format(self.puntos))

        return datos

    def __str__(self):
        """
        :return:    Representación textual de este juego.
        """

        cadena = "{}\tj:[{}-{}] t:[{}-{}]"

        # Extraer los valores de las tuplas
        (jMin, jMax) = self.jugadores
        (dMin, dMax) = self.duracion

        return cadena.format(self.nombre, jMin, jMax, dMin, dMax)


class Expansion:
    """
    Expansión asociada a un Juego de Mesa.
    """

    def __init__(self, nombre, duenos, juegos, jugadores, duracion, porcentaje):
        """
        Constructor.

        :param nombre:      Nombre de la Expansion.
        :param duenos:      Participantes que tienen una copia de esta Expansion.
        :param juegos:      Juegos de Mesa con los que se puede utilizar.
        :param jugadores:   Numero de jugadores que añade esta Expansion.
        :param duracion:    Tiempo de juego que añade esta Expansion (en minutos).
        :param porcentaje:  Probabilidad de que esta Expansion se asigne a su Juego de Mesa en un Encuentro.
        """

        self.nombre = nombre

        self.__aduenar(duenos)
        self.__asignar(juegos)

        self.jugadores = jugadores
        self.duracion = duracion

        self.__porcentuar(porcentaje)
        self.__puntuar()

    def __aduenar(self, duenos):
        """
        Vincula esta expansión con sus dueños, de forma que queden relacionados entre sí.

        :param duenos:  Dueño(s) de una copia de esta expansión.
        """

        # Inicializar los dueños
        self.duenos = set()

        if duenos is not None:
            # Añade esta expansión a la lista de dueños de este objeto
            if isinstance(duenos, Participante):
                self.duenos.add(duenos)
            else:
                self.duenos.update(duenos)

            # Añade esta expansión a la lista de expansiones de todos sus dueños
            for dueno in self.duenos:
                dueno.expansiones.add(self)

    # TODO: Revisar
    def __asignar(self, juegos):
        """
        Vincula juegos a esta expansión, de forma que queden relacionadas
        entre sí; y a los dueños que tengan una copia de las expansiones.

        :param juegos:  Juego(s) compatible(s) con la expansión.
        """

        # Inicializar los juegos
        self.juegos = set()

        if juegos is not None:
            # Añade este juego a la lista de juegos de este objeto
            if isinstance(juegos, JuegoMesa):
                self.juegos.add(juegos)
            else:
                self.juegos.update(juegos)

    def __porcentuar(self, porcentaje):
        """
        Asigna una probabilidad de que esta expansión sea elegida para un Encuentro.
        Si se inserta un valor erróneo, se establecerá un 0 % por defecto.

        :param porcentaje:  Probabilidad de que este juego sea elegido para un Encuentro.
        """

        # Inicializar el porcentaje
        if porcentaje is not None and porcentaje >= 0:
            self.porcentaje = porcentaje
        else:
            self.porcentaje = 0

    def __puntuar(self):
        """
        Asigna 1 punto si la expansión aumenta el número de jugadores del
        juego, y otro punto más si también aumenta la duración de la partida.
        """

        # inicializar los puntos
        self.puntos = 0

        if self.jugadores > 0:
            self.puntos += 1

        if self.duracion > 0:
            self.puntos += 1

    def datos(self):
        """
        Muestra información de todos los campos de esta expansión en forma de árbol.

        :return:    Cadena con todos los valores de la clase.
        """

        linea = lambda texto: texto + "\n"

        datos = linea(self.nombre)
        datos += linea("\tDueños:")

        if len(self.duenos) > 0:
            for dueno in self.duenos:
                datos += "\t\t" + linea(dueno.nombre)
        else:
            datos += linea("\t\tNinguno")

        datos += linea("\tJuegos:")

        if len(self.juegos) > 0:
            for juegos in self.juegos:
                datos += "\t\t" + linea(juegos.nombre)
        else:
            datos += linea("\t\tNinguna")

        datos += linea("\tJugadores:\t Añade {}".format(self.jugadores))
        datos += linea("\tDuracion:\t Añade {} minutos".format(self.duracion))

        datos += linea("\tProbabilidad: {} %".format(self.porcentaje))
        datos += linea("\tPuntos:\t\t{}".format(self.puntos))

        return datos

    def __str__(self):
        """
        :return:    Representación textual de esta expansión.
        """

        cadena = "{} ({})\tj:[+{}] t:[+{}]"

        # Guardar solo el nombre de los juegos
        juegos = [juego.nombre for juego in self.juegos]

        return cadena.format(self.nombre, ", ".join(juegos), self.jugadores, self.duracion)
