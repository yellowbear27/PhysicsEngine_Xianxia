"""Soul Formation (化神期) – Branching Out.
Lie groups and algebras: SO(3) generators, exponential map, adjoint, Killing form.
"""

import numpy as np

def so3_generator(axis):
    """Return 3x3 skew‑symmetric generator for axis 'x', 'y', or 'z'."""
    if axis == 'x':
        return np.array([[0,0,0],[0,0,-1],[0,1,0]], dtype=float)
    elif axis == 'y':
        return np.array([[0,0,1],[0,0,0],[-1,0,0]], dtype=float)
    elif axis == 'z':
        return np.array([[0,-1,0],[1,0,0],[0,0,0]], dtype=float)
    else:
        raise ValueError("axis must be 'x','y','z'")

def lie_exponential(L, angle):
    """Exponential map for SO(3): exp(θ L) using Rodrigues formula."""
    K = L
    K2 = K @ K
    return np.eye(3) + np.sin(angle) * K + (1 - np.cos(angle)) * K2

def adjoint_representation(X, Y):
    """ad_X(Y) = [X,Y]."""
    return X @ Y - Y @ X

def cartan_killing_form(X, Y):
    """Killing form K(X,Y) = Tr(ad_X ad_Y). For matrix Lie algebra, proportional to Tr(XY)."""
    return np.trace(X @ Y)  # Works for simple Lie algebras like su(2)
