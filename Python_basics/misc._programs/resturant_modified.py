class Resturant:
    """A Simple Attempt to model a resturant"""
    def __init__(self,resturant_name,cuisine_type):
        '''Initialize attributes to describe a resturant'''
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
    def describe_resturant(self):
        '''General Description of Resturant'''
        print(f"Welcome to {self.resturant_name}")
        print(f"{self.resturant_name} serves {self.cuisine_type} food")
    def open_resturant(self):
        '''Greeting the Coustomer on enterance in the resturant'''
        print(f"{self.resturant_name} is open to serve you")
resturant = Resturant("Hotel Taz", "North Indian")
print(f"{resturant.resturant_name}")
print(f"{resturant.cuisine_type}")
resturant.describe_resturant()
resturant.open_resturant()