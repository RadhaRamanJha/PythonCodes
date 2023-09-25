import unittest
from employee_info_blue_print import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Tests Check on employee raise being Default or Coustom"""
    def test_give_default_raise(self):
        """Test to Check default increment of salary took place"""
        self.employee_under_scan = Employee("Radha Raman","Jha",480000)
        # self.employee_under_scan.salary_info_of_employee()
        previous_anuual_salary = self.employee_under_scan.annual_salary
        self.employee_under_scan.give_raise()
        default_increased_annual_salary = previous_anuual_salary + 5000
        self.assertEqual(default_increased_annual_salary,self.employee_under_scan.annual_salary)

    def test_give_coustom_raise(self):
        """Test to check default increament in salary did not happen 
        instead a coustom increament of salary took place """
        self.employee_under_scan = Employee("radha ramann","jha",504000)
        # self.employee_under_scan.salary_info_of_employee()
        previous_annual_salary = self.employee_under_scan.annual_salary
        self.employee_under_scan.give_raise(200000)
        coustom_increased_salary = previous_annual_salary + 200000
        self.assertEqual(coustom_increased_salary,self.employee_under_scan.annual_salary)

    

if __name__ == "__main__":
    unittest.main()