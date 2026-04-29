"""Golden Core – Work, energy, power."""

import math
import numpy as np

def work_constant_force(F: float, d: float, angle_deg: float = 0.0) -> float:
    """W = F*d*cosθ"""
    return F * d * math.cos(math.radians(angle_deg))

def kinetic_energy(m: float, v: float) -> float:
    """KE = ½ m v²"""
    return 0.5 * m * v**2

def gravitational_pe(m: float, h: float, g: float = 9.80665) -> float:
    """PE = m g h (near Earth surface)"""
    return m * g * h

def elastic_pe(k: float, x: float) -> float:
    """PE_spring = ½ k x²"""
    return 0.5 * k * x**2

def power_constant_force(F: float, v: float, angle_deg: float = 0.0) -> float:
    """P = F * v * cosθ"""
    return F * v * math.cos(math.radians(angle_deg))

def work_variable_force(F_func, x_start: float, x_end: float, n_steps: int = 1000) -> float:
    """
    Approximates work done by a variable force F(x) via numeric integration.
    F_func: callable that takes position x (float) and returns force (float).
    x_start, x_end: integration limits.
    n_steps: number of steps for trapezoidal integration.
    """
    dx = (x_end - x_start) / n_steps
    total = 0.0
    for i in range(n_steps):
        x = x_start + i * dx
        total += F_func(x) * dx
    return total

def work_energy_theorem(initial_ke: float, final_ke: float) -> float:
    """W_net = ΔKE (net work equals change in kinetic energy)"""
    return final_ke - initial_ke
