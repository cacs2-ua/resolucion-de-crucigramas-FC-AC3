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
        
        expected_horizontals = [
            Word("-", 1, (0,2), (0, 3), 2, "horizontal"), #1
            Word("-", 2, (1,2), (1, 5), 4, "horizontal"), #2
            Word("-", 3, (2,3), (2, 5), 3, "horizontal"), #3
            Word("-", 4, (3,4), (3, 5), 2, "horizontal"), #4
            Word("-", 5, (4,0), (4, 1), 2, "horizontal"), #5
            Word("-", 6, (4,3), (4, 5), 3, "horizontal") #6
            ]
        expected_verticals = [ 
            Word("-", 7, (0,0), (1, 0), 2, "vertical"), #7
            Word("-", 8, (3,0), (4, 0), 2, "vertical"), #8
            Word("-", 9, (0,2), (1, 2), 2, "vertical"), #9
            Word("-", 10, (0,3), (2, 3), 3, "vertical"), #10
            Word("-", 11, (1,4), (4, 4), 4, "vertical"), #11
            Word("-", 12, (0,5), (4, 5), 5, "vertical") #12
            ]
        expected_isolated = [ 
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_all_variables(board)
        self.assertEqual(expected_horizontals, real["horizontal"])
        self.assertEqual(expected_verticals, real["vertical"])
        self.assertEqual(expected_isolated, real["isolated"])


    def test_initialize_2_all_variables(self): # Test 21
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_vertical_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_vertical_variables)
        
        expected_verticals = [
            Word("-", 1, (0,0), (1, 0), 2, "vertical"), #1
            Word("-", 2, (3,0), (4, 0), 2, "vertical"), #2
            Word("-", 3, (0,2), (1, 2), 2, "vertical"), #3
            Word("-", 4, (0,3), (2, 3), 3, "vertical"), #4
            Word("-", 5, (1,4), (4, 4), 4, "vertical"), #5
            Word("-", 6, (0,5), (4, 5), 5, "vertical")  #6
            ]
            
        expected_horizontals = [
            Word("-", 7, (0,2), (0, 3), 2, "horizontal"), #7
            Word("-", 8, (1,2), (1, 5), 4, "horizontal"), #8
            Word("-", 9, (2,3), (2, 5), 3, "horizontal"), #9
            Word("-", 10, (3,4), (3, 5), 2, "horizontal"), #10
            Word("-", 11, (4,0), (4, 1), 2, "horizontal"), #11
            Word("-", 12, (4,3), (4, 5), 3, "horizontal"), #12
            ]
        expected_isolated = [
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated") #14
            ]
        
        real = initialize_2_all_variables(board)
        self.assertEqual(expected_verticals, real["vertical"])
        self.assertEqual(expected_horizontals, real["horizontal"])
        self.assertEqual(expected_isolated, real["isolated"])
        

    def test_initialize_3_all_variables(self): # Test 22
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_horizontal_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_horizontal_variables)
        
        expected_horizontals = [
            Word("-", 1, (0,2), (0, 3), 2, "horizontal"), #1
            Word("-", 2, (1,2), (1, 5), 4, "horizontal"), #2
            Word("-", 3, (2,3), (2, 5), 3, "horizontal"), #3
            Word("-", 4, (3,4), (3, 5), 2, "horizontal"), #4
            Word("-", 5, (4,0), (4, 1), 2, "horizontal"), #5
            Word("-", 6, (4,3), (4, 5), 3, "horizontal") #6
            ]
        expected_verticals = [ 
            Word("-", 7, (0,0), (1, 0), 2, "vertical"), #7
            Word("-", 8, (3,0), (4, 0), 2, "vertical"), #8
            Word("-", 9, (0,2), (1, 2), 2, "vertical"), #9
            Word("-", 10, (0,3), (2, 3), 3, "vertical"), #10
            Word("-", 11, (1,4), (4, 4), 4, "vertical"), #11
            Word("-", 12, (0,5), (4, 5), 5, "vertical") #12
            ]
        expected_isolated = [ 
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated"), #14
        ]
        real = initialize_1_all_variables(board)
        self.assertEqual(expected_horizontals, real["horizontal"])
        self.assertEqual(expected_verticals, real["vertical"])
        self.assertEqual(expected_isolated, real["isolated"])

    def test_initialize_4_all_variables(self): # Test 23
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_vertical_variables = []
        initialize_1_horizontal_variables(board, 0, list_of_vertical_variables)
        
        expected_verticals = [
            Word("-", 1, (0,0), (1, 0), 2, "vertical"), #1
            Word("-", 2, (3,0), (4, 0), 2, "vertical"), #2
            Word("-", 3, (0,2), (1, 2), 2, "vertical"), #3
            Word("-", 4, (0,3), (2, 3), 3, "vertical"), #4
            Word("-", 5, (1,4), (4, 4), 4, "vertical"), #5
            Word("-", 6, (0,5), (4, 5), 5, "vertical")  #6
            ]
            
        expected_horizontals = [
            Word("-", 7, (0,2), (0, 3), 2, "horizontal"), #7
            Word("-", 8, (1,2), (1, 5), 4, "horizontal"), #8
            Word("-", 9, (2,3), (2, 5), 3, "horizontal"), #9
            Word("-", 10, (3,4), (3, 5), 2, "horizontal"), #10
            Word("-", 11, (4,0), (4, 1), 2, "horizontal"), #11
            Word("-", 12, (4,3), (4, 5), 3, "horizontal"), #12
            ]
        expected_isolated = [
            Word("-", 13, (2,1), (2, 1), 1, "isolated"), #13
            Word("-", 14, (3,2), (3, 2), 1, "isolated") #14
            ]
        
        real = initialize_2_all_variables(board)
        self.assertEqual(expected_verticals, real["vertical"])
        self.assertEqual(expected_horizontals, real["horizontal"])
        self.assertEqual(expected_isolated, real["isolated"])

    def test_create_storage_with_hash_table(self): # Test 24
        filename = 'd0.txt'
        
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
    


    def test_initialize_feasibles_v1(self): # Test 25
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        list_of_variables = initialize_1_all_variables(board)
        filename = 'd0.txt'
        dictionary_of_domains = create_storage_with_hash_table(filename)
        
        variable_1_feasibles = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        variable_2_feasibles = ['ESTO', 'PARA', 'COMO', 'ROSA', 'OLOR', 'LALA', 'PERO', 'OSOS', 'PERA']
        variable_3_feasibles = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA']
        variable_4_feasibles = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        variable_5_feasibles = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        variable_6_feasibles = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA']
        
        variable_7_feasibles = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        variable_8_feasibles = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        variable_9_feasibles = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        variable_10_feasibles = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA']
        variable_11_feasibles = ['ESTO', 'PARA', 'COMO', 'ROSA', 'OLOR', 'LALA', 'PERO', 'OSOS', 'PERA']
        variable_12_feasibles = ['TOTEM', 'OSERA', 'RETOS', 'SETOS', 'ESOPO']
        
        variable_13_feasibles = ['L', 'A', 'B']
        variable_14_feasibles = ['L', 'A', 'B']
        
        expected_horizontals = [
            Word("-", 1, (0,2), (0, 3), 2, "horizontal", 
                 feasibles= variable_1_feasibles), #1
            Word("-", 2, (1,2), (1, 5), 4, "horizontal", 
                 feasibles= variable_2_feasibles), #2
            Word("-", 3, (2,3), (2, 5), 3, "horizontal", 
                 feasibles= variable_3_feasibles), #3
            Word("-", 4, (3,4), (3, 5), 2, "horizontal",
                 feasibles= variable_4_feasibles), #4
            Word("-", 5, (4,0), (4, 1), 2, "horizontal",
                 feasibles=variable_5_feasibles), #5
            Word("-", 6, (4,3), (4, 5), 3, "horizontal",
                 feasibles= variable_6_feasibles), #6
            ]
        
        expected_verticals = [
            Word("-", 7, (0,0), (1, 0), 2, "vertical",
                feasibles= variable_7_feasibles), #7
            Word("-", 8, (3,0), (4, 0), 2, "vertical",
                feasibles= variable_8_feasibles), #8
            Word("-", 9, (0,2), (1, 2), 2, "vertical",
                feasibles= variable_9_feasibles), #9
            Word("-", 10, (0,3), (2, 3), 3, "vertical",
                feasibles= variable_10_feasibles), #10
            Word("-", 11, (1,4), (4, 4), 4, "vertical",
                variable_11_feasibles), #11
            Word("-", 12, (0,5), (4, 5), 5, "vertical",
                feasibles=variable_12_feasibles) #12
            ]
    
        expected_isolated = [
        Word("-", 13, (2,1), (2, 1), 1, "isolated", 
                feasibles= variable_13_feasibles), #13
        Word("-", 14, (3,2), (3, 2), 1, "isolated",
                feasibles= variable_14_feasibles), #14
        ]
        
        real = initialize_feasibles_v1(board, dictionary_of_domains, list_of_variables)
        self.assertEqual(expected_horizontals, real["horizontal"])
        self.assertEqual(expected_verticals, real["vertical"])
        self.assertEqual(expected_isolated, real["isolated"])
    
    def test_get_initial_letters(self): # Test 26
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        #my_dict = {'key1': value1, 'key2': value2, 'key3': value3}
        expected_dict = {
                         (0, 0): "E",
                         (1, 3): "V",
                         (1, 5): "S",
                         (2, 4): "S",
                         (3, 5): "N",
                         (4, 1): "O"
                         }
        real_dict = get_initial_letters(board)
        self.assertEqual(expected_dict, real_dict)
    
    def test_square_belongs_to_word(self): # Test 27
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        hash_table_of_variables = initialize_1_all_variables(board)
        
        self.assertTrue(square_belongs_to_word(1, 3, 
                                hash_table_of_variables["horizontal"][1]))
        
        self.assertTrue(square_belongs_to_word(1, 5, 
                                hash_table_of_variables["horizontal"][1]))
        
        self.assertTrue(square_belongs_to_word(2, 4, 
                                hash_table_of_variables["horizontal"][2]))
        
        self.assertTrue(square_belongs_to_word(3, 5, 
                                hash_table_of_variables["horizontal"][3]))
        
        self.assertTrue(square_belongs_to_word(4, 1, 
                                hash_table_of_variables["horizontal"][4]))
        
        self.assertTrue(square_belongs_to_word(4, 4, 
                                hash_table_of_variables["horizontal"][5]))
        
        self.assertTrue(square_belongs_to_word(0, 0, 
                                hash_table_of_variables["vertical"][0]))
        
        self.assertTrue(square_belongs_to_word(3, 0, 
                                hash_table_of_variables["vertical"][1]))
        
        self.assertTrue(square_belongs_to_word(0, 2, 
                                hash_table_of_variables["vertical"][2]))
        
        self.assertTrue(square_belongs_to_word(1, 3, 
                                hash_table_of_variables["vertical"][3]))
        
        self.assertFalse(square_belongs_to_word(2, 1, 
                                hash_table_of_variables["horizontal"][3]))
        
    def test_initialize_restrictions_v1(self): # Test 28
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        
        hash_table_of_variables = initialize_1_all_variables(board)
        
        filename = 'd0.txt'
        hash_table_of_domains = create_storage_with_hash_table(filename)
        
        initialize_feasibles_v1(board, hash_table_of_domains, hash_table_of_variables)
        
        initial_letters_hash_map = get_initial_letters(board)
                
        expected_horizontal_2_restriction = {2: 
            [Restriction(hash_table_of_variables["horizontal"][1],
                         hash_table_of_variables["horizontal"][1], 
                         1, 3, "V"),
             Restriction(hash_table_of_variables["horizontal"][1], 
                         hash_table_of_variables["horizontal"][1],
                         1, 5, "S")]}
        
        expected_horizontal_3_restriction = {3: 
            [Restriction(hash_table_of_variables["horizontal"][2],
                         hash_table_of_variables["horizontal"][2], 
                         2, 4, "S")]}
        
        expected_vertical_4_restriction = {10: 
            [Restriction(hash_table_of_variables["vertical"][3],
                         hash_table_of_variables["vertical"][3], 
                         1, 3, "V")]}
        
        expected_vertical_5_restriction = {11: 
            [Restriction(hash_table_of_variables["vertical"][4],
                         hash_table_of_variables["vertical"][4], 
                         2, 4, "S")]}
        
        expected_vertical_6_restriction = {12: 
            [Restriction(hash_table_of_variables["vertical"][5],
                         hash_table_of_variables["vertical"][5], 
                         1, 5, "S"),
             Restriction(hash_table_of_variables["vertical"][5],
                         hash_table_of_variables["vertical"][5], 
                         3, 5, "N")]}
        
        
        
        expected_horizontal_6_restriction = {}
        
        expected_isolated_1_restriction = {}
        
        expected_isolated_2_restriction = {}
        
        expected_horizontal_2_feasibles = ['ESTO', 'PARA', 'COMO', 'ROSA', 'OLOR', 'LALA', 'PERO', 'OSOS', 'PERA']
        expected_horizontal_3_feasibles = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA']
        expected_horizontal_6_feasibles = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA']
        
        expected_vertical_4_feasibles = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA']
        expected_vertical_5_feasibles = ['ESTO', 'PARA', 'COMO', 'ROSA', 'OLOR', 'LALA', 'PERO', 'OSOS', 'PERA']
        expected_vertical_6_feasibles = ['TOTEM', 'OSERA', 'RETOS', 'SETOS', 'ESOPO']
        
        expected_isolated_1_feasibles = ['L', 'A', 'B']
        expected_isolated_2_feasibles = ['L', 'A', 'B']
        
        
        expected_horizontal_2 = Word(
            value="-", name = 2, initial_pos= (1, 2), final_pos= (1, 5),
            length= 4, orientation= "horizontal", 
            feasibles = expected_horizontal_2_feasibles,
            restrictions = expected_horizontal_2_restriction
            )
        
        expected_horizontal_3 = Word(
            value="-", name = 3, initial_pos= (2, 3), final_pos= (2, 5),
            length= 3, orientation= "horizontal", 
            feasibles = expected_horizontal_3_feasibles,
            restrictions = expected_horizontal_3_restriction
            )
        
        expected_horizontal_6 = Word(
            value="-", name = 6, initial_pos= (4, 3), final_pos= (4, 5),
            length= 3, orientation= "horizontal", 
            feasibles = expected_horizontal_6_feasibles,
            restrictions = expected_horizontal_6_restriction
            )
        
        expected_vertical_4 = Word(
            value="-", name = 10, initial_pos= (0, 3), final_pos= (2, 3),
            length= 3, orientation= "vertical", 
            feasibles = expected_vertical_4_feasibles,
            restrictions = expected_vertical_4_restriction
            )
        
        expected_vertical_5 = Word(
            value="-", name = 11, initial_pos= (1, 4), final_pos= (4, 4),
            length= 4, orientation= "vertical", 
            feasibles = expected_vertical_5_feasibles,
            restrictions = expected_vertical_5_restriction
            )
        
        expected_vertical_6 = Word(
            value="-", name = 12, initial_pos= (0, 5), final_pos= (4, 5),
            length= 5, orientation= "vertical", 
            feasibles = expected_vertical_6_feasibles,
            restrictions = expected_vertical_6_restriction
            )
        
        expected_isolated_1 = Word(
            value="-", name = 13, initial_pos= (2, 1), final_pos= (2, 1),
            length= 1, orientation= "isolated", 
            feasibles = expected_isolated_1_feasibles,
            restrictions = expected_isolated_1_restriction
            )
        
        expected_isolated_2 = Word(
            value="-", name = 14, initial_pos= (3, 2), final_pos= (3, 2),
            length= 1, orientation= "isolated", 
            feasibles = expected_isolated_2_feasibles,
            restrictions = expected_isolated_2_restriction
            )
        
        initialize_restrictions_v1(board, initial_letters_hash_map, hash_table_of_variables)
        
        real_horizontal_2 = hash_table_of_variables["horizontal"][1]
        real_horizontal_3 = hash_table_of_variables["horizontal"][2]
        real_horizontal_6 = hash_table_of_variables["horizontal"][5]
        
        real_vertical_4 = hash_table_of_variables["vertical"][3]
        real_vertical_5 = hash_table_of_variables["vertical"][4]
        real_vertical_6 = hash_table_of_variables["vertical"][5]

        real_isolated_1 = hash_table_of_variables["isolated"][0]
        real_isolated_2 = hash_table_of_variables["isolated"][1]
        
        self.assertEqual(expected_horizontal_2, real_horizontal_2)
        self.assertEqual(expected_horizontal_3, real_horizontal_3)
        self.assertEqual(expected_horizontal_6, real_horizontal_6)
        
        self.assertEqual(expected_vertical_4, real_vertical_4)
        self.assertEqual(expected_vertical_5, real_vertical_5)
        self.assertEqual(expected_vertical_6, real_vertical_6)
        
        self.assertEqual(expected_isolated_1, real_isolated_1)
        self.assertEqual(expected_isolated_2, real_isolated_2)  

    
    def test_count_number_of_variables(self): # Test 29
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        
        expected_number = 14
        
        real = initialize_1_all_variables(board)
        real_number = count_number_of_variables(real)
        
        self.assertEqual(expected_number, real_number)
    
    def test_count_number_of_horizontal_variables(self): # Test 30
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        
        expected_number = 6
        
        real = initialize_1_all_variables(board)
        real_number = count_number_of_horizontal_variables(real)
        
        self.assertEqual(expected_number, real_number)
    
    def test_count_number_of_vertical_variables(self): # Test 31
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        
        expected_number = 6
        
        real = initialize_1_all_variables(board)
        real_number = count_number_of_vertical_variables(real)
        
        self.assertEqual(expected_number, real_number)
    
    def test_count_number_of_isolated_variables(self): # Test 32
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        
        expected_number = 2
        
        real = initialize_1_all_variables(board)
        real_number = count_number_of_isolated_variables(real)
        
        self.assertEqual(expected_number, real_number)
        
    
    def test_get_common_square_coordinates_from_two_variables(self): # Test 33
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        hash_map_of_variables = initialize_1_all_variables(board)
        
        expected_square_1 = (2, 4)
        expected_square_2 = (3, 5)
        expected_square_3 = None
        expected_square_4 = (2, 1)
        expected_square_5 = None
        expected_square_6 = None
        expected_square_7 = None
        
        horizontal_variable_3 = hash_map_of_variables["horizontal"][2]
        vertical_variable_5 = hash_map_of_variables["vertical"][4]
        
        horizontal_variable_4 = hash_map_of_variables["horizontal"][3]
        vertical_variable_6 = hash_map_of_variables["vertical"][5]
        
        horizontal_variable_5 = hash_map_of_variables["horizontal"][4]
        vertical_variable_1 = hash_map_of_variables["vertical"][0]
        
        isolated_variable_1 = hash_map_of_variables["isolated"][0]
        isolated_variable_2 = hash_map_of_variables["isolated"][1]
        
        real_square_1 = get_common_square_coordinates_from_two_variables(
            horizontal_variable_3, 
            vertical_variable_5)
        
        real_square_2 = get_common_square_coordinates_from_two_variables(
            horizontal_variable_4, 
            vertical_variable_6)
        
        real_square_3 = get_common_square_coordinates_from_two_variables(
            horizontal_variable_5, 
            vertical_variable_1)
        
        real_square_4 = get_common_square_coordinates_from_two_variables(
            isolated_variable_1, 
            isolated_variable_1)
        
        real_square_5 = get_common_square_coordinates_from_two_variables(
            isolated_variable_1, 
            isolated_variable_2)
        
        real_square_6 = get_common_square_coordinates_from_two_variables(
            horizontal_variable_5, 
            horizontal_variable_3)
        
        real_square_7 = get_common_square_coordinates_from_two_variables(
            vertical_variable_1, 
            vertical_variable_5)
        
        
        self.assertEqual(expected_square_1, real_square_1)
        self.assertEqual(expected_square_2, real_square_2)
        self.assertEqual(expected_square_3, real_square_3)
        self.assertEqual(expected_square_4, real_square_4)
        self.assertEqual(expected_square_5, real_square_5)
        self.assertEqual(expected_square_6, real_square_6)
        self.assertEqual(expected_square_7, real_square_7)
    
    def test_ok_restriction_between_two_variables(self): # Test 34
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        hash_map_of_variables = initialize_1_all_variables(board)
        
        expected_ok_restriction_1 = True
        expected_ok_restriction_2 = True
        expected_ok_restriction_3 = True
        expected_ok_restriction_4 = True
        expected_ok_restriction_5 = True
        expected_ok_restriction_6 = True
        expected_ok_restriction_7 = True
        
        expected_ok_restriction_8 = True
        
        expected_ok_restriction_9 = False
        expected_ok_restriction_10 = False
        
        expected_ok_restriction_11 = True
        
        horizontal_variable_2 = hash_map_of_variables["horizontal"][1]
        horizontal_variable_2.set_value("ATAS")
        vertical_variable_6 = hash_map_of_variables["vertical"][5]
        feasible_1 = "ESOPO"
        
        
        
        horizontal_variable_3 = hash_map_of_variables["horizontal"][2]
        horizontal_variable_3.set_value("ASI")
        vertical_variable_5 = hash_map_of_variables["vertical"][4]
        feasible_2 = "OSOS"
        
        vertical_variable_1 = hash_map_of_variables["vertical"][0]
        feasible_3 = "LO"
        
        feasible_4 = "LOS"
        
        feasible_5 = "OSERA"
        
        isolated_variable_1 = hash_map_of_variables["isolated"][0]
        isolated_variable_2 = hash_map_of_variables["isolated"][1]
        
        feasible_6 = "O"
        
        real_ok_restriction_1 = ok_restriction_between_two_variables(
            board,
            horizontal_variable_2, 
            vertical_variable_6, 
            feasible_1
            )
        
        real_ok_restriction_2 = ok_restriction_between_two_variables(
            board,
            horizontal_variable_3, 
            vertical_variable_5, 
            feasible_2
            )
        
        vertical_variable_5.set_value("OSOS")
        real_ok_restriction_11 = ok_restriction_between_two_variables(
            board,
            vertical_variable_5,
            horizontal_variable_3, 
            "ESE"
            )
        
        self.assertEqual(expected_ok_restriction_11, real_ok_restriction_11)
        
        vertical_variable_5.set_value("-")
                
        real_ok_restriction_3 = ok_restriction_between_two_variables(
            board,
            horizontal_variable_3, 
            vertical_variable_1, 
            feasible_3
            )
        
        real_ok_restriction_4 = ok_restriction_between_two_variables(
            board,
            horizontal_variable_2, 
            horizontal_variable_3, 
            feasible_4
            )
        
        real_ok_restriction_5 = ok_restriction_between_two_variables(
            board,
            vertical_variable_5, 
            vertical_variable_6, 
            feasible_5
            )
        
        real_ok_restriction_6 = ok_restriction_between_two_variables(
            board,
            horizontal_variable_3, 
            horizontal_variable_3, 
            feasible_4
            )
        
        real_ok_restriction_7 = ok_restriction_between_two_variables(
            board,
            vertical_variable_6, 
            vertical_variable_6, 
            feasible_5
            )
        
        real_ok_restriction_8 = ok_restriction_between_two_variables(
            board,
            isolated_variable_1, 
            isolated_variable_2, 
            feasible_5
            )
        
        
        self.assertEqual(expected_ok_restriction_1, real_ok_restriction_1)
        self.assertEqual(expected_ok_restriction_2, real_ok_restriction_2)
        self.assertEqual(expected_ok_restriction_3, real_ok_restriction_3)
        self.assertEqual(expected_ok_restriction_4, real_ok_restriction_4)
        self.assertEqual(expected_ok_restriction_5, real_ok_restriction_5)
        self.assertEqual(expected_ok_restriction_6, real_ok_restriction_6)
        self.assertEqual(expected_ok_restriction_7, real_ok_restriction_7)
        self.assertEqual(expected_ok_restriction_8, real_ok_restriction_8)
        
        horizontal_variable_2.set_value("MAPA")
        
        real_ok_restriction_9 = ok_restriction_between_two_variables(
            board,
            horizontal_variable_2, 
            vertical_variable_6, 
            feasible_1
            )
        
        self.assertEqual(expected_ok_restriction_9, real_ok_restriction_9)
        
        feasible_2 = "OZAL"
        
        real_ok_restriction_10 = ok_restriction_between_two_variables(
            board,
            horizontal_variable_3, 
            vertical_variable_5, 
            feasible_2
            )
        
        self.assertEqual(expected_ok_restriction_10, real_ok_restriction_10)
    
    def test_2_ok_restriction_between_two_variables(self): # Test 35
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        hash_map_of_variables = initialize_1_all_variables(board)
        
        expected_ok_restriction_1 = True
        expected_ok_restriction_2 = True
        
        expected_ok_restriction_3 = False
        
        vertical_variable_4 = hash_map_of_variables["vertical"][3]
        vertical_variable_4.set_value("UVE")
        horizontal_variable_2 = hash_map_of_variables["horizontal"][1]
        feasible_1 = "AVES"
        
        vertical_variable_6 = hash_map_of_variables["vertical"][5]
        vertical_variable_6.set_value("ASILO")
        horizontal_variable_6 = hash_map_of_variables["horizontal"][5]
        feasible_2 = "ALO"
        
        vertical_variable_2 = hash_map_of_variables["vertical"][1]
        vertical_variable_2.set_value("LO")
        horizontal_variable_5 = hash_map_of_variables["horizontal"][4]
        feasible_3 = "AL"
        
        real_ok_restriction_1 = ok_restriction_between_two_variables(
            board,
            vertical_variable_4, 
            horizontal_variable_2, 
            feasible_1
            )
        
        real_ok_restriction_2 = ok_restriction_between_two_variables(
            board,
            vertical_variable_6, 
            horizontal_variable_6, 
            feasible_2
            )
        
        real_ok_restriction_3 = ok_restriction_between_two_variables(
            board,
            vertical_variable_2, 
            horizontal_variable_5, 
            feasible_3
            )
        
        
        self.assertEqual(expected_ok_restriction_1, real_ok_restriction_1)
        self.assertEqual(expected_ok_restriction_2, real_ok_restriction_2)
        self.assertEqual(expected_ok_restriction_3, real_ok_restriction_3)
        
        expected_ok_restriction_4 = False
        
        vertical_variable_3 = hash_map_of_variables["vertical"][2]
        vertical_variable_3.set_value("NO")
        horizontal_variable_2 = hash_map_of_variables["horizontal"][1]
        feasible_4 = "HOLA"
        
        real_ok_restriction_4 = ok_restriction_between_two_variables(
            board,
            vertical_variable_3, 
            horizontal_variable_2, 
            feasible_4
            )
        self.assertEqual(expected_ok_restriction_4, real_ok_restriction_4)
    
    def test_add_restriction(self): # Test 36
        word1 = Word(value="hello", name=1, initial_pos=(0, 0), final_pos=(0, 4), length=5, orientation="horizontal")
        word2 = Word(value="world", name=2, initial_pos=(0, 0), final_pos=(4, 0), length=5, orientation="vertical")
        restriction = Restriction(word_restricted=word1, word_restrainer=word2, x_coordinate=0, y_coordinate=0, letter_of_restriction='h')
        
        word1.add_restriction(restriction)
        
        self.assertIn(2, word1.get_restrictions())
        self.assertIn(restriction, word1.get_restrictions()[2])
        self.assertEqual(word1.get_restrictions()[2][0].get_letter_of_restriction(), 'h')

    def test_add_pound(self): # Test 37
        word1 = Word(value="hello", name=1, initial_pos=(0, 0), final_pos=(0, 4), length=5, orientation="horizontal")
        word2 = Word(value="world", name=2, initial_pos=(0, 0), final_pos=(4, 0), length=5, orientation="vertical")
        pound = "LOPEZ"
        
        word1.add_pound(word2, pound)
        
        self.assertIn(2, word1.get_pounds())
        self.assertIn(pound, word1.get_pounds()[2])
        self.assertEqual(word1.get_pounds()[2][0], pound)
    
    def test_remove_pound(self): # Test 38
        word1 = Word(name=1)
        word2 = Word(name=2)
        word3 = Word(name=3)
        
        expected_pound_1 = {2 : ["LOPEZ"]}
        word1.add_pound(word2, "LOPEZ")
        real_pound_1 = word1.get_pounds()
        
        self.assertEqual(expected_pound_1, real_pound_1)
        
        expected_pound_2 = {}
        word1.remove_pound(word2, "LOPEZ")
        real_pound_2 = word1.get_pounds()
        
        self.assertEqual(expected_pound_2, real_pound_2)
        
        expected_pound_3 = {2 : ["LOPEZ", "HOLA"]}
        word1.add_pound(word2, "LOPEZ")
        word1.add_pound(word2, "HOLA")
        real_pound_3 = word1.get_pounds()
        
        self.assertEqual(expected_pound_3, real_pound_3)
        
    def test_1_forward(self): # Test 39
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        hash_table_of_variables = initialize_1_all_variables(board)
        filename = 'tests/resources/Boards_Examples/d0-forward-test1.txt'
        hash_table_of_domains = create_storage_with_hash_table(filename)
        initialize_feasibles_v1(board, hash_table_of_domains, hash_table_of_variables)
        
        initial_letters_hash_map = get_initial_letters(board)
        initialize_restrictions_v1(board, initial_letters_hash_map, hash_table_of_variables)
        
        horiziontal_variable_restrainer_3 = hash_table_of_variables["horizontal"][2]
        vertical_variable_restricted_5 = hash_table_of_variables["vertical"][4]
        
        expected_pounded_domain_1 = ['ESTO', 'OSOS']
        
        horiziontal_variable_restrainer_3.set_value("OSO")
        expected_result = True
        real_result = forward(board, horiziontal_variable_restrainer_3, hash_table_of_variables)
        
        self.assertEqual(expected_result, real_result)
        real_pounded_domain_1 = hash_table_of_variables["vertical"][4].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_1, real_pounded_domain_1)
        
        expected_pounded_domain_2 = ['AVO']
        real_pounded_domain_2 = hash_table_of_variables["vertical"][3].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_2, real_pounded_domain_2)
        
        expected_pounded_domain_3 = ['ESOPO']
        real_pounded_domain_3 = hash_table_of_variables["vertical"][5].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_3, real_pounded_domain_3)
        
        expected_pounded_domain_4 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        real_pounded_domain_4 = hash_table_of_variables["vertical"][0].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_4, real_pounded_domain_4)
        
        expected_pounded_domain_5 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        real_pounded_domain_5 = hash_table_of_variables["vertical"][1].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_5, real_pounded_domain_5)
        
        expected_pounded_domain_6 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        real_pounded_domain_6 = hash_table_of_variables["vertical"][2].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_6, real_pounded_domain_6)
        
        
        expected_pounded_domain_7 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        real_pounded_domain_7 = hash_table_of_variables["horizontal"][0].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_7, real_pounded_domain_7)
        
        expected_pounded_domain_8 = ['ESTO', 'PARA', 'COMO', 'ROSA', 'OLOR', 'LALA', 'PERO', 'OSOS', 'PERA']
        real_pounded_domain_8 = hash_table_of_variables["horizontal"][1].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_8, real_pounded_domain_8)
        
        expected_pounded_domain_9 = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA', 'AVO']
        real_pounded_domain_9 = hash_table_of_variables["horizontal"][2].get_feasibles()
        self.assertEqual(expected_pounded_domain_9, real_pounded_domain_9)
        
        expected_pounded_domain_10 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        real_pounded_domain_10 = hash_table_of_variables["horizontal"][3].get_feasibles()
        self.assertEqual(expected_pounded_domain_10, real_pounded_domain_10)
        
        expected_pounded_domain_11 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR']
        real_pounded_domain_11 = hash_table_of_variables["horizontal"][4].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_11, real_pounded_domain_11)
        
        expected_pounded_domain_12 = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA', 'AVO']
        real_pounded_domain_12 = hash_table_of_variables["horizontal"][5].get_feasibles()
        self.assertEqual(expected_pounded_domain_12, real_pounded_domain_12)
        
        expected_pounded_domain_13 = ['L', 'A', 'B']
        real_pounded_domain_13 = hash_table_of_variables["isolated"][0].get_feasibles()
        self.assertEqual(expected_pounded_domain_13, real_pounded_domain_13)
        
        expected_pounded_domain_14 = ['L', 'A', 'B']
        real_pounded_domain_14 = hash_table_of_variables["isolated"][0].get_feasibles()
        self.assertEqual(expected_pounded_domain_14, real_pounded_domain_14)


    def test_2_forward(self):  # Test 40
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        hash_table_of_variables = initialize_1_all_variables(board)
        filename = 'tests/resources/Boards_Examples/d0-forward-test2.txt'
        hash_table_of_domains = create_storage_with_hash_table(filename)
        initialize_feasibles_v1(board, hash_table_of_domains, hash_table_of_variables)
        
        initial_letters_hash_map = get_initial_letters(board)
        initialize_restrictions_v1(board, initial_letters_hash_map, hash_table_of_variables)
        
        vertical_variable_restrainer_5 = hash_table_of_variables["vertical"][4]
        horizontal_variable_restricted_6 = hash_table_of_variables["horizontal"][5]
        
        expected_pounded_domain_1 = ['CON', 'ROL', 'RON', 'SOL']
        
        vertical_variable_restrainer_5.set_value("ISLO")
        b = hash_table_of_variables["horizontal"][1]
        a = forward(board, vertical_variable_restrainer_5, hash_table_of_variables)
        
        real_pounded_domain_1 = hash_table_of_variables["horizontal"][5].get_feasibles()
        
        self.assertEqual(expected_pounded_domain_1, real_pounded_domain_1)
        
        expected_pounded_domain_2 = ['LA', 'LN']
        real_pounded_domain_2 = hash_table_of_variables["horizontal"][3].get_feasibles()
        self.assertEqual(expected_pounded_domain_2, real_pounded_domain_2)
        
        expected_pounded_domain_3 = ['ASA']
        real_pounded_domain_3 = hash_table_of_variables["horizontal"][2].get_feasibles()
        self.assertEqual(expected_pounded_domain_3, real_pounded_domain_3)
        
        expected_pounded_domain_4 = ['AVIS']
        real_pounded_domain_4 = hash_table_of_variables["horizontal"][1].get_feasibles()
        self.assertEqual(expected_pounded_domain_4, real_pounded_domain_4)
        
        expected_pounded_domain_5 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR', 'LN']
        real_pounded_domain_5 = hash_table_of_variables["horizontal"][4].get_feasibles()
        self.assertEqual(expected_pounded_domain_5, real_pounded_domain_5)
        
        expected_pounded_domain_6 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR', 'LN']
        real_pounded_domain_6 = hash_table_of_variables["horizontal"][0].get_feasibles()
        self.assertEqual(expected_pounded_domain_6, real_pounded_domain_6)
        
        expected_pounded_domain_7 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR', 'LN']
        real_pounded_domain_7 = hash_table_of_variables["vertical"][0].get_feasibles()
        self.assertEqual(expected_pounded_domain_7, real_pounded_domain_7)
        
        expected_pounded_domain_8 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR', 'LN']
        real_pounded_domain_8 = hash_table_of_variables["vertical"][1].get_feasibles()
        self.assertEqual(expected_pounded_domain_8, real_pounded_domain_8)
        
        expected_pounded_domain_9 = ['ES', 'UN', 'DE', 'LA', 'NO', 'AR', 'LN']
        real_pounded_domain_9 = hash_table_of_variables["vertical"][2].get_feasibles()
        self.assertEqual(expected_pounded_domain_9, real_pounded_domain_9)
        
        expected_pounded_domain_10 = ['CON', 'LAL', 'ROL', 'RON', 'OLA', 'SOL', 'ARA', 'AVO', 'ASA']
        real_pounded_domain_10 = hash_table_of_variables["vertical"][3].get_feasibles()
        self.assertEqual(expected_pounded_domain_10, real_pounded_domain_10)
        
        expected_pounded_domain_11 = ['ESTO', 'PARA', 'COMO', 'ROSA', 'OLOR', 'LALA', 'PERO', 'OSOS', 'PERA', 'AVIS']
        real_pounded_domain_11 = hash_table_of_variables["vertical"][4].get_feasibles()
        self.assertEqual(expected_pounded_domain_11, real_pounded_domain_11)
        
        expected_pounded_domain_12 = ['TOTEM', 'OSERA', 'RETOS', 'SETOS', 'ESOPO']
        real_pounded_domain_12 = hash_table_of_variables["vertical"][5].get_feasibles()
        self.assertEqual(expected_pounded_domain_12, real_pounded_domain_12)
        
        expected_pounded_domain_13 = ['L', 'A', 'B']
        real_pounded_domain_13 = hash_table_of_variables["isolated"][0].get_feasibles()
        self.assertEqual(expected_pounded_domain_13, real_pounded_domain_13)
        
        expected_pounded_domain_14 = ['L', 'A', 'B']
        real_pounded_domain_14 = hash_table_of_variables["isolated"][1].get_feasibles()
        self.assertEqual(expected_pounded_domain_14, real_pounded_domain_14)
        
    def test_pound_reflexive_restrictions(self): # Test 41
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1_v2.txt')
        hash_table_of_variables = initialize_1_all_variables(board)
        filename = 'tests/resources/Boards_Examples/d0.txt'
        hash_table_of_domains = create_storage_with_hash_table(filename)
        initialize_feasibles_v1(board, hash_table_of_domains, hash_table_of_variables)
        
        initial_letters_hash_map = get_initial_letters(board)
        initialize_restrictions_v1(board, initial_letters_hash_map, hash_table_of_variables)
        pound_reflexive_restrictions(hash_table_of_variables)
        
        
        expected_pounded_domain_1 = ['ESTO', 'OSOS']
        vertical_variable_restrainer_5 = hash_table_of_variables["vertical"][4]
        real_pounded_domain_1 = vertical_variable_restrainer_5.get_feasibles()
        

        
        self.assertEqual(expected_pounded_domain_1, real_pounded_domain_1)
        
        expected_pounded_domain_2 = ['NO']
        horizontal_variable_restrainer_5 = hash_table_of_variables["horizontal"][4]
        real_pounded_domain_2 = horizontal_variable_restrainer_5.get_feasibles()
        
        self.assertEqual(expected_pounded_domain_2, real_pounded_domain_2)
        
        expected_pounded_domain_3 = ['L']
        isolated_variable_restrainer_2 = hash_table_of_variables["isolated"][1]
        real_pounded_domain_3 = isolated_variable_restrainer_2.get_feasibles()
        
        self.assertEqual(expected_pounded_domain_3, real_pounded_domain_3)
        
        expected_pounded_domain_4 = ['L', 'A', 'B']
        isolated_variable_restrainer_1 = hash_table_of_variables["isolated"][0]
        real_pounded_domain_4 = isolated_variable_restrainer_1.get_feasibles()
        
        self.assertEqual(expected_pounded_domain_4, real_pounded_domain_4)
        
        
        
    def test_1_restore(self): # Test 42
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        hash_table_of_variables = initialize_1_all_variables(board)
        filename = 'tests/resources/Boards_Examples/d0-forward-test1.txt'
        hash_table_of_domains = create_storage_with_hash_table(filename)
        initialize_feasibles_v1(board, hash_table_of_domains, hash_table_of_variables)
        
        initial_letters_hash_map = get_initial_letters(board)
        initialize_restrictions_v1(board, initial_letters_hash_map, hash_table_of_variables)
        
        horizontal_variable_restrainer_3 = hash_table_of_variables["horizontal"][2]
        horizontal_variable_restrainer_3.set_value("OSO")
        vertical_variable_restricted_5 = hash_table_of_variables["vertical"][4]
        
        
        
        forward(board, horizontal_variable_restrainer_3, hash_table_of_variables)
        
        expected_feasible_1 = ['ESTO', 'OSOS']
        real_feasible_1 = hash_table_of_variables["vertical"][4].get_feasibles()
        self.assertEqual(expected_feasible_1, real_feasible_1)
        
        expected_pounded_1 = ['PARA', 'COMO', 'ROSA', 'OLOR', 'LALA', 'PERO', 'PERA']
        real_pounded_1 = hash_table_of_variables["vertical"][4].get_pounds()[3]
        self.assertEqual(expected_pounded_1, real_pounded_1)
        
        restore(board, horizontal_variable_restrainer_3, hash_table_of_variables)
        
        after_expected_feasible_1 = ['ESTO', 'OSOS', 'PARA', 'COMO', 'ROSA', 'OLOR', 'LALA', 'PERO', 'PERA']
        after_real_feasible_1 = hash_table_of_variables["vertical"][4].get_feasibles()
        self.assertEqual(after_expected_feasible_1, after_real_feasible_1)
        
        after_expected_pounded_1 = False
        real_expected_pounded_1 = 3 in hash_table_of_variables["vertical"][4].get_pounds()
        self.assertEqual(after_expected_pounded_1, real_expected_pounded_1)

    
    def test_2_restore(self): # Test 43
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1.txt')
        hash_table_of_variables = initialize_1_all_variables(board)
        filename = 'tests/resources/Boards_Examples/d0-forward-test2.txt'
        hash_table_of_domains = create_storage_with_hash_table(filename)
        initialize_feasibles_v1(board, hash_table_of_domains, hash_table_of_variables)
        
        initial_letters_hash_map = get_initial_letters(board)
        initialize_restrictions_v1(board, initial_letters_hash_map, hash_table_of_variables)
        
        vertical_variable_restrainer_5 = hash_table_of_variables["vertical"][4]
        vertical_variable_restrainer_5.set_value("ISLO")
        horizontal_variable_restricted_6 = hash_table_of_variables["horizontal"][5]
        
        forward(board, vertical_variable_restrainer_5, hash_table_of_variables)
        
        expected_feasible_1 = ['CON', 'ROL', 'RON', 'SOL']
        real_feasible_1 = hash_table_of_variables["horizontal"][5].get_feasibles()
        self.assertEqual(expected_feasible_1, real_feasible_1)
        
        expected_pounded_1 = ['LAL', 'OLA', 'ARA', 'AVO', 'ASA']
        real_pounded_1 = hash_table_of_variables["horizontal"][5].get_pounds()[11]
        self.assertEqual(expected_pounded_1, real_pounded_1)
        
        restore(board, vertical_variable_restrainer_5, hash_table_of_variables)
        
        after_expected_feasible_1 = ['CON', 'ROL', 'RON', 'SOL', 'LAL', 'OLA', 'ARA', 'AVO', 'ASA']
        after_real_feasible_1 = hash_table_of_variables["horizontal"][5].get_feasibles()
        self.assertEqual(after_expected_feasible_1, after_real_feasible_1)
        
        after_expected_pounded_1 = False
        real_expected_pounded_1 = 11 in hash_table_of_variables["horizontal"][5].get_pounds()
        self.assertEqual(after_expected_pounded_1, real_expected_pounded_1)
            
    def test_forward_checking(self): # Test 44
        board = Tablero(file_path='tests/resources/Boards_Examples/mine1_v2.txt')
        domains_route = 'tests/resources/Domains_Examples/mine_crossboard_ordered_domain_h_v_a.txt'
        debug_flag = True
        
        expected_board = store_crossboard(file_path='tests/resources/Boards_Examples/mine1_solution.txt')
        forward_checking(board, domains_route, debug_flag)
        real_board = tablero_to_2d_array(board)
        
        self.assertEqual(expected_board, real_board)
    
    
        

      
if __name__ == '__main__':
    unittest.main()