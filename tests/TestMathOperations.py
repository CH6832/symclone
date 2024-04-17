import unittest
from symclone import MathOperations

class TestMathOperations(unittest.TestCase):
    def test_derivative(self):
        func = lambda x: x**2 + 2*x + 1
        result = MathOperations.derivative(func, 'x', 3)
        self.assertEqual(result, 8.0001)  # Approximately equal due to numerical differentiation

    def test_integral(self):
        func = lambda x: x**2 + 2*x + 1
        result = MathOperations.integral(func, 0, 1)
        self.assertEqual(result, 1.3333333333333333)  # Approximately equal due to numerical integration

if __name__ == '__main__':
    unittest.main()
