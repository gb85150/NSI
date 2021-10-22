from Geoffrey import generate
# Main project


class Dominos:
    """The dominos game is composed of tiles painted with two numbers from 0 to 6
    Two sides :
    - A from 0 to 6
    - B from 0 to 6
    """
    def __init__(self, A, B):
        self.__A = A
        self.__B = B

    def debug(self):
        """
        Fonction de debuging.
        @return None
        """
        print("============================")
        print(self.__A)
        print(self.__B)
        print("============================")
        return None

    def pretty_print(self, vertical: bool):
        """
        :self: self
        :vertical: booléen qui définit le sens du domino selon True = vertical, False = horizontal
        Affiche esthétiquement le domino.
        @return None
        """
        if vertical == True:
            print("""
=======
#     #
#  {}  #
#     #
# === #
#     #
#  {}  #
#     #
=======
""".format(self.__A, self.__B))
        else:
            print("""
=================
#       #       #
#   {}   #   {}   #
#       #       #
=================
        """.format(self.__A, self.__B))
        return None

    def domino_vide(self):
        if self.__A == 0 and self.__B == 0:
          print("Vide !")
        else:
          print("Pas Vide !")
        pass


deck = generate(Dominos)

# Debug zone
deck[5].pretty_print(False)
print(chr(127031))
for i in range(len(deck)):
  deck[i].domino_vide()
