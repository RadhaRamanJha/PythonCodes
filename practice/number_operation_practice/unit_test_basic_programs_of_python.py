import unittest
from basic_programs_of_python import basic_programs

class BasicProgramTest(unittest.TestCase):
    """Unit Tests for entire basic_program class"""
    def setUp(self):
       """Creates an instance of basic programs (bp)"""
       self.bp = basic_programs()

    """Unit tests for sum of two numbers"""
    def test_numbers_sum(self):
        """1.verify normal behaviour of  'numbers_sum' function"""
        self.assertEqual(9,self.bp.numbers_sum(4,5))
    def test_number_sum_str_args(self):
        """2.verify exception being thrown by 'numbers_sum' function"""
        self.assertRaises(Exception,self.bp.numbers_sum,'A','B')

    """Unit tests for finding maximum of two numbers"""
    def test_max_number(self):
        """3.verify normal behaviour of  'max_number' function"""
        self.assertEqual(108,self.bp.max_number(102,108))
    def test_max_number_str_args(self):
        """4.Test to verify exception being thrown by 'max_number' function"""
        self.assertRaises(Exception,self.bp.max_number,'a','d')

    """Unit test for factorial of numbers"""
    def test_factorial(self):
        """5.A test to verify normal behaviour of 'factorial' function for 0 value"""
        self.assertEqual(1,self.bp.factorial(0))
    def test_factorial_negative_args(self):
        """6.Test to verify exception being thrown by 'factorial' function' for -ve arguments"""
        self.assertRaises(Exception,self.bp.factorial,-1)
    def test_factorial_str_args(self):
        """7.Test to verify exception being thrown by 'factorial' function' for str arguments"""
        self.assertRaises(TypeError,self.bp.factorial,'a')

    """Unit tests for simple interest calculation"""
    def test_simple_interest_calculation(self):
        """8.Checks the calculation of Simple interest"""
        self.assertEqual(1000,self.bp.simple_interest_calculation(10000,5,2))
    def test_simple_interest_exception_principal(self):
        """9.Checks the simple interest function returns error for string principal value"""
        self.assertRaises(Exception,self.bp.simple_interest_calculation,'p',5,2)
    def test_simple_interest_exception_time(self):
        """10.Checks the simple interest function returns error for string time value"""
        self.assertRaises(Exception,self.bp.simple_interest_calculation,10000,5,'2')
    def test_simple_interest_exception_rate(self):
        """11.Checks the simple interest function returns error for string rate value"""
        self.assertRaises(Exception,self.bp.simple_interest_calculation,10000,'5',2)

    """Unit tests for compound interest calculation"""
    def test_compound_intrest_calculation(self):
        """12.Checks the calculation of compound interest"""
        self.assertEqual(1025,self.bp.compound_intrest_calculation(10000,5,2))
    def test_compound_interest_exception_principal(self):
        """13.Checks the compound interest function returns error for string principal value"""
        self.assertRaises(Exception,self.bp.compound_intrest_calculation,'10000',5,2)
    def test_compound_interest_exception_time(self):
        """14.Checks the compound interest function returns error for string time value"""
        self.assertRaises(Exception,self.bp.compound_intrest_calculation,10000,5,'2')
    def test_compound_interest_exception_rate(self):
        """15.Checks the compound interest function returns error for string rate value"""
        self.assertRaises(Exception,self.bp.compound_intrest_calculation,10000,'5',2)

    """Unit tests for is armstrong numbers verification"""    
    def test_is_armstrong(self):
        """16.Checks the test for armmstrong number"""
        self.assertTrue(self.bp.is_armstrong(153)) 
    def test_is_armstrong_returns_false(self):
        """17.Checks the test for armstrong number fails"""
        self.assertFalse(self.bp.is_armstrong(152))
    def test_is_armstrong_returns_exception_float(self):
        """18.Checks the test for armstrong number returns exception for float"""
        self.assertRaises(Exception,self.bp.is_armstrong,12.5)
    def test_is_armstrong_returns_exception_string(self):
        """19.Checks the test for armstrong number returns exception for string"""
        self.assertRaises(Exception,self.bp.is_armstrong,'153')
    
    """Unit tests for circle area calulation"""
    def test_find_circle_area(self):
        """20.Checks function returns correct area of circle"""
        self.assertEqual(314,self.bp.find_circle_area(10))
    def test_find_circle_area_float(self):
        """21.Checks function returns correct area of circle float radius"""
        self.assertEqual(346.185,self.bp.find_circle_area(10.5))
    def test_circle_area_value_error(self):
        """22.Checks function raises value error for negative circle radius"""
        self.assertRaises(ValueError,self.bp.find_circle_area,-10)
    def test_circle_area_exception(self):
        """23.Checks function raises exception for string circle radius"""
        self.assertRaises(Exception,self.bp.find_circle_area,'10')
        
    """Unit tests for is_prime"""
    def test_is_number_prime(self):
        """24.Verifies the prime number is detected"""
        self.assertTrue(self.bp.is_number_prime(7))
    def test_number_not_prime(self):
        """25.Verifies non prime number returns false"""
        self.assertFalse(self.bp.is_number_prime(6))
    def test_0_not_prime(self):
        """26.Verifies 0 is returned as non-prime nummber"""
        self.assertFalse(self.bp.is_number_prime(0))
    def test_1_not_prime(self):
        """27.Verifies 1 is returned as non-prime nummber"""
        self.assertFalse(self.bp.is_number_prime(1))
    def test_str_not_prime(self):
        """28.Verifies 'str' input throws an exception"""
        self.assertRaises(Exception,self.bp.is_number_prime,'12')

    """Unit tests for fibbonaci number"""
    def test_fibbonaci_num(self):
        """29.Test the return of correct fibbonaci number"""
        self.assertEqual(8,self.bp.fibbonaci_number(7))
    def test_fibbonani_neg_num(self):
        """30.Test to check function raises value error for negative arg num"""
        self.assertRaises(ValueError,self.bp.fibbonaci_number,-1)
    def test_fibbo_float_num(self):
        """31.Checks function raises value error for float num"""
        self.assertRaises(Exception,self.bp.fibbonaci_number,1.2)
    def test_fibbonani_str_num(self):
        """32.Checks function raises exception for str arg num"""
        self.assertRaises(Exception,self.bp.fibbonaci_number,'1')

    """Unit tests for checking number is fibbonaci"""
    def test_is_fibbonaci_number(self):
        """33.Tests fibbonaci number wheter fibbonaci number being detected """
        self.assertTrue(self.bp.is_fibbonaci_number(8))
    def test_is_not_fibbonaci_number(self):
        """34.Tests fibbonaci number wheter fibbonaci number being detected """
        self.assertFalse(self.bp.is_fibbonaci_number(9))
    def test_is_fibbo_raise_execption_neg_number(self):
        """35.Checks is_fibbo function raises exception for negative number"""
        self.assertRaises(ValueError,self.bp.is_fibbonaci_number,-1)
    def test_is_fibbo_raise_execption_str_number(self):
        """36.Checks is_fibbo function raises exception for str number"""
        self.assertRaises(Exception,self.bp.is_fibbonaci_number,'1')
    
    """Unit tests for determing position of 'k'th multiple of 'n' in fibbo series"""
    def test_position_in_fibbonaci_series(self):
        """37.Checks if true position of number in fibbonaci series being returned"""
        self.assertEqual(7,self.bp.position_in_fibbonaci_series(2,2))
    def test_pos_fibbo_raise_typeerror_float_k(self):
        """38.Position in fibbo raises type error for float k value"""
        self.assertRaises(TypeError,self.bp.position_in_fibbonaci_series,7,2.5)
    def test_pos_fibbo_raise_typeerror_str_k(self):
        """39.Position in fibbo raises type error for str k value"""
        self.assertRaises(TypeError,self.bp.position_in_fibbonaci_series,7,'2')
    def test_pos_fibbo_raise_typeerror_float_n(self):
        """40.Position in fibbo raises exception for float n value"""
        self.assertRaises(Exception,self.bp.position_in_fibbonaci_series,7.2,2)
    def test_pos_fibbo_raise_typeerror_str_n(self):
        """41.Position in fibbo raises exception for str n value"""
        self.assertRaises(Exception,self.bp.position_in_fibbonaci_series,'7',2)
    
    """Unit tests for square sum of 'n' natural numbers"""
    def test_square_sum_of_n_natural_numbers(self):
        """42.Checks wheter true sum of squares being returned"""
        self.assertEqual(5,self.bp.square_sum_of_n_natural_numbers(2))
    def test_sq_sum_returns_value_error_neg_num(self):
        """43.Checks sum of square returns value error for neg num"""
        self.assertRaises(ValueError,self.bp.square_sum_of_n_natural_numbers,-23)
    def test_sq_sum_returns_0_num(self):
        """44.Verifies 0 as sum for 0 natural numbers"""
        self.assertEqual(0,self.bp.square_sum_of_n_natural_numbers(0))
    def test_sq_sum_raises_exception_for_float_input(self):
        """45.Verifies excetion raised for float number enterd"""
        self.assertRaises(Exception,self.bp.square_sum_of_n_natural_numbers,2.3)
    def test_sq_sum_raises_exception_for_str_input(self):
        """46.Verifies excetion raised for str number enterd"""
        self.assertRaises(Exception,self.bp.square_sum_of_n_natural_numbers,'2')
    
    """Unit tests for cube sum of 'n' natural numbers"""
    def test_cube_sum_of_n_natural_numbers(self):
        """47.Checks wheter true sum of cubes being returned"""
        self.assertEqual(9,self.bp.cube_sum_of_n_natural_numbers(2))
    def test_cube_n_nat_num_0(self):
        """48.Verifies 0 is sum for adding 0 nat num"""
        self.assertEqual(0,self.bp.cube_sum_of_n_natural_numbers(0))
    def test_cube_neg_n_nat_num(self):
        """49.Verifies value error raised for nat num entered as negative value"""
        self.assertRaises(ValueError,self.bp.cube_sum_of_n_natural_numbers,-3)
    def test_cube_float_n_nat_numm(self):
        """50.Verifies exception raised for float num entered"""
        self.assertRaises(Exception,self.bp.cube_sum_of_n_natural_numbers,2.5)
    def test_cube_str_n_nat_numm(self):
        """51.Verifies exception raised for str num entered"""
        self.assertRaises(Exception,self.bp.cube_sum_of_n_natural_numbers,'34')

if __name__ == '__main__':
    unittest.main()