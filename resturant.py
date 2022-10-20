from pydoc import describe
from unicodedata import name


class Resturant:
    '''General Description of a Resturant'''
    def __init__(self, resturant_name, cuisine_type):
        self.name = resturant_name
        self.type = cuisine_type
    def describe_resturant(self):
        print(f"The name of Resturant is {self.name}")
        print(f"The resturant serves {self.type} food")
    def open_resturant(self):
        print(f"{self.name} is a good resturant and it is open")
favorite_resturant = Resturant("The Lodhi","Indian Accent")
print(f"{favorite_resturant.name}, {favorite_resturant.type}")
favorite_resturant.describe_resturant()
favorite_resturant.open_resturant()
nearest_resturant = Resturant("Flavors", "Chinese, Fast and Street ")
nearest_resturant.describe_resturant()
distant_resturant = Resturant("Telankhana", "Telangana Regional Delicacies along with other cuisines prepared in native style")
distant_resturant.describe_resturant()
