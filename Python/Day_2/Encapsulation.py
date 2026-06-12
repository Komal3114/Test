"""
class Instagram:
    __password = "Akshay12345" # Private
    __followers = 500

    def change_Password(self,old,new):
        if old == self.__password:
            self.__password = new
            print("Password Changed Successfully ")
        else:
            print("Wrong Password")

    def add_followers(self):
        self.__followers += 1
        print(f"New Follower ! Total : {self.__followers}")


    def get_followers(self):
        print(f"Followers : {self.__followers}")

# Object
acc = Instagram()
acc.change_Password("rahul@123","newpass@456")
acc.add_followers()
acc.get_followers()

# Direct access nahi milega
print(acc.__password) # Error
print(acc.__followers) # Error

"""

class Mobile:
    __battery = 100
    
    def check_battery(self):
        print(self.__battery)
        
m = Mobile()
m.check_battery()