"""Golden Core (金丹期) – Four Orthodox Techniques (Part 2).
Functional analysis: finite‑dimensional Hilbert space, linear operators,
spectral decomposition, commutators, projections.
"""

import numpy as np
from scipy.linalg import eigh

class HilbertSpace:
    """Finite‑dimensional Hilbert space (R^n or C^n)."""
    def __init__(self, dimension, complex=False):
        self.dim = dimension
        self.complex = complex

    def inner_product(self, v, w):
        """⟨v|w⟩."""
        if self.complex:
            return np.vdot(v, w)
        else:
            return np.dot(v, w)

    def norm(self, v):
        return np.sqrt(self.inner_product(v, v))

    def is_orthogonal(self, v, w, tol=1e-8):
        return abs(self.inner_product(v, w)) < tol

def linear_operator(A, x):
    """Apply matrix A to vector x."""
    return np.dot(A, x)

def adjoint_operator(A):
    """Hermitian adjoint (conjugate transpose)."""
    return A.conj().T

def is_hermitian(A, tol=1e-8):
    return np.allclose(A, adjoint_operator(A), atol=tol)

def spectral_decomposition(A):
    """Eigenvalues and eigenvectors of a Hermitian matrix."""
    if not is_hermitian(A):
        raise ValueError("Matrix must be Hermitian")
    w, v = eigh(A)
    return w, v

def projection_operator(vectors):
    """Projection onto subspace spanned by orthonormal column vectors."""
    V = np.column_stack(vectors)
    return V @ V.conj().T

def commutator(A, B):
    """[A,B] = A B - B A."""
    return A @ B - B @ A

def anticommutator(A, B):
    """{A,B} = A B + B A."""
    return A @ B + B @ A
