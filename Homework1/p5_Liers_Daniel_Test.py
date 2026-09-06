
import unittest
from p5_Liers_Daniel import (
    caesar_cipher,
    caesar_decipher,
    letter_frequency
)


class TestCaesarCipher(unittest.TestCase):

    def test_cipher_basic(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

    def test_cipher_wraparound(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc")

    def test_cipher_uppercase(self):
        self.assertEqual(caesar_cipher("ABC", 2), "CDE")

    def test_cipher_mixed_case(self):
        self.assertEqual(
            caesar_cipher("Hello World", 3),
            "Khoor Zruog"
        )

    def test_decipher(self):
        encrypted = caesar_cipher("Python", 5)
        self.assertEqual(
            caesar_decipher(encrypted, 5),
            "Python"
        )

    def test_frequency_simple(self):
        freq = letter_frequency("hello")

        self.assertEqual(freq["h"], 1)
        self.assertEqual(freq["e"], 1)
        self.assertEqual(freq["l"], 2)
        self.assertEqual(freq["o"], 1)

    def test_frequency_ignore_case(self):
        freq = letter_frequency("AaBbCc")

        self.assertEqual(freq["a"], 2)
        self.assertEqual(freq["b"], 2)
        self.assertEqual(freq["c"], 2)

    def test_frequency_ignore_symbols(self):
        freq = letter_frequency("A! A?")

        self.assertEqual(freq["a"], 2)


if __name__ == "__main__":
    unittest.main()