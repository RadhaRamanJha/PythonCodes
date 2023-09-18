from random import randint
class Die:
    def __init__(self, num_sides = 6):
        """Creates a six-faced die if 'num_sides' is not mentioned"""
        self.num_sides = num_sides
    def roll(self):
        """Return a random value from 1 to number of sides of Die"""
        return(randint(1, self.num_sides)) # Name of a 6 faced die will be D6, for an 8 Faced die will be D8 so on 
    