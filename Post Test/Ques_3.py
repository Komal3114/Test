"""
Q3. Create Abstract class Payment with: (3 Marks) 
• Abstract method pay() 
• Abstract method receipt() 

Create 2 child classes: GPay and CreditCard — implement both methods. 
Create objects and call all methods.
"""

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def receipt(self):
        pass


class Gpay(Payment):
    def pay(self):
        print("Payment made using GPay")

    def receipt(self):
        print("GPay receipt generated")

class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")

    def receipt(self):
        print("Credit Card receipt generated")


gpay = Gpay()
card = CreditCard()

print("GPay:")
gpay.pay()
gpay.receipt()

print("\nCredit Card:")
card.pay()
card.receipt()