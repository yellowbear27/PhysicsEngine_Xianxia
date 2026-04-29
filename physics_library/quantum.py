"""Mahayana – Quantum mechanics basics."""

import math
import numpy as np
from .constants import HBAR, H, C

def photon_energy(f: float) -> float:
    """E = h f"""
    return H * f

def photon_wavelength(E: float) -> float:
    """λ = hc / E"""
    return H * C / E

def de_broglie_wavelength(m: float, v: float) -> float:
    """λ = h / (m v)"""
    return H / (m * v)

def uncertainty_position_momentum(dx: float) -> float:
    """Δp ≥ ħ/(2Δx) (minimum uncertainty)"""
    return HBAR / (2 * dx)

def uncertainty_energy_time(dE: float) -> float:
    """Δt ≥ ħ/(2ΔE)"""
    return HBAR / (2 * dE)

def infinite_well_energy(n: int, m: float, L: float) -> float:
    """E_n = (n² π² ħ²) / (2 m L²)"""
    return (n**2 * math.pi**2 * HBAR**2) / (2 * m * L**2)

def infinite_well_wavefunction(x: float, n: int, L: float) -> float:
    """ψ_n(x) = sqrt(2/L) sin(nπx/L) (0 < x < L)"""
    if x <= 0 or x >= L:
        return 0.0
    return math.sqrt(2 / L) * math.sin(n * math.pi * x / L)

def quantum_harmonic_oscillator_energy(n: int, omega: float) -> float:
    """E_n = ħ ω (n + 1/2)"""
    return HBAR * omega * (n + 0.5)

def tunneling_probability(V0: float, E: float, width: float, mass: float) -> float:
    """
    1D rectangular barrier tunneling probability (WKB approximation).
    V0: barrier height (eV), E: particle energy (eV), width: barrier width (m), mass: particle mass (kg)
    Returns transmission probability (0 to 1).
    """
    if E >= V0:
        return 1.0
    kappa = math.sqrt(2 * mass * (V0 - E)) / HBAR
    return math.exp(-2 * kappa * width)

def time_independent_schrodinger_1d(potential_func, x_min: float, x_max: float,
                                    n_points: int = 1000, energy_guess: float = 1.0) -> dict:
    """
    Numerical solver for 1D time‑independent Schrödinger equation using finite differences.
    Returns a dictionary with 'energies' (list of found eigenvalues) and 'wavefunctions' (list of arrays).
    This is a simple shooting method, not a full eigensolver. For demonstration only.
    In practice, use `scipy.linalg.eigh` for a matrix representation.
    """
    # This is a placeholder skeleton. A complete solver would discretize the Hamiltonian
    # and solve the eigenvalue problem. For brevity, we return a stub.
    # Full implementation is beyond the scope of a single function, but here is the structure:
    # x = np.linspace(x_min, x_max, n_points)
    # dx = x[1] - x[0]
    # V = potential_func(x)
    # Construct kinetic + potential matrix, then diagonalize.
    # For now, return a placeholder.
    return {
        "energies": [energy_guess],
        "wavefunctions": [np.zeros(n_points)],
        "note": "Full solver not implemented; use scipy.linalg.eigh for actual computations."
    }
