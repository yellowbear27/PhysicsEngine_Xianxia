"""Mahayana – Special and simplified general relativity."""

import math
from .constants import C, G

def lorentz_factor(v: float) -> float:
    """γ = 1 / sqrt(1 - v²/c²)"""
    if v >= C:
        return float('inf')
    return 1 / math.sqrt(1 - (v**2 / C**2))

def time_dilation(dt_proper: float, v: float) -> float:
    """Δt = γ Δτ"""
    return lorentz_factor(v) * dt_proper

def length_contraction(L0: float, v: float) -> float:
    """L = L0 / γ"""
    return L0 / lorentz_factor(v)

def relativistic_momentum(m0: float, v: float) -> float:
    """p = γ m0 v"""
    return lorentz_factor(v) * m0 * v

def energy_total(m0: float, v: float) -> float:
    """E = γ m0 c²"""
    return lorentz_factor(v) * m0 * C**2

def energy_rest(m0: float) -> float:
    """E0 = m0 c²"""
    return m0 * C**2

def kinetic_energy_relativistic(m0: float, v: float) -> float:
    """K = (γ - 1) m0 c²"""
    return (lorentz_factor(v) - 1) * m0 * C**2

def schwarzschild_radius(mass: float) -> float:
    """Schwarzschild radius (event horizon) for a non‑rotating black hole: r_s = 2GM/c²"""
    return 2 * G * mass / C**2

def gravitational_time_dilation(radius: float, mass: float, far_time_interval: float = 1.0) -> float:
    """
    Gravitational time dilation near a spherical mass.
    Returns proper time interval at radius r, given far‑away (coordinate) time interval.
    τ = t_far * sqrt(1 - 2GM/(r c²))
    """
    factor = 1 - (2 * G * mass) / (radius * C**2)
    if factor <= 0:
        return 0.0  # within or at horizon
    return far_time_interval * math.sqrt(factor)
