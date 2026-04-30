"""Foundation Establishment (筑基期) – Four Orthodox Techniques (Part 1).
Linear algebra: matrix operations, eigenvalue decomposition, SVD, QR,
linear solvers, norms, and least squares (NumPy).
"""

import numpy as np
from numpy.linalg import inv, det, eig, eigh, svd, qr, norm, solve, lstsq, matrix_power

def inverse(matrix):
    """Matrix inverse."""
    return inv(matrix)

def determinant(matrix):
    """Determinant of a square matrix."""
    return det(matrix)

def eigenvalues(matrix, hermitian=False):
    """Eigenvalues (and eigenvectors) for general or Hermitian matrices."""
    if hermitian:
        w, v = eigh(matrix)
    else:
        w, v = eig(matrix)
    return w, v

def singular_value_decomposition(matrix):
    """U, S, Vh = svd(A)."""
    return svd(matrix)

def qr_decomposition(matrix):
    """Q, R = qr(A)."""
    return qr(matrix)

def vector_norm(vector, ord=2):
    """Norm of a vector (default Euclidean)."""
    return norm(vector, ord=ord)

def solve_linear(A, b):
    """Solve Ax = b."""
    return solve(A, b)

def least_squares(A, b):
    """Least‑squares solution to Ax ≈ b."""
    return lstsq(A, b, rcond=None)[0]

def matrix_power_square(A, n):
    """Integer power of a square matrix."""
    return matrix_power(A, n)

def is_symmetric(matrix, tol=1e-8):
    """Check if matrix is symmetric (real) or Hermitian (complex)."""
    return np.allclose(matrix, matrix.conj().T, atol=tol)
