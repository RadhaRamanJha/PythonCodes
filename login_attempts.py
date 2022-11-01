class User:
    '''Information of New user'''
    def __init__(self,name,title, age, gender ):
        self.name = name
        self.title = title
        self.age = age
        self.gender = gender
        self.login_attempt = 0
    def describe_user(self):
        print(f"{self.name}{self.title}is a {self.gender},is {self.age} years old")
    def greet_user(self):
        print(f"Hello {self.name} welcome to the world of programing")
    def increment_login_attempt(self):
        self.login_attempt += 1
        print(f"The number of login attempt done by {self.name} is {self.login_attempt}")
    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f"The login attempt has been set to {self.login_attempt} after deactivation")
first_user = User("Bandana", "Mishra",40, "Female")
first_user.greet_user()
first_user.describe_user()
first_user.increment_login_attempt()
first_user.reset_login_attempts()
current_user = User("Mukund","Jha", 35, "Male")
current_user.greet_user()
current_user.describe_user()
current_user.increment_login_attempt()
current_user.increment_login_attempt()
current_user.increment_login_attempt()
future_user = User("Mukesh", "Jha", 33, "Male")
future_user.greet_user()
future_user.describe_user()
