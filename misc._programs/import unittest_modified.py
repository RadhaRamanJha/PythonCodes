import unittest
from city_founction import city_description 

class CitiesTestCase(unittest.TestCase):
    def test_city_country_population(self):
        formatted_city_name = city_description("santiago","chile", 5000000)
        self.assertEqual(formatted_city_name,f"Santiago, Chile, population = 5000000")
    def test_city_country(self):
        formatted_city_name = city_description("santiago","chile")
        self.assertEqual(formatted_city_name,"Santiago, Chile, population = 5000000")
    def test_city_country_population_india(self):
        formatted_city_name = city_description("delhi","india", 20000000)
        self.assertEqual(formatted_city_name,f"Delhi, India, population = 10000000")
        
if __name__== "__main__":
    unittest.main()