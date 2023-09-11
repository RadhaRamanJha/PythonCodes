class User:
    """ Blue Print for user information Storage"""
    def __init__(self, first_name,last_name):
       '''Initialize the user attributes'''
       self.first_name = first_name
       self.last_name = last_name
       self.age = 18
       self.gender = "Male"
       self.emailID = "emailID"
    def describe_user(self):
        '''Breif description of the User'''
        print(f"\n\n{self.first_name} {self.last_name} is {self.age} year old {self.gender} faculty. You can contact the faculty at {self.emailID}")
    def greet_user(self):
        '''Welcome message to user on log in'''
        print(f"Welcome {self.first_name} {self.last_name}. Glad you logged in !")
class Privileges:
    def __init__(self, privileges ):
        self.privileges = ["can add Post","can delete post","can ban user"]
    def show_privileges(self):
        print(f"\n\nThe privileges of admin are {self.privileges}\n")
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  
        self.privileges = Privileges(self)
user1 = User("Rahul","Singh")
user1.age = 29
user1.gender = "Male"
user1.emailID = "rahul.sing@imsec.ac.in"
user1.describe_user()
user1.greet_user()


user2 = User("Rekha","Goel")
user2.age = 30
user2.gender = "Female"
user2.emailID = "rekha.goel@imsec.ac.in"
user2.describe_user()
user2.greet_user()


admin1 = Admin("Raman","Jha")
admin1.privileges.show_privileges()