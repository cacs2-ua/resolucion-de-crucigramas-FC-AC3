import unittest
from copy import deepcopy
from variable import *

class TestWordInitialization(unittest.TestCase):
    
    def test_initialization(self):
        name = "test_word"
        initial_pos = (0, 0)
        final_pos = (0, 4)
        length = 5
        orientation = "horizontal"
        feasibles = ["apple", "apply", "apron"]
        
        word = Word(name, initial_pos, final_pos, length, orientation, feasibles)
        
        self.assertEqual(word.value, "-")
        self.assertEqual(word.name, name)
        self.assertEqual(word.initial_pos, initial_pos)
        self.assertEqual(word.final_pos, final_pos)
        self.assertEqual(word.length, length)
        self.assertEqual(word.orientation, orientation)
        self.assertEqual(word.feasibles, feasibles)
        self.assertEqual(word.pounds, [])
        self.assertEqual(word.restrictions, [])
        
if __name__ == '__main__':
    unittest.main()
