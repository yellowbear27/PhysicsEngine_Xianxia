"""Foundation Establishment (筑基期) – Complex analysis.
Complex arithmetic, contour integration, residue estimation.
"""

import numpy as np
import cmath
from scipy.integrate import quad

def complex_to_real_imag(z):
    """Return (real, imag)."""
    return z.real, z.imag

def complex_add(z1, z2):
    return z1 + z2

def complex_mul(z1, z2):
    return z1 * z2

def complex_divide(z1, z2):
    return z1 / z2

def complex_conjugate(z):
    return z.conjugate()

def complex_modulus(z):
    return abs(z)

def complex_argument(z):
    return cmath.phase(z)

def complex_power(z, n):
    return z ** n

def complex_exp(z):
    return cmath.exp(z)

def complex_log(z):
    return cmath.log(z)

def complex_sin(z):
    return cmath.sin(z)

def complex_cos(z):
    return cmath.cos(z)

def contour_integral(func, t_start, t_end, param_func, n_points=1000):
    """
    ∫_C f(z) dz with C parameterised as z(t).
    Uses trapezoidal rule.
    """
    t = np.linspace(t_start, t_end, n_points)
    z = param_func(t)
    dz = np.gradient(z, t)
    integrand = func(z) * dz
    return np.trapz(integrand, t)

def residue_pole(func, z0, order=1, n_points=100):
    """Estimate residue at simple pole (order=1) via Cauchy integral."""
    r = 1e-5  # small radius
    theta = np.linspace(0, 2*np.pi, n_points)
    z = z0 + r * np.exp(1j * theta)
    dz_dt = 1j * np.exp(1j * theta)
    integrand = func(z) * dz_dt
    return (1/(2*np.pi*1j)) * np.trapz(integrand, theta)
