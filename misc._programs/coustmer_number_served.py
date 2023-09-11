from ast import Num
from pydoc import describe
from unicodedata import name


class Resturant:
    '''General Description of a Resturant'''
    def __init__(self, resturant_name, cuisine_type):
        self.name = resturant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_resturant(self):
        print(f"The name of Resturant is {self.name}")
        print(f"The resturant serves {self.type} food")
    def open_resturant(self):
        print(f"{self.name} is a good resturant and it is open")
        print(f"The Coustomer served by the resturant on starting day was {self.number_served}")
    def coustumer_served(self):
        print(f"{self.name}is a very popular resturant and has served {self.number_served} coustomers till date")
    def increment_number_served(self,new_coustomers):
        self.number_served += new_coustomers
favorite_resturant = Resturant("The Lodhi","Indian Accent")
print(f"{favorite_resturant.name}, {favorite_resturant.type}")
favorite_resturant.describe_resturant()
favorite_resturant.open_resturant()
# favorite_resturant.name = 250000
# favorite_resturant.name += 25
print(favorite_resturant.name)
favorite_resturant.number_served = 20000
favorite_resturant.coustumer_served()
nearest_resturant = Resturant("Flavors", "Chinese, Fast and Street ")
nearest_resturant.describe_resturant()
nearest_resturant.increment_number_served(1250)
nearest_resturant.coustumer_served()
distant_resturant = Resturant("Telankhana", "Telangana Regional Delicacies along with other cuisines prepared in native style")
distant_resturant.describe_resturant()
