#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Symbol.py

Unittest for the Symbol class.
"""

import os
import sys
import unittest
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from symclone.Symbol import Symbol

class TestSymbol(unittest.TestCase):

    def test_name(self):
        symbol = Symbol('x')
        self.assertEqual(symbol.name, 'x')

if __name__ == '__main__':
    unittest.main()
