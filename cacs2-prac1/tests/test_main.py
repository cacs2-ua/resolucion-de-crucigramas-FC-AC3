import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_substract(self):
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
    
    def test_is_outside_crossboard(self):
        # Initialize a board instance
        board = Tablero(FILS=3, COLS=3)
        
        # Test cases for is_outside_crossboard
        self.assertTrue(is_outside_crossboard(-1, 0, board))
        self.assertTrue(is_outside_crossboard(0, -1, board))
        self.assertTrue(is_outside_crossboard(3, 0, board))
        self.assertTrue(is_outside_crossboard(0, 3, board))
        
        self.assertFalse(is_outside_crossboard(0, 0, board))
        self.assertFalse(is_outside_crossboard(2, 2, board))
    
    def test_is_inside_crossboard(self):
        # Initialize a board instance
        board = Tablero(FILS=3, COLS=3)
        
        # Test cases for is_inside_crossboard
        self.assertFalse(is_inside_crossboard(-1, 0, board))
        self.assertFalse(is_inside_crossboard(0, -1, board))
        self.assertFalse(is_inside_crossboard(3, 0, board))
        self.assertFalse(is_inside_crossboard(0, 3, board))
        
        self.assertTrue(is_inside_crossboard(0, 0, board))
        self.assertTrue(is_inside_crossboard(2, 2, board))
    
    def test_is_solid(self):
        # Initialize a board instance
        board = Tablero(FILS=3, COLS=3)
        board.tablero = [
            ['*', '-', '-'],
            ['-', '*', '-'],
            ['-', '-', '*']
        ]
        
        # Test cases for is_solid
        self.assertTrue(is_solid(0, 0, board))
        self.assertTrue(is_solid(1, 1, board))
        self.assertTrue(is_solid(2, 2, board))
        
        self.assertFalse(is_solid(0, 1, board))
        self.assertFalse(is_solid(1, 0, board))
        self.assertFalse(is_solid(2, 1, board))
    
    def test_is_isolated(self):
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        self.assertTrue(is_isolated(2, 1, board))
        self.assertTrue(is_isolated(3, 2, board))
        self.assertFalse(is_isolated(1, 4, board))
        self.assertFalse(is_isolated(3, 3, board))
