class Employee():
    def __init__(self,first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)
    
    def full_name_of_employee(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()
    
    def salary_info_of_employee(self):
        print(self.full_name_of_employee())
        print(f"\t\t {self.annual_salary}")

    def give_raise(self, raise_amount = 5000):
        if (raise_amount >= 5000):
            self.annual_salary += raise_amount
        else:
            self.annual_salary += 5000
