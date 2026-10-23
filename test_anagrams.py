import anagrams
import unittest

class TestAnagrams(unittest.TestCase):
    def test_anagrams_basic(self):
        self.assertEqual(anagrams.anagrams('hello', 'llohe'), True)
        self.assertEqual(anagrams.anagrams('hello', 'llohee'), False)
    
    def test_anagrams_empty(self):
        self.assertEqual(anagrams.anagrams('', ''), True)

    def test_anagrams_case(self):
        self.assertEqual(anagrams.anagrams('Hello', 'llohe'), True)
    
    def test_anagrams_spaces(self):
        self.assertEqual(anagrams.anagrams('hello world', 'worldhello'), True)
    
    def test_anagrams_punctuation(self):
        self.assertEqual(anagrams.anagrams('hello, world', 'worldhello'), True)
    
    def test_anagrams_long(self):
        with open('tests/hamlet.txt', 'r') as file:
            long_string = file.read()
        long_string_reversed = long_string[::-1]
        self.assertEqual(anagrams.anagrams(long_string, long_string_reversed), True)
    
    def test_has_docstring(self):
        self.assertIsNotNone(anagrams.anagrams.__doc__)