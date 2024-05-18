#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""TestExpression.py

Unittest for the Expression class.
"""

import os
import sys
import unittest
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from symclone.Expression import Expression

class TestExpression(unittest.TestCase):

    def test_evaluate(self):
        expr = Expression('x**2 + 2*x + 1')
        self.assertEqual(expr.evaluate({'x': 3}), 16.0)

    def test_substitute(self):
        expr = Expression('x**2 + 2*x + 1')
        substituted_expr = expr.substitute({'x': 2})
        self.assertEqual(str(substituted_expr), '2**2 + 2*2 + 1')

    def test_derivative(self):
        expr = Expression('x**2 + 2*x + 1')
        derivative_expr = expr.derivative('x')
        self.assertEqual(str(derivative_expr), '2*x + 2')

if __name__ == '__main__':
    unittest.main()
