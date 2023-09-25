import unittest
from employee_info_blue_print import Employee

class employee_salary_raise_check_with_setup(unittest.TestCase):
    """Tests for check whether employee has got a default or costum salary raise"""
    def setUp(self):
        self.first_employee_of_concern = Employee("amit","singh",500000)
        self.second_employee_of_concern = Employee("gaurav","gupta",500000)

    def test_give_default_raise(self):
        expected_new_salary = self.first_employee_of_concern.annual_salary + 5000
        self.first_employee_of_concern.give_raise()
        self.assertEqual(expected_new_salary,self.first_employee_of_concern.annual_salary)
    
    def test_give_costum_raise(self):
        expected_new_salary = self.second_employee_of_concern.annual_salary + 200000
        self.second_employee_of_concern.give_raise(200000)
        self.assertEqual(expected_new_salary,self.second_employee_of_concern.annual_salary)

if __name__ == "__main__":
    unittest.main()