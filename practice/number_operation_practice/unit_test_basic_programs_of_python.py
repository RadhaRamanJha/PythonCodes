import unittest
from basic_programs_of_python import basic_programs

class BasicProgramTest(unittest.TestCase):
    # def setUpClass(self):
    #    """Creates an instance of basic programs (bp)"""
    #    print("setUp Class called")
    # def tearDownClass(self):
    #    """Creates an instance of basic programs (bp)"""
    #    print("tearDown Class called\n")
    """Unit Tests for entire basic_program class"""
    def setUp(self):
       """Creates an instance of basic programs (bp)"""
    #    print("setup called")
       self.bp = basic_programs()
    # def tearDown(self):
       """Creates an instance of basic programs (bp)"""
       print("tearDown called\n")

    def test_numbers_sum(self):
        """A Test to verify normal behaviour of  'numbers_sum' function"""
        self.assertEqual(9,self.bp.numbers_sum(4,5))
    def test_number_sum_str_args(self):
        """Test to verify exception being thrown by 'numbers_sum' function"""
        self.assertRaises(Exception,self.bp.numbers_sum,('A','B'))

    def test_max_number(self):
        """A Test to verify normal behaviour of  'max_number' function"""
        self.assertEqual(108,self.bp.max_number(102,108))
    def test_max_number_str_args(self):
        """Test to verify exception being thrown by 'max_number' function"""
        self.assertRaises(Exception,self.bp.max_number,('a','d'))

    def test_factorial(self):
        """A test to verify normal behaviour of 'factorial' function for 0 value"""
        self.assertEqual(1,self.bp.factorial(0))
    def test_factorial_negative_args(self):
        """Test to verify exception being thrown by 'factorial' function' for -ve arguments"""
        self.assertRaises(Exception,self.bp.factorial,-1)
    def test_factorial_str_args(self):
        """Test to verify exception being thrown by 'factorial' function' for str arguments"""
        self.assertRaises(Exception,self.bp.factorial,'a')
    def test_factorial_(self):
        """A test to verify normal behaviour of 'factorial' function"""
        self.assertEqual(120,self.bp.factorial(5))

    def test_simple_interest_calculation(self):
        """Checks the calculation of Simple interest"""
        self.assertEqual(1000,self.bp.simple_interest_calculation(10000,5,2))
    
    def test_compound_intrest_calculation(self):
        """Checks the calculation of Simple interest"""
        self.assertEqual(1025,self.bp.compound_intrest_calculation(10000,5,2))
    
    def test_is_armstrong(self):
        """Checks the test for armmstrong number"""
        self.assertTrue(self.bp.is_armstrong(153))
        
    def test_is_armstrong_returns_false(self):
        """Checks the test for armstrong number fails"""
        self.assertFalse(self.bp.is_armstrong(152))

    def test_find_circle_area(self):
        """Checks the area of circle"""
        self.assertEqual(314,self.bp.find_circle_area(10))

    def test_negative_radius_exception_circle_area(self):
        """Checks the return in case of negative radius"""
        self.assertRaises(ValueError,self.bp.find_circle_area,-23)

    def test_string_radius_error_circle_area(self):
        """Checks the retuen in case string value of radius provided"""
        self.assertRaises(TypeError,self.bp.find_circle_area,'abc')
    
    def test_is_number_prime(self):
        """Verifies the prime number is detected"""
        self.assertTrue(self.bp.is_number_prime(7))

    def test_fibbonaci_number(self):
        """Test the return of correct fibbonaci number"""
        self.assertEqual(8,self.bp.fibbonaci_number(7))

    def test_is_fibbonaci_number(self):
        """Tests fibbonaci number wheter fibbonaci number being detected """
        self.assertTrue(self.bp.is_fibbonaci_number(8))
    
    def test_is_not_fibbonaci_number(self):
        """Tests fibbonaci number wheter fibbonaci number being detected """
        self.assertFalse(self.bp.is_fibbonaci_number(9))
    
    def test_position_in_fibbonaci_series(self):
        """Checks if true position of number in fibbonaci series being returned"""
        self.assertEqual(7,self.bp.position_in_fibbonaci_series(2,2))
        print("test fibo test")
    
    def test_square_sum_of_n_natural_numbers(self):
        """Checks wheter true sum of squares being returned"""
        self.assertEqual(5,self.bp.square_sum_of_n_natural_numbers(2))
        print("test square test")
    
    def test_cube_sum_of_n_natural_numbers(self):
        """Checks wheter true sum of cubes being returned"""
        self.assertEqual(9,self.bp.cube_sum_of_n_natural_numbers(2))
        print("test cube test")


if __name__ == '__main__':
    unittest.main()