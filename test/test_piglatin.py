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
        pass