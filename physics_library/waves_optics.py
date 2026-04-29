"""Mahayana – Oscillations, waves, geometric optics, interference."""

import math
from .constants import C

def simple_harmonic_motion(A: float, omega: float, t: float, phi: float = 0.0) -> float:
    """x(t) = A cos(ωt + φ)"""
    return A * math.cos(omega * t + phi)

def angular_frequency_spring(k: float, m: float) -> float:
    """ω = sqrt(k/m)"""
    return math.sqrt(k / m)

def period_spring(k: float, m: float) -> float:
    """T = 2π sqrt(m/k)"""
    return 2 * math.pi * math.sqrt(m / k)

def wave_speed(f: float, lam: float) -> float:
    """v = f λ"""
    return f * lam

def doppler_shift_approaching(v_source: float, v_sound: float, f0: float) -> float:
    """f = f0 * v_sound / (v_sound - v_source) (source moving toward observer)"""
    return f0 * v_sound / (v_sound - v_source)

def snells_law(n1: float, theta1_deg: float, n2: float):
    """n1 sinθ1 = n2 sinθ2 → returns θ2 in degrees, or None for TIR"""
    sin_theta2 = n1 * math.sin(math.radians(theta1_deg)) / n2
    if sin_theta2 > 1:
        return None
    return math.degrees(math.asin(sin_theta2))

def lensmaker_formula(n: float, R1: float, R2: float) -> float:
    """1/f = (n-1)(1/R1 - 1/R2). Returns focal length (positive for converging)."""
    power = (n - 1) * (1/R1 - 1/R2)
    return 1 / power if power != 0 else float('inf')

def thin_lens_equation(object_distance: float, focal_length: float) -> float:
    """1/f = 1/do + 1/di → returns image distance di."""
    if object_distance == 0:
        return float('inf')
    inv_di = 1/focal_length - 1/object_distance
    return 1 / inv_di if inv_di != 0 else float('inf')

def interference_maxima(wavelength: float, slit_spacing: float, order: int) -> float:
    """
    Double‑slit maxima angle (in radians): d sinθ = mλ.
    Returns θ in radians.
    """
    sin_theta = order * wavelength / slit_spacing
    if abs(sin_theta) > 1:
        return None  # beyond 90°
    return math.asin(sin_theta)
