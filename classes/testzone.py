from banque import BankAccount

database = BankAccount("Neil", 100)


def printresume(database=database):
    print("""
    Amount :
    Name :""".format(BankAccount.get_amount(database), BankAccount.get_name(database)))


database.add_and_deposit(50, "-")
printresume()
database.rename("Jean")
database.add_and_deposit(100, "+")
