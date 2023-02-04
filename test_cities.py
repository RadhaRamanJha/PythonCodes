import unittest
from city_founction import city_description 

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_name = city_description("santiago","chile")
        self.assertEqual(formatted_city_name,"Santiago, Chile")
    
if __name__== "__main__":
    unittest.main()