"""Qi Condensation – Kinematics (1D & 2D constant acceleration)."""

import math
import numpy as np

def final_velocity(u: float, a: float, t: float) -> float:
    """v = u + a*t"""
    return u + a * t

def displacement(u: float, a: float, t: float) -> float:
    """s = u*t + 0.5*a*t²"""
    return u * t + 0.5 * a * t**2

def velocity_squared(u: float, a: float, s: float) -> float:
    """v² = u² + 2*a*s"""
    return u**2 + 2 * a * s

def average_velocity(u: float, v: float) -> float:
    """v_avg = (u+v)/2 (constant acceleration)"""
    return (u + v) / 2.0

def projectile_range(v0: float, angle_deg: float, g: float = 9.80665) -> float:
    """R = v0² * sin(2θ) / g"""
    rad = math.radians(angle_deg)
    return (v0**2 * math.sin(2 * rad)) / g

def projectile_max_height(v0: float, angle_deg: float, g: float = 9.80665) -> float:
    """H = v0² * sin²θ / (2g)"""
    rad = math.radians(angle_deg)
    return (v0**2 * (math.sin(rad))**2) / (2 * g)

def projectile_time_of_flight(v0: float, angle_deg: float, g: float = 9.80665) -> float:
    """T = 2 v0 sinθ / g"""
    rad = math.radians(angle_deg)
    return (2 * v0 * math.sin(rad)) / g

def projectile_motion_vector(v0, angle_deg: float, t: float, g: float = 9.80665) -> np.ndarray:
    """
    Returns position vector after time t for a projectile launched from origin.
    v0: initial velocity (float = speed, or 2D numpy array [vx0, vy0]).
    angle_deg: launch angle in degrees (ignored if v0 is 2D array).
    """
    if isinstance(v0, (int, float)):
        vx0 = v0 * np.cos(np.radians(angle_deg))
        vy0 = v0 * np.sin(np.radians(angle_deg))
    else:
        vx0, vy0 = v0[0], v0[1]
    x = vx0 * t
    y = vy0 * t - 0.5 * g * t**2
    return np.array([x, y])

def relative_velocity(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """v_rel = v1 - v2 (velocity of object 1 relative to object 2)"""
    return v1 - v2
