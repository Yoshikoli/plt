import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phase(self):
        piglatin = PigLatin()
        piglatin.get_phrase("hello world", "hello world")

