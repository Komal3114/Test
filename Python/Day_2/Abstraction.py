from abc import ABC,abstractmethod

# Blueprint
class ATM(ABC) :
    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SBI(ATM):
    def withdraw(self):
        server = "SBI CORE BANKING SERVER"
        language = "JAVA 8"
        database = "Oracle DB"

        print("Cash Withdrawn Successfully")

    def check_balance(self):
        server ="SBI CORE BANKING SERVER"
        language = "JAVA 8"
        database = "Oracle DB"

        print("Balance : 1000000")

sbi = SBI()
sbi.withdraw()
sbi.check_balance()




