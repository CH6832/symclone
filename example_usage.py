#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""example_usage.py

Example usage of the SymClone library.
"""

# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

from symclone.Expression import Expression
from symclone.Symbol import Symbol

def main():
    """Driving code."""

    # Define symbolic variables
    x = Symbol('x')
    y = Symbol('y')

    # Define symbolic expressions
    expr = Expression(f'{x} ** 2 + math.sin({x})')

    # Evaluate expression at x = 2
    result = expr.evaluate({x: 2})
    print("Expression evaluated at x=2:", result)

    # Compute power
    result_pow = expr.pow(2, 3)
    print("2^3:", result_pow)

    # Compute derivative
    derivative_expr = expr.derivative(x)
    print("Derivative:", derivative_expr)

    # Compute integral
    integral_expr = expr.integral(x, (0, 1))
    print("Integral from 0 to 1:", integral_expr)

    # Compute limit
    try:
        limit_expr = expr.limit_of_expression(x, 0)
        print("Limit as x approaches 0:", limit_expr)
    except ValueError as e:
        print("Limit error:", e)
