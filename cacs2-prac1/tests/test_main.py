import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(substract(2, 3), -1)
        self.assertEqual(substract(-1, 1), -2)
        self.assertEqual(substract(0, 0), 0)
        
    def test_assertions(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIsNone(None)
        self.assertIsNotNone(1)
        self.assertIn(2, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])