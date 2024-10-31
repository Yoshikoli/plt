import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phase(self):
        piglatin = PigLatin()
        piglatin.set_phrase("hello world", "hello world")
        self.assertEqual("hello world", piglatin.translate("hello world"))

    def test_translate_an_empty_phase(self):
        piglatin = PigLatin()
        piglatin.set_phrase("", "nil")
        self.assertEqual("nil", piglatin.translate(""))

    def test_translate_a_word_starting_with_vowel(self):
        piglatin = PigLatin()
        piglatin.set_phrase("any", "anynay")
        piglatin.set_phrase("apple", "appleyay")
        piglatin.set_phrase("ask", "askay")
        self.assertEqual("anynay", piglatin.translate("any"))
        self.assertEqual("appleyay", piglatin.translate("apple"))
        self.assertEqual("askay", piglatin.translate("ask"))

