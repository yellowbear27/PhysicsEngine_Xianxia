"""Nascent Soul – Newtonian gravity."""

import math
from .constants import G

def gravitational_force(m1: float, m2: float, r: float) -> float:
    """F = G m1 m2 / r² (magnitude)"""
    return G * m1 * m2 / (r**2)

def gravitational_potential_energy(m1: float, m2: float, r: float) -> float:
    """U = -G m1 m2 / r"""
    return -G * m1 * m2 / r

def gravitational_field(m: float, r: float) -> float:
    """g = G m / r² (magnitude)"""
    return G * m / (r**2)

def kepler_third_law(semi_major_axis: float, central_mass: float) -> float:
    """
    Returns orbital period T (in seconds) for a body orbiting a central mass.
    T² = (4π² / (G M)) * a³
    """
    return 2 * math.pi * math.sqrt(semi_major_axis**3 / (G * central_mass))

def orbital_velocity(central_mass: float, radius: float) -> float:
    """Orbital speed for a circular orbit: v = sqrt(G M / r)"""
    return math.sqrt(G * central_mass / radius)
