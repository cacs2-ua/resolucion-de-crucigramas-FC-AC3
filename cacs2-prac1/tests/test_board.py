import unittest
import tempfile
import os
from tablero import *

class TestTablero(unittest.TestCase):

    def setUp(self):
        # Create a temporary file with board content
        self.test_file_content = (
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
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.test_file.write(self.test_file_content)
        self.test_file.seek(0)

    def tearDown(self):
        self.test_file.close()
        os.unlink(self.test_file.name)

    def test_load_from_file(self):
        tablero = Tablero(file_path=self.test_file.name)
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

    def test_set_from_file(self):
        tablero = Tablero(10, 10)
        tablero.set_from_file(self.test_file.name)
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

if __name__ == '__main__':
    unittest.main()
