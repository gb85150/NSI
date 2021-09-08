class Chrono:
    """
    Une classe pour représsenter un temps en heures minutes secondes
    """

    def __init__(self, h: int, m: int, s: int) -> None:
        self.__heures = h
        self.__minutes = m
        self.__secondes = s
        print("création d'un nouvel horaire {}:{}:{}"
              .format(self.__heures, self.__minutes, self.__secondes))

    def get_heure(self) -> int:
        return self.__heures

    def set_heure(self, h: int):
        self.__heures = h

    def debug(self) -> str:
        """nik la doc"""
        return "le chrono indique {}:{}:{}".format(self.__heures, self.__minutes, self.__secondes)


Chrono(5, 5, 5)
Chrono.get_heure()
Chrono.set_heure(8)
Chrono.debug()
