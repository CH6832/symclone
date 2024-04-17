#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""example_usage.py

Example usage of the SymClone library.
"""


# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled


import math
from symclone.Expression import Expression
from symclone.Symbol import Symbol


def main():
    """main program"""
    # Define symbolic variables
    x = Symbol('x')
    y = Symbol('y')

    # Define symbolic expressions
    expr = Expression(x**2 + math.sin(x))

    # Compute derivatives
    derivative_expr = expr.derivative('x')
    print("Derivative:", derivative_expr)

    # Compute integrals
    integral_expr = expr.integral('x')
    print("Integral:", integral_expr)

    # Compute limits
    limit_expr = expr.limit('x', 0)
    print("Limit:", limit_expr)

    # Compute series expansions
    series_expr = expr.series_expansion('x', 0, 3)
    print("Series Expansion:", series_expr)

if __name__ == "__main__":
    main()
