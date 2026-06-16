""" Q1. Create a class BankAccount with: (4 Marks) 
• Private variable __balance = 10000 
• Method deposit(amount) → add to balance and print new balance 
• Method withdraw(amount) → if amount > balance print 'Insufficient!', else deduct 
• Method get_balance() → print current balance Create 2 objects and perform deposit and withdraw operations on both.
"""

class BankAccount:
    def __init__(self):
        self.__balance = 10000

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)
        print("New Balance:", self.__balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient!")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.__balance)

    def get_balance(self):
        print("Current Balance:", self.__balance)



account1 = BankAccount()
account2 = BankAccount()


print("Account 1:")
account1.deposit(5000)
account1.withdraw(3000)
account1.get_balance()

print("\nAccount 2:")
account2.deposit(2000)
account2.withdraw(15000)
account2.get_balance()