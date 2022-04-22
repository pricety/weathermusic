import unittest

# from unittest.mock import MagicMock, patch
from app import valid_zip


class zipcode_test(unittest.TestCase):
    def test_empty(self):
        expected = False
        actual = valid_zip("")
        self.assertEqual(expected, actual)

    def test_let_zip(self):
        expected = False
        actual = valid_zip("abcde")
        self.assertEqual(expected, actual)

    def test_char_zip(self):
        expected = False
        actual = valid_zip("*&%^@")
        self.assertEqual(expected, actual)

    def test_badlen_zip(self):
        expected = False
        actual = valid_zip("3030")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
