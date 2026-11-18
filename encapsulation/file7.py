class BankAccount:
    def __init__(self,name,accnum):
        self.name = name
        self._accnum = accnum
        self.__balance = 500

    def view_balance(self): #getter method
        return self.__balance

    def deposit(self,amount): #setter method
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Amount")

    def withdraw(self,amount): #setter method
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Amount Insufficent")

c1 = BankAccount("Yash",11330)

print(c1.view_balance())
c1.deposit(500)
print(c1.view_balance())
c1.withdraw(555)
print(c1.view_balance())