import unittest
from symclone import FuzzyBoolean

class TestFuzzyBoolean(unittest.TestCase):
    def test_and(self):
        a = FuzzyBoolean(0.6)
        b = FuzzyBoolean(0.4)
        result = a & b
        self.assertEqual(result.value, 0.4)

    def test_or(self):
        a = FuzzyBoolean(0.6)
        b = FuzzyBoolean(0.4)
        result = a | b
        self.assertEqual(result.value, 0.6)

    def test_not(self):
        a = FuzzyBoolean(0.6)
        result = ~a
        self.assertEqual(result.value, 0.4)

if __name__ == '__main__':
    unittest.main()
