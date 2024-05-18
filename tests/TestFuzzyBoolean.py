#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""TestFuzzyBoolean.py

Unittest for the FuzzyBoolean class.
"""

import os
import sys
import unittest
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from symclone.FuzzyBoolean import FuzzyBoolean

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
