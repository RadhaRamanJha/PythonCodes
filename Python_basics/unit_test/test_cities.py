import unittest
from city_function import city_description 

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_name = city_description("santiago","chile")
        self.assertEqual(formatted_city_name,"Santiago, Chile, population = 5000000")

if __name__== "__main__":
    unittest.main()