"""Tribulation Transcendence – Classical electromagnetism."""

import math
import numpy as np
from .constants import K, EPSILON_0, MU_0, C

def coulomb_force(q1: float, q2: float, r: float) -> float:
    """F = k * q1 q2 / r² (magnitude)"""
    return K * q1 * q2 / (r**2)

def electric_field_point(q: float, r: float) -> float:
    """E = k q / r² (magnitude)"""
    return K * q / (r**2)

def lorentz_force_magnitude(q: float, E: float, v: float, B: float, angle_deg: float = 90.0) -> float:
    """F = qE + q v B sinθ (simplified 1D)"""
    return abs(q) * E + abs(q) * v * B * math.sin(math.radians(angle_deg))

def electric_flux(E: float, A: float, angle_deg: float = 0.0) -> float:
    """Φ_E = E A cosθ"""
    return E * A * math.cos(math.radians(angle_deg))

def magnetic_force_on_wire(I: float, L: float, B: float, angle_deg: float = 90.0) -> float:
    """F = I L B sinθ"""
    return I * L * B * math.sin(math.radians(angle_deg))

def maxwell_faraday_law(dphi_B_dt: float) -> float:
    """
    Faraday's law: emf = -dΦ_B/dt.
    Returns induced electromotive force (volts).
    """
    return -dphi_B_dt

def maxwell_ampere_law(displacement_current: float, enclosed_current: float) -> float:
    """
    Ampère-Maxwell law: ∮B·dl = μ0 (I_enc + I_displacement).
    Returns the line integral of B (magnetic field circulation).
    """
    return MU_0 * (enclosed_current + displacement_current)

def poynting_vector(E: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Poynting vector S = (1/μ0) E × B. Represents power flow per unit area.
    E, B: 3D numpy arrays.
    Returns S as 3D vector.
    """
    return (1.0 / MU_0) * np.cross(E, B)

def electromagnetic_wave_speed(epsilon: float = EPSILON_0, mu: float = MU_0) -> float:
    """Speed of electromagnetic wave in a medium: v = 1/sqrt(εμ). Vacuum gives c."""
    return 1.0 / math.sqrt(epsilon * mu)
