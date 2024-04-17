import unittest
from symclone import Symbol

class TestSymbol(unittest.TestCase):
    def test_name(self):
        symbol = Symbol('x')
        self.assertEqual(symbol.name, 'x')

if __name__ == '__main__':
    unittest.main()
