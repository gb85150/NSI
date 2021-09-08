class BankAccount:
    def __init__(self, name: str, amount: int):
        """
        Setup the account
        """
        self.__amount = amount
        self.__name = name
        print("The account of M./Mme. {} was created with success, is amount is {} Euros"
              .format(self.__name, self.__amount))

    def get_name(self):
        """
        Get the name of the account
        """
        return self.__name

    def get_amount(self):
        return self.__amount

    def rename(self, newname: str):
        self.__name = newname
        return None

    def add_and_deposit(self, amount: int, operationtype: str):
        if operationtype == "-":
            self.__amount -= amount
        if operationtype == "+":
            self.__amount += amount
        return print("The operation was successful, the new amount is {}"
                     .format(BankAccount.get_amount(self)))
