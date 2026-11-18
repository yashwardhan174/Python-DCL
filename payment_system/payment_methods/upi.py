from api.payment_api import Payment_API
from random import randint

class UPI(Payment_API):
    def authenticate(self):
        otp = randint(100,999)
        print(f"UPI Pin verified {otp}")
        print("UPI Authentication Done")

    def pay(self,amount):
        transactID = randint(10000,99999)
        print(f"Transaction ID is {transactID}")        
        print(f"Paid {amount} using UPI")
        
