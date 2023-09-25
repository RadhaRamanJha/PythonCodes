import unittest
from name_founction import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name_founction.py"""

    def test_first_last_name(self):
        """Does names like 'Ravi Sharma' work?"""
        formatted_name = get_formatted_name('ravi','sharma')
        self.assertEqual(formatted_name,"Ravi Sharma")

    def test_first_middle_last_name(self):
        """Does names like 'Narendarbhai Damodardas Modi' work"""
        formatted_name = get_formatted_name('narendarbhai','modi','damodardas')
        self.assertEqual(formatted_name,"Narendarbhai Damodardas Modi")

if __name__ == "__main__":
    unittest.main()