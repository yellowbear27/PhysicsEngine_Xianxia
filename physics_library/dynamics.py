"""Foundation Establishment – Newton's laws and forces."""

import math
import numpy as np

def net_force(m: float, a: float) -> float:
    """F = m*a"""
    return m * a

def weight(m: float, g: float = 9.80665) -> float:
    """W = m*g"""
    return m * g

def hookes_force(k: float, x: float) -> float:
    """F_spring = -k*x (restoring force)"""
    return -k * x

def kinetic_friction(N: float, mu_k: float) -> float:
    """f_k = μ_k * N"""
    return mu_k * N

def static_friction_max(N: float, mu_s: float) -> float:
    """f_s,max = μ_s * N (threshold)"""
    return mu_s * N

def centripetal_force(m: float, v: float, r: float) -> float:
    """F_c = m*v²/r"""
    return m * v**2 / r

def centripetal_acceleration(v: float, r: float) -> float:
    """a_c = v²/r"""
    return v**2 / r

def tension_with_acceleration(mass: float, acceleration: float, g: float = 9.80665, upward: bool = True) -> float:
    """
    Tension in a string supporting a mass that is accelerating.
    If upward=True: T = m*(g + a)
    If upward=False (downward): T = m*(g - a) (provided a ≤ g)
    """
    if upward:
        return mass * (g + acceleration)
    else:
        return mass * (g - acceleration)

def friction_inclined_plane(mass: float, angle_deg: float, mu: float, g: float = 9.80665) -> float:
    """
    Returns the friction force (magnitude) on an object on an inclined plane.
    mu is the coefficient of friction (kinetic or static as appropriate).
    """
    normal_force = mass * g * math.cos(math.radians(angle_deg))
    return mu * normal_force

def spring_force_vector(k: float, displacement: np.ndarray) -> np.ndarray:
    """F = -k * displacement_vector (vector form of Hooke's law)"""
    return -k * displacement
