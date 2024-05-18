#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Symbol.py

Symbol class for the SymClone library.
"""

class Symbol:
    """Class to represent a symbolic variable."""
    
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Symbol('{self.name}')"
