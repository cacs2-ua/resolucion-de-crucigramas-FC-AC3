import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_substract(self): # Test 1
        self.assertEqual(substract(2, 3), -1)
        self.assertEqual(substract(-1, 1), -2)
        self.assertEqual(substract(0, 0), 0)
        
    def test_assertions(self): # Test 2
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIsNone(None)
        self.assertIsNotNone(1)
        self.assertIn(2, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
    
    def test_is_outside_crossboard(self): # Test 3
        # Initialize a board instance
        board = Tablero(FILS=3, COLS=3)
        
        # Test cases for is_outside_crossboard
        self.assertTrue(is_outside_crossboard(-1, 0, board))
        self.assertTrue(is_outside_crossboard(0, -1, board))
        self.assertTrue(is_outside_crossboard(3, 0, board))
        self.assertTrue(is_outside_crossboard(0, 3, board))
        
        self.assertFalse(is_outside_crossboard(0, 0, board))
        self.assertFalse(is_outside_crossboard(2, 2, board))
    
    def test_is_inside_crossboard(self): # Test 4
        # Initialize a board instance
        board = Tablero(FILS=3, COLS=3)
        
        # Test cases for is_inside_crossboard
        self.assertFalse(is_inside_crossboard(-1, 0, board))
        self.assertFalse(is_inside_crossboard(0, -1, board))
        self.assertFalse(is_inside_crossboard(3, 0, board))
        self.assertFalse(is_inside_crossboard(0, 3, board))
        
        self.assertTrue(is_inside_crossboard(0, 0, board))
        self.assertTrue(is_inside_crossboard(2, 2, board))
    
    def test_is_solid(self): # Test 5
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
    
    def test_is_isolated(self): # Test 6
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        self.assertTrue(is_isolated(2, 1, board))
        self.assertTrue(is_isolated(3, 2, board))
        self.assertFalse(is_isolated(1, 4, board))
        self.assertFalse(is_isolated(3, 3, board))
    
    def test_initialize_1_isolated_variables(self): # Test 7
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
            
    def test_2_initialize_1_isolated_variables(self): # Test 8
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        expected = [
            Word("-", 1, (2, 1), (2, 1), 1, "isolated"),
            Word("-", 2, (3, 2), (3, 2), 1, "isolated")
        ]
        real = initialize_1_isolated_variables(board)
        
        self.assertEqual(expected, real)
    
    def test_is_right_horizontal_terminal(self): # Test 9
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        self.assertTrue(is_right_horizontal_terminal(0, 5, board))
        self.assertTrue(is_right_horizontal_terminal(2, 1, board))
        self.assertTrue(is_right_horizontal_terminal(3, 2, board))
        
        self.assertFalse(is_right_horizontal_terminal(0, 2, board))
        self.assertFalse(is_right_horizontal_terminal(2, 3, board))
        self.assertFalse(is_right_horizontal_terminal(4, 4, board))
    
    def test_is_empty(self): # Test 10
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        
        self.assertTrue(is_empty(0, 2, board))
        self.assertTrue(is_empty(3, 0, board))
        self.assertTrue(is_empty(1, 4, board))
        
        self.assertFalse(is_empty(2, 2, board))
        self.assertFalse(is_empty(3, 1, board))
        self.assertFalse(is_empty(1, 6, board))
    
    def test_has_letter(self): # Test 11
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        
        self.assertTrue(has_letter(0, 0, board))
        self.assertTrue(has_letter(2, 4, board))
        self.assertTrue(has_letter(4, 1, board))
        
        self.assertFalse(has_letter(0, 1, board))
        self.assertFalse(has_letter(2, 1, board))
        self.assertFalse(has_letter(5, 2, board))

 
    def test_1_initialize_1_horizontal_variables(self): # Test 12
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
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
    
    def test_is_down_vertical_terminal(self): # Test 13
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        self.assertTrue(is_down_vertical_terminal(1, 0, board))
        self.assertTrue(is_down_vertical_terminal(4, 4, board))
        self.assertTrue(is_down_vertical_terminal(4, 5, board))
        
        self.assertFalse(is_down_vertical_terminal(2, 2, board))
        self.assertFalse(is_down_vertical_terminal(1, 8, board))
        self.assertFalse(is_down_vertical_terminal(0, 3, board))


    def test_1_initialize_1_vertical_variables(self): # Test 14
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        expected = [
            Word("-", 9, (0,0), (1, 0), 2, "vertical"), #1
            Word("-", 10, (3,0), (4, 0), 2, "vertical"), #2
            Word("-", 11, (0,2), (1, 2), 2, "vertical"), #3
            Word("-", 12, (0,3), (2, 3), 3, "vertical"), #4
            Word("-", 13, (1,4), (4, 4), 4, "vertical"), #5
            Word("-", 14, (0,5), (4, 5), 5, "vertical"), #6
        ]
        real = initialize_1_vertical_variables(board, 8)
    
        self.assertEqual(expected, real)
    
    def test_1_initialize_1_horizontal_and_isolated_variables(self): # Test 15
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_vertical_variables = []
        initialize_1_vertical_variables(board, 0, list_of_vertical_variables)

        expected = [
            Word("-", 1, (0,0), (1, 0), 2, "vertical"), #1
            Word("-", 2, (3,0), (4, 0), 2, "vertical"), #2
            Word("-", 3, (0,2), (1, 2), 2, "vertical"), #3
            Word("-", 4, (0,3), (2, 3), 3, "vertical"), #4
            Word("-", 5, (1,4), (4, 4), 4, "vertical"), #5
            Word("-", 6, (0,5), (4, 5), 5, "vertical"), #6
            Word("-", 7, (0,2), (0, 3), 2, "horizontal"), #7
            Word("-", 8, (1,2), (1, 5), 4, "horizontal"), #8
            Word("-", 9, (2,3), (2, 5), 3, "horizontal"), #9
            Word("-", 10, (3,4), (3, 5), 2, "horizontal"), #10
            Word("-", 11, (4,0), (4, 1), 2, "horizontal"), #11
            Word("-", 12, (4,3), (4, 5), 3, "horizontal"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_horizontal_and_isolated_variables(board, 6, list_of_vertical_variables= list_of_vertical_variables)
        print("")
        
        self.assertEqual(expected, real)
    
    def test_2_initialize_1_horizontal_and_isolated_variables(self): # Test 16
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_vertical_variables = []
        initialize_1_vertical_variables(board, 0, list_of_vertical_variables)

        expected = [
            Word("-", 1, (0,0), (1, 0), 2, "vertical"), #1
            Word("-", 2, (3,0), (4, 0), 2, "vertical"), #2
            Word("-", 3, (0,2), (1, 2), 2, "vertical"), #3
            Word("-", 4, (0,3), (2, 3), 3, "vertical"), #4
            Word("-", 5, (1,4), (4, 4), 4, "vertical"), #5
            Word("-", 6, (0,5), (4, 5), 5, "vertical"), #6
            Word("-", 7, (0,2), (0, 3), 2, "horizontal"), #7
            Word("-", 8, (1,2), (1, 5), 4, "horizontal"), #8
            Word("-", 9, (2,3), (2, 5), 3, "horizontal"), #9
            Word("-", 10, (3,4), (3, 5), 2, "horizontal"), #10
            Word("-", 11, (4,0), (4, 1), 2, "horizontal"), #11
            Word("-", 12, (4,3), (4, 5), 3, "horizontal"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_horizontal_and_isolated_variables(board, 6, list_of_vertical_variables= list_of_vertical_variables)
        print("")
        
        self.assertEqual(expected, real)
    
    def test_3_initialize_1_horizontal_and_isolated_variables(self): # Test 17
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_vertical_variables = []
        initialize_1_vertical_variables(board, 0, list_of_vertical_variables)

        expected = [
            Word("-", 1, (0,0), (1, 0), 2, "vertical"), #1
            Word("-", 2, (3,0), (4, 0), 2, "vertical"), #2
            Word("-", 3, (0,2), (1, 2), 2, "vertical"), #3
            Word("-", 4, (0,3), (2, 3), 3, "vertical"), #4
            Word("-", 5, (1,4), (4, 4), 4, "vertical"), #5
            Word("-", 6, (0,5), (4, 5), 5, "vertical"), #6
            Word("-", 7, (0,2), (0, 3), 2, "horizontal"), #7
            Word("-", 8, (1,2), (1, 5), 4, "horizontal"), #8
            Word("-", 9, (2,3), (2, 5), 3, "horizontal"), #9
            Word("-", 10, (3,4), (3, 5), 2, "horizontal"), #10
            Word("-", 11, (4,0), (4, 1), 2, "horizontal"), #11
            Word("-", 12, (4,3), (4, 5), 3, "horizontal"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_horizontal_and_isolated_variables(board, 6, list_of_vertical_variables= list_of_vertical_variables)
        print("")
        
        self.assertEqual(expected, real)
        
    def test_1_initialize_1_vertical_and_isolated_variables(self): # Test 18
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_horizontal_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_horizontal_variables)
        

        expected = [
            Word("-", 1, (0,2), (0, 3), 2, "horizontal"), #1
            Word("-", 2, (1,2), (1, 5), 4, "horizontal"), #2
            Word("-", 3, (2,3), (2, 5), 3, "horizontal"), #3
            Word("-", 4, (3,4), (3, 5), 2, "horizontal"), #4
            Word("-", 5, (4,0), (4, 1), 2, "horizontal"), #5
            Word("-", 6, (4,3), (4, 5), 3, "horizontal"), #6
            Word("-", 7, (0,0), (1, 0), 2, "vertical"), #7
            Word("-", 8, (3,0), (4, 0), 2, "vertical"), #8
            Word("-", 9, (0,2), (1, 2), 2, "vertical"), #9
            Word("-", 10, (0,3), (2, 3), 3, "vertical"), #10
            Word("-", 11, (1,4), (4, 4), 4, "vertical"), #11
            Word("-", 12, (0,5), (4, 5), 5, "vertical"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_vertical_and_isolated_variables(board, 6, list_of_horizontal_variables= list_of_horizontal_variables)
        print("")
        
        self.assertEqual(expected, real)
        
    def test_2_initialize_1_vertical_and_isolated_variables(self): # Test 19
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_horizontal_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_horizontal_variables)
        

        expected = [
            Word("-", 1, (0,2), (0, 3), 2, "horizontal"), #1
            Word("-", 2, (1,2), (1, 5), 4, "horizontal"), #2
            Word("-", 3, (2,3), (2, 5), 3, "horizontal"), #3
            Word("-", 4, (3,4), (3, 5), 2, "horizontal"), #4
            Word("-", 5, (4,0), (4, 1), 2, "horizontal"), #5
            Word("-", 6, (4,3), (4, 5), 3, "horizontal"), #6
            Word("-", 7, (0,0), (1, 0), 2, "vertical"), #7
            Word("-", 8, (3,0), (4, 0), 2, "vertical"), #8
            Word("-", 9, (0,2), (1, 2), 2, "vertical"), #9
            Word("-", 10, (0,3), (2, 3), 3, "vertical"), #10
            Word("-", 11, (1,4), (4, 4), 4, "vertical"), #11
            Word("-", 12, (0,5), (4, 5), 5, "vertical"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_vertical_and_isolated_variables(board, 6, list_of_horizontal_variables= list_of_horizontal_variables)
        print("")
        
        self.assertEqual(expected, real)

    def test_initialize_1_all_variables(self): # Test 20
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_horizontal_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_horizontal_variables)
        
        expected = [
            Word("-", 1, (0,2), (0, 3), 2, "horizontal"), #1
            Word("-", 2, (1,2), (1, 5), 4, "horizontal"), #2
            Word("-", 3, (2,3), (2, 5), 3, "horizontal"), #3
            Word("-", 4, (3,4), (3, 5), 2, "horizontal"), #4
            Word("-", 5, (4,0), (4, 1), 2, "horizontal"), #5
            Word("-", 6, (4,3), (4, 5), 3, "horizontal"), #6
            Word("-", 7, (0,0), (1, 0), 2, "vertical"), #7
            Word("-", 8, (3,0), (4, 0), 2, "vertical"), #8
            Word("-", 9, (0,2), (1, 2), 2, "vertical"), #9
            Word("-", 10, (0,3), (2, 3), 3, "vertical"), #10
            Word("-", 11, (1,4), (4, 4), 4, "vertical"), #11
            Word("-", 12, (0,5), (4, 5), 5, "vertical"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_all_variables(board)
        self.assertEqual(expected, real)

    def test_initialize_2_all_variables(self): # Test 21
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_vertical_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_vertical_variables)
        
        expected = [
            Word("-", 1, (0,0), (1, 0), 2, "vertical"), #1
            Word("-", 2, (3,0), (4, 0), 2, "vertical"), #2
            Word("-", 3, (0,2), (1, 2), 2, "vertical"), #3
            Word("-", 4, (0,3), (2, 3), 3, "vertical"), #4
            Word("-", 5, (1,4), (4, 4), 4, "vertical"), #5
            Word("-", 6, (0,5), (4, 5), 5, "vertical"), #6
            Word("-", 7, (0,2), (0, 3), 2, "horizontal"), #7
            Word("-", 8, (1,2), (1, 5), 4, "horizontal"), #8
            Word("-", 9, (2,3), (2, 5), 3, "horizontal"), #9
            Word("-", 10, (3,4), (3, 5), 2, "horizontal"), #10
            Word("-", 11, (4,0), (4, 1), 2, "horizontal"), #11
            Word("-", 12, (4,3), (4, 5), 3, "horizontal"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_2_all_variables(board)
        self.assertEqual(expected, real)

    def test_initialize_3_all_variables(self): # Test 22
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_horizontal_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_horizontal_variables)
        
        expected = [
            Word("-", 1, (0,2), (0, 3), 2, "horizontal"), #1
            Word("-", 2, (1,2), (1, 5), 4, "horizontal"), #2
            Word("-", 3, (2,3), (2, 5), 3, "horizontal"), #3
            Word("-", 4, (3,4), (3, 5), 2, "horizontal"), #4
            Word("-", 5, (4,0), (4, 1), 2, "horizontal"), #5
            Word("-", 6, (4,3), (4, 5), 3, "horizontal"), #6
            Word("-", 7, (0,0), (1, 0), 2, "vertical"), #7
            Word("-", 8, (3,0), (4, 0), 2, "vertical"), #8
            Word("-", 9, (0,2), (1, 2), 2, "vertical"), #9
            Word("-", 10, (0,3), (2, 3), 3, "vertical"), #10
            Word("-", 11, (1,4), (4, 4), 4, "vertical"), #11
            Word("-", 12, (0,5), (4, 5), 5, "vertical"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_all_variables(board)
        self.assertEqual(expected, real)

    def test_initialize_4_all_variables(self): # Test 23
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_vertical_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_vertical_variables)
        
        expected = [
            Word("-", 1, (0,0), (1, 0), 2, "vertical"), #1
            Word("-", 2, (3,0), (4, 0), 2, "vertical"), #2
            Word("-", 3, (0,2), (1, 2), 2, "vertical"), #3
            Word("-", 4, (0,3), (2, 3), 3, "vertical"), #4
            Word("-", 5, (1,4), (4, 4), 4, "vertical"), #5
            Word("-", 6, (0,5), (4, 5), 5, "vertical"), #6
            Word("-", 7, (0,2), (0, 3), 2, "horizontal"), #7
            Word("-", 8, (1,2), (1, 5), 4, "horizontal"), #8
            Word("-", 9, (2,3), (2, 5), 3, "horizontal"), #9
            Word("-", 10, (3,4), (3, 5), 2, "horizontal"), #10
            Word("-", 11, (4,0), (4, 1), 2, "horizontal"), #11
            Word("-", 12, (4,3), (4, 5), 3, "horizontal"), #12
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_2_all_variables(board)
        self.assertEqual(expected, real)
    
    def test_create_storage_with_hash_table(self):
        filename = 'd0.txt'
        with open(filename, 'w', encoding="utf-8") as f:
            f.write("Esto es un ejemplo de fichero de prueba para la practica con varias palabras de distinta longitud como totem osera l a b no rosa olor lal rol ron ola sol ara lala ar pero lotero retos setos osos lotera pera romano esopo romana")
        
        result = create_storage_with_hash_table(filename)
        
        # Check if all keys exist
        self.assertIn(4, result)
        self.assertIn(2, result)
        self.assertIn(5, result)
        self.assertIn(6, result)
        
        # Check if lengths are correct
        self.assertEqual(result[4].getTam(), 4)
        self.assertEqual(result[2].getTam(), 2)
        self.assertEqual(result[5].getTam(), 5)
        self.assertEqual(result[6].getTam(), 6)
        
        # Check if words are correctly added and uppercased
        self.assertIn('ESTO', result[4].getLista())
        self.assertIn('ES', result[2].getLista())
        self.assertIn('UN', result[2].getLista())
        self.assertIn('EJEMPLO', result[7].getLista())
        self.assertIn('PRACTICA', result[8].getLista())
        self.assertIn('TOTEM', result[5].getLista())
        
        # Check if duplicate words are not added
        self.assertEqual(result[4].getLista().count('PERO'), 1)
        self.assertEqual(result[2].getLista().count('LA'), 1)
        


if __name__ == '__main__':
    unittest.main()