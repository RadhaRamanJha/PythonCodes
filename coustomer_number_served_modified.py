class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name = resturant_name          
        self.cuisine_type = cuisine_type              
        self.number_served = 0
    def describe_resturant(self):
        print(f"Welcome to {self.resturant_name}")
        print(f"{self.resturant_name} serves {self.cuisine_type} food")
    def open_resturant(self):
        print(f"{self.resturant_name} is open to serve you")
        print(f"The number of coustomer served today is {self.number_served}")
    def set_number_served(self,new_coustomer):
        self.number_served += new_coustomer 
        print(f"The number of coustomers served = {self.number_served}")
resturant = Resturant("Hotel Taz", "North Indian")
print(f"{resturant.resturant_name}")
print(f"{resturant.cuisine_type}")
resturant.describe_resturant()
resturant.open_resturant()
resturant.set_number_served(23)