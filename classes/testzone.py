from banque import BankAccount

DATABASE = [BankAccount.__init__("Neil", 100)]


def printresume(database=DATABASE):
    print("""
    Amount :
    Name :""".format(BankAccount.get_amount(database[0]), BankAccount.get_name(database[0])))


BankAccount.add_and_deposit(50, "-")
printresume()
BankAccount.rename("Jean")
BankAccount.add_and_deposit(100, "+")
