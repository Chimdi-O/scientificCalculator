import sympy as sp
import numpy as np
from scipy.misc import derivative

def symbolic_differentiation(func_str, x):
  """
  Calculates the symbolic derivative of a function from a string.

  Args:
    func_str: The string representation of the function.
    x: The independent variable.

  Returns:
    The symbolic derivative.
  """
  f = string_to_function(func_str)
  dfdx = sp.diff(f(x), x)  # This line is crucial
  return dfdx

def numerical_differentiation(func_str, x0):
  """
  Calculates the numerical derivative of a function from a string at a point.

  Args:
    func_str: The string representation of the function.
    x0: The point at which to calculate the derivative.

  Returns:
    The numerical derivative.
  """
  f = string_to_function(func_str)
  dfdx_num = derivative(f, x0)
  return dfdx_num

def string_to_function(func):
  """
  Converts a string representation of a function into a callable function using sympy.

  Args:
    func_str: The string representation of the function.

  Returns:
    The callable function.
  """

  x = sp.Symbol('x')
  expr = sp.sympify(func)
  return sp.lambdify(x, expr)

# Example usage:
func_str = "2*x**3 + 2*x"  # No need to modify the string
x = sp.Symbol('x')
x0 = 3

symbolic_result = symbolic_differentiation(func_str, x)
print(symbolic_result)  

numerical_result = numerical_differentiation(func_str, x0)
print(numerical_result) 
