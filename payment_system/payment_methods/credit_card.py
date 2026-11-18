from api.payment_api import Payment_API
from random import randint

class CreditCard(Payment_API):
    def authenticate(self):
        otp = randint(100,999)
        print(f"Credit Card OTP verified {otp}")
        print("Credit Card Authentication Done")

    def pay(self,amount):
        transactID = randint(10000,99999)
        print(f"Transaction ID is {transactID}")        
        print(f"Paid {amount} using Credit Card")
        
