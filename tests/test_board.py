import unittest
import tempfile
import os
from tablero import *

class TestTablero(unittest.TestCase):

    def get_temporary_file_content(self):
        # This function returns the temporary file content
        return (
            "---------\n"
            "-#######-\n"
            "-#######-\n"
            "-----###-\n"
            "-###-#---\n"
            "-----###-\n"
            "#####-###-\n"
            "##------#-\n"
            "#####-###-\n"
            "------###-\n"
        )

    def test_load_from_file(self):
        # Create a temporary file with board content
        test_file_content = self.get_temporary_file_content()
        test_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        test_file.write(test_file_content)
        test_file.close()

        tablero = Tablero(file_path=test_file.name)
        expected_board = [
            "---------",
            "-#######-",
            "-#######-",
            "-----###-",
            "-###-#---",
            "-----###-",
            "#####-###-",
            "##------#-",
            "#####-###-",
            "------###-"
        ]

        for i, line in enumerate(expected_board):
            for j, char in enumerate(line):
                self.assertEqual(tablero.getCelda(i, j), char)

        os.unlink(test_file.name)

    def test_set_from_file(self):
        # Create a temporary file with board content
        test_file_content = self.get_temporary_file_content()
        test_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        test_file.write(test_file_content)
        test_file.close()

        tablero = Tablero(10, 10)
        tablero.set_from_file(test_file.name)
        expected_board = [
            "---------",
            "-#######-",
            "-#######-",
            "-----###-",
            "-###-#---",
            "-----###-",
            "#####-###-",
            "##------#-",
            "#####-###-",
            "------###-"
        ]

        for i, line in enumerate(expected_board):
            for j, char in enumerate(line):
                self.assertEqual(tablero.getCelda(i, j), char)

        os.unlink(test_file.name)

if __name__ == '__main__':
    unittest.main()
