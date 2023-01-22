import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french('Day'), 'Jour')
        self.assertEqual(english_to_french('Mother'), 'Mére')
        self.assertEqual(english_to_french(''), 'Please enter a text')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english('Jour'), 'Day')
        self.assertEqual(french_to_english('Mére'), 'Mother')
        self.assertEqual(french_to_english(''), 'Please enter a text')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')