"""Qi Condensation (炼气期) – First Hearing the Great Dao.
Calculus operations: derivatives, definite integrals, partial derivatives,
gradients, and scalar optimisation using NumPy and SciPy.
"""

import numpy as np
from scipy.integrate import quad, dblquad, tplquad
from scipy.optimize import minimize_scalar

def derivative_at_point(func, x, dx=1e-6, args=(), order=1):
    """Compute 1st or 2nd derivative using central differences."""
    if order == 1:
        return (func(x + dx, *args) - func(x - dx, *args)) / (2 * dx)
    elif order == 2:
        return (func(x + dx, *args) - 2*func(x, *args) + func(x - dx, *args)) / (dx**2)
    else:
        raise ValueError("order must be 1 or 2")

def definite_integral(func, a, b, args=()):
    """∫_a^b func(x) dx using adaptive quadrature."""
    result, _ = quad(func, a, b, args=args)
    return result

def double_integral(func, xa, xb, ya, yb, args=()):
    """∬ func(x,y) dy dx."""
    result, _ = dblquad(func, xa, xb, ya, yb, args=args)
    return result

def triple_integral(func, xa, xb, ya, yb, za, zb, args=()):
    """∭ func(x,y,z) dz dy dx."""
    result, _ = tplquad(func, xa, xb, ya, yb, za, zb, args=args)
    return result

def gradient_2d(f, x, y, spacing=1.0):
    """Numerical gradient of 2D scalar field f(x,y) using numpy.gradient."""
    return np.gradient(f, spacing, axis=0), np.gradient(f, spacing, axis=1)

def find_minimum_scalar(func, bounds, args=()):
    """Minimize scalar function over interval using bounded optimisation."""
    res = minimize_scalar(func, bounds=bounds, args=args, method='bounded')
    return res.x if res.success else None

def partial_derivative(func, point, var_index, dx=1e-6):
    """∂f/∂x_i at given point using central differences."""
    point = np.array(point, dtype=float)
    x_forward = point.copy()
    x_back = point.copy()
    x_forward[var_index] += dx
    x_back[var_index] -= dx
    return (func(*x_forward) - func(*x_back)) / (2 * dx)
