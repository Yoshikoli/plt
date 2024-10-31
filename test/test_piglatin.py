import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phase(self):
        piglatin = PigLatin()
        piglatin.get_phrase("hello world", "hello world")

    def test_translate_an_empty_phase(self):
        piglatin = PigLatin()
        piglatin.translate("nil", "")

    def test_translate_a_word_starting_with_vowel(self):
        piglatin = PigLatin()
        piglatin.translate("anynay", "any")
        piglatin.translate("appleyay", "apple")
        piglatin.translate("askay", "ask")

    def test_translating_a_word_starting_with_a_single_consonant(self):
        piglatin = PigLatin()
        piglatin.translate("ellohay", "hello")


