from payment_methods.credit_card import CreditCard
from payment_methods.upi import UPI



class OnlineStore:
    def __init__(self,payment_method):  #loose Coupling
        self.payment_method = payment_method

    def process(self,amount):
        print("Processing Transaction")
        self.payment_method.authenticate()
        self.payment_method.pay(amount)
        print("Transcation Successfull....")


payment1 = CreditCard() #CC instance
payment2 = UPI() #upi instance

order1 = OnlineStore(payment2)
order1.process(5000)
