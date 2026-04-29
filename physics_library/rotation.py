"""Nascent Soul – Rotational mechanics."""

import math
import numpy as np

def torque(F: float, r: float, angle_deg: float = 90.0) -> float:
    """τ = r F sinθ"""
    return r * F * math.sin(math.radians(angle_deg))

def angular_acceleration(tau: float, I: float) -> float:
    """α = τ / I"""
    return tau / I

def angular_velocity(omega0: float, alpha: float, t: float) -> float:
    """ω = ω0 + α t"""
    return omega0 + alpha * t

def angular_displacement(omega0: float, alpha: float, t: float) -> float:
    """θ = ω0 t + ½ α t²"""
    return omega0 * t + 0.5 * alpha * t**2

def moment_inertia_point(m: float, r: float) -> float:
    """I = m r² (point mass)"""
    return m * r**2

def moment_inertia_disk(m: float, r: float) -> float:
    """I = ½ m r² (solid disk)"""
    return 0.5 * m * r**2

def moment_inertia_rod_center(m: float, L: float) -> float:
    """I = (1/12) m L² (rod about center)"""
    return (1/12) * m * L**2

def moment_inertia_rod_end(m: float, L: float) -> float:
    """I = (1/3) m L² (rod about one end)"""
    return (1/3) * m * L**2

def angular_momentum(I: float, omega: float) -> float:
    """L = I ω"""
    return I * omega

def rotational_ke(I: float, omega: float) -> float:
    """KE_rot = ½ I ω²"""
    return 0.5 * I * omega**2

def parallel_axis_theorem(I_cm: float, m: float, d: float) -> float:
    """I = I_cm + m*d² (parallel axis theorem)"""
    return I_cm + m * d**2

def rotational_dynamics_composite(torques: list, moments_of_inertia: list) -> float:
    """
    For a composite system (e.g., multiple rotating parts), returns the net angular acceleration.
    torques: list of torques (signed, float)
    moments_of_inertia: list of corresponding moments of inertia (float)
    Net α = Στ / ΣI
    """
    net_torque = sum(torques)
    total_I = sum(moments_of_inertia)
    if total_I == 0:
        return 0.0
    return net_torque / total_I
