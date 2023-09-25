class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer_reading(self):
        print(f"This car has {self.odometer_reading} miles on it")
class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    def describe_battery_size(self):
        print(f"This car has a {self.battery_size} battery size")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        else:
            range = 325
        print(f"This car has a range of {range} km")
    def upgrade_battery(self):
        if self.battery_size == 100:
            print("Battery already upgraded")
        else:
            self.battery_size = 100
            print("Upgrading the Battery")       
class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
TataTiagoEV = Electric_car("Tata Motors","Tata Tiggo", 2023)
TataTiagoEV.get_descriptive_name()
TataTiagoEV.battery = Battery()
TataTiagoEV.battery.get_range()
print(f"The Battery size is {TataTiagoEV.battery.battery_size} kW")
TataTiagoEV.battery.upgrade_battery()
print(f"The Battery size is {TataTiagoEV.battery.battery_size} kW")
TataTiagoEV.battery.get_range()
TataTiagoEV.battery.upgrade_battery()