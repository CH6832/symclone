#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""FuzzyBoolean.py

Example usage of the SymClone library.
"""


# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled


import math
from typing import Any


class MathOperations:
    """Class providing various mathematical operations on expressions.

    This class contains static methods to perform mathematical operations such as derivative calculation,
    numerical integration, limit computation, and Taylor series expansion.
    """
    

    @staticmethod
    def derivative(expression: callable, symbol: str, value: float, h: float = 0.0001) -> Any:
        """Compute the derivative of an expression with respect to a given symbol numerically.

        Arguments:
        expression -- The expression to differentiate.
        symbol -- The symbol with respect to which the derivative is computed.
        value -- The point at which to compute the derivative.
        h -- Step size for numerical differentiation.
        """
        rate_of_change = (expression(value + h) - expression(value)) / h
        return rate_of_change


    @staticmethod
    def integral(expression: callable, lower_limit: float, upper_limit: float, num_intervals: int | None = 100) -> int:
        """Compute the definite integral of an expression over a specified range numerically.

        Arguments:
        expression -- The expression to integrate.
        lower_limit -- The lower limit of integration.
        upper_limit -- The upper limit of integration.
        num_intervals -- Number of intervals for numerical integration.
        """
        interval_width = (upper_limit - lower_limit) / num_intervals
        integral = sum(expression(lower_limit + i * interval_width) * interval_width for i in range(num_intervals))
        return integral


    @staticmethod
    def limit(expression: callable, symbol: str, value: float) -> Any:
        """Compute the limit of an expression as a symbol approaches a specified value numerically.

        Arguments:
        expression -- The expression to evaluate.
        symbol -- The symbol whose limit is being computed.
        value -- The value toward which the symbol approaches.
        """
        return expression(value)


    @staticmethod
    def series_expansion(expression: callable, point: str, order: float) -> list:
        """Compute the Taylor series expansion of an expression around a specified point up to a given order.

        Arguments:
        expression -- The expression to expand.
        point -- The point around which the series expansion is computed.
        order -- The order of the series expansion.
        """
        coefficients = [expression(point)]
        for i in range(1, order + 1):
            derivative = (expression(point + 1e-10*i) - expression(point)) / (1e-10*i)
            coefficients.append(derivative / math.factorial(i))
        return coefficients
