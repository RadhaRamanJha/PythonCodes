class User:
    '''Information of New user'''
    def __init__(self,name,title, age, gender ):
        self.name = name
        self.title = title
        self.age = age
        self.gender = gender
    def describe_user(self):
        print(f"{self.name}{self.title}is a {self.gender},is {self.age} years old")
    def greet_user(self):
        print(f"Hello {self.name} welcome to the world of programing")
first_user = User("Bandana", "Mishra",40, "Female")
first_user.greet_user()
first_user.describe_user()
current_user = User("Mukund","Jha", 35, "Male")
current_user.greet_user()
current_user.describe_user()
future_user = User("Mukesh", "Jha", 33, "Male")
future_user.greet_user()
future_user.describe_user()
