class Resturant:
    def __init__(self,r_n,c_t):
        self.resturant_name = r_n          
        self.cuisine_type = c_t              
    def describe_resturant(self):
        print(f"Welcome to {self.resturant_name}")
        print(f"{self.resturant_name} serves {self.cuisine_type} food")
    def open_resturant(self):
        print(f"{self.resturant_name} is open to serve you")
class IceCreamStand(Resturant):
    def __init__(self,name,fl= ["Vanila", "Choclate", "TutiFruty", "ButterSchoth","Surprise Flavor"]):
        super().__init__(name, "IceCreamStand")
        self.flavours = fl
#    def description_IceCreamStand(self):   
    def describe_resturant(self):
        print(f"The Flavors of {self.resturant_name}  Ice Cream stand are {self.flavours[:]}")
resturant = Resturant("Hotel Taz", "North Indian")
print(f"{resturant.resturant_name}")
print(f"{resturant.cuisine_type}")
resturant.describe_resturant()
resturant.open_resturant()
IceCreamWorld = IceCreamStand("IcecreamWorld")
IceCreamWorld1 = IceCreamStand("PrueDelight", ["TutiFruty", "ButterSchoth","Surprise Flavor"])
IceCreamWorld.describe_resturant()
IceCreamWorld1.describe_resturant()