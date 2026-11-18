class InValidAmountException(Exception):
    pass

class InSufficientBalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,name):
        self.name = name
        self.__balance = 500

    def deposit(self,amount):
        if amount < 0:
            raise InValidAmountException("Amount cannot be negative")
        else:
            self.__balance += amount
            print(f"{amount} deposited successfully")

    def withdrawl(self,amount):
        if amount > self.__balance:
            raise InSufficientBalanceException("Insufficient Balance")
        else:
            self.__balance -= amount
            print(f"{amount} Withdrawn Succesfully")


ba = BankAccount("Yash")
try:
    ba.deposit(1000)
    ba.withdrawl(7000)
except InSufficientBalanceException as e2:
    print(e2)
# try:
#     ba.deposit(-1000)
# except InValidAmountException as e1:
#     print(e1)

print("end")

