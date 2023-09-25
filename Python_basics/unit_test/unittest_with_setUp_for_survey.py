""" When a test case is running, Python prints one character for each unit test as it is
completed. A passing test prints a dot, a test that results in an error prints an E, and
a test that results in a failed assertion prints an F. This is why you’ll see a different
number of dots and characters on the first line of output when you run your test cases.
If a test case takes a long time to run because it contains many unit tests, you can
watch these results to get a sense of how many tests are passing."""

import unittest
from survey import AnonymusSurvey

class TestAnonymusSurvey(unittest.TestCase):
    """Tests for AnonymusSurvey """
    def setUp(self):
        """Create a survey and set of responses for use in all test methods"""
        question = "What is your native country ?"
        self.mysurvey = AnonymusSurvey(question)
        self.responses = ["India","Australia","South Africa","NewZeland","England"]
    
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.mysurvey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.mysurvey.responses)
    
    def test_store_five_responses(self):
        """Test that five individual responses are stored properly"""
        for response in self.responses:
            self.mysurvey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.mysurvey.responses)

if __name__ == "__main__":
    unittest.main()
