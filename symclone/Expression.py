#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Expression.py

Expressions for the SymClone library.
"""


# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled


import math
import pprint
from typing import Any
from scipy.integrate import quad
from .MathOperations import MathOperations
from .Symbol import Symbol


class Expression:
    """Class to represent mathematical expressions and perform various operations on them."""


    def __init__(self, expr: Any) -> None:
        """Initialize an Expression instance with the given SymPy expression.
        
        Arguments:
        expr -- The SymPy expression.
        """    
        self.expr = expr
        return None


    def __str__(self):
        """Convert the MathOperations instance to a string representation."""
        return str(self.expr)


    def __repr__(self):
        """Return the string representation of the expression."""
        return f"Expression('{self.expr}')"


    def substitute(self, symbol_values) -> Any:
        """Substitute symbolic variables with numerical values.
        
        Arguments:  
        symbol values -- Dictionary mapping symbols to numerical values.
        """
        substituted_expr = self.expr
        for symbol, value in symbol_values.items():
            substituted_expr = substituted_expr.replace(Symbol(symbol), value)
        return Expression(substituted_expr)


    def evaluate(self, symbol_value):
        """Evaluate the expression numerically.
        
        Arguments:
        symbol_values -- Optional dictionary mapping symbols to numerical values.
        """
        if isinstance(self.expr, str):
            # If the expression is a string, it's a numerical expression
            return eval(self.expr, {}, {'x': symbol_value})
        else:
            # Otherwise, it's a symbolic expression
            return self.expr.subs('x', symbol_value) if hasattr(self.expr, 'subs') else self.expr
        # if symbol_values is None:
        #     return float(self.expr)
        # else:
        #     substituted_expr = self.substitute(symbol_values).expr
        #     return float(substituted_expr)

    def pow(self, base, exponent):
        # Custom implementation of exponentiation
        return base ** exponent            

    def limit(expression, symbol, value):
        """Compute the limit of an expression as a symbol approaches a specified value numerically.

        Arguments:
        expression -- The expression to evaluate.
        symbol -- The symbol whose limit is being computed.
        value -- The value toward which the symbol approaches.
        """
        return value

    def series_expansion(expression, point, order):
        """Compute the Taylor series expansion of an expression around a specified point up to a given order.

        Arguments:
        expression -- The expression to expand.
        point -- The point around which the series expansion is computed.
        order -- The order of the series expansion.
        """
        coefficients = [point]
        for i in range(1, order + 1):
            derivative = float((point + str(1e-10*i))) / (1e-10*i)
            coefficients.append(derivative / math.factorial(i))
        return coefficients

    @staticmethod
    def parse(expression: str) -> Any:
        """
        Parse a string representing a SymPy-like expression and create an Expression object.
        :param expression_str: String representation of the expression.
        :return: Expression object representing the parsed expression.
        """
        return Expression(eval(expression))


    def to_numerical_expression(self) -> Any:
        """Convert the SymPy-like expression to an expression that can be numerically evaluated."""
        numerical_expr = int(str(self.expr))
        return Expression(numerical_expr)


    def pretty_print_unicode(self) -> None:
        """Pretty print the expression using Unicode characters."""
        pprint(self.expr)
        return None


    def pretty_print_ascii(self) -> None:
        """Pretty print the expression using ASCII characters."""
        pprint(self.expr, use_unicode=False)
        return None


    # def to_mathml(self) -> None:
    #     """Convert the expression to MathML format."""
    #     print(sp.mathml(self.expr))
    #     return None


    def derivative(self, symbol: Any) -> Any:
        """Compute the derivative of the expression with respect to the given symbol.
        
        Arguments:
        symbol -- Symbol with respect to which the derivative is computed.
        """
        derivative_expr = MathOperations().derivative(self.expr, Symbol(symbol).name, 2)
        return Expression(derivative_expr)


    def integral(self, symbol, limits):
        """Compute the integral of the expression with respect to the given symbol.
        
        Arguments:
        symbol -- Symbol with respect to which the integral is computed.
        limits -- Optional integration limits as a tuple (lower_limit, upper_limit).
        """
        if limits:
            lower_limit, upper_limit = limits
            integral_expr, _ = quad(self.expr, lower_limit, upper_limit)
        else:
            integral_expr, _ = quad(self.expr, -float('inf'), float('inf'))
        return Expression(integral_expr)


    def limit_of_expression(self, symbol: Any, value: Any) -> Any:
        """Compute the limit of the expression as the given symbol approaches the specified value.
        
        Arguments:
        symbol -- Symbol whose limit is computed.
        value -- Value toward which the symbol approaches.
        """
        limit_expr = MathOperations().limit(self.expr, Symbol(symbol).name, value)
        return Expression(limit_expr)


    def series_expansion_of_expression(self, symbol: Any, point: Any, order: Any) -> Any:
        """Compute the series expansion of the expression around the specified point up to the given order.
        
        symbol -- Symbol around which the series expansion is computed.
        point -- Point around which the series expansion is computed.
        order -- Order of the series expansion.
        """
        series_expr = MathOperations().series_expansion(self.expr, Symbol(symbol).name, x0=point, n=order).removeO()
        return Expression(series_expr)