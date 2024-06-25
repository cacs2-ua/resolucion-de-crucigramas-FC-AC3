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
    
    def test_initialize_1_isolated_variables(self):
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        expected = [
            ["-", 1, (2, 1), (2, 1), 1, "isolated", [], {}, {}],
            ["-", 2, (3, 2), (3, 2), 1, "isolated", [], {}, {}]
        ]
        real = initialize_1_isolated_variables(board)
        
        self.assertEqual(len(real), len(expected))
        
        for real_word, expected_word in zip(real, expected):
            self.assertEqual(real_word.value, expected_word[0])
            self.assertEqual(real_word.name, expected_word[1])
            self.assertEqual(real_word.initial_pos, expected_word[2])
            self.assertEqual(real_word.final_pos, expected_word[3])
            self.assertEqual(real_word.length, expected_word[4])
            self.assertEqual(real_word.orientation, expected_word[5])
            self.assertEqual(real_word.feasibles, expected_word[6])
            self.assertEqual(real_word.pounds, expected_word[7])
            self.assertEqual(real_word.restrictions, expected_word[8])
            
    def test_2_initialize_1_isolated_variables(self):
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        expected = [
            Word("-", 1, (2, 1), (2, 1), 1, "isolated"),
            Word("-", 2, (3, 2), (3, 2), 1, "isolated")
        ]
        real = initialize_1_isolated_variables(board)
        
        self.assertEqual(expected, real)
    
    def test_1_initialize_1_horizontal_variables(self):
        board = Tablero(file_path='tests/resources/Boards_Examples/horizontal1.txt')
        expected = [
            Word("-", 3, (0,2), (0, 3), 2, "horizontal"), #1
            Word("-", 4, (1,2), (1, 5), 4, "horizontal"), #2
            Word("-", 5, (2,3), (2, 5), 3, "horizontal"), #3
            Word("-", 6, (3,4), (3, 5), 2, "horizontal"), #4
            Word("-", 7, (4,0), (4, 1), 2, "horizontal"), #5
            Word("-", 8, (4,3), (4, 5), 3, "horizontal"), #6
        ]
        real = initialize_1_horizontal_variables(board, 2)
        
        self.assertEqual(expected, real)
        


if __name__ == '__main__':
    unittest.main()