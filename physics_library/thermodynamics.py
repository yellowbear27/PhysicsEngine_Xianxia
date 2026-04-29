"""Tribulation Transcendence – Thermodynamics and statistical mechanics."""

import math
from .constants import BOLTZMANN

def ideal_gas_pressure(n: float, T: float, V: float, R: float = 8.314462618) -> float:
    """P = nRT / V"""
    return n * R * T / V

def internal_energy_monatomic(n: float, T: float, R: float = 8.314462618) -> float:
    """U = (3/2) n R T (monatomic ideal gas)"""
    return 1.5 * n * R * T

def entropy_change_heat(Q: float, T: float) -> float:
    """ΔS = Q / T (reversible isothermal)"""
    return Q / T

def boltzmann_entropy(omega: float) -> float:
    """S = k_B ln Ω"""
    return BOLTZMANN * math.log(omega)

def average_kinetic_energy(T: float) -> float:
    """⟨KE⟩ = (3/2) k_B T (per particle, monatomic)"""
    return 1.5 * BOLTZMANN * T

def maxwell_boltzmann_probability(v: float, m: float, T: float) -> float:
    """PDF value for speed v given mass m and temperature T."""
    factor = (m / (2 * math.pi * BOLTZMANN * T))**1.5
    return 4 * math.pi * factor * v**2 * math.exp(-m * v**2 / (2 * BOLTZMANN * T))

def heat_capacity_cp_cv(R: float = 8.314462618, gamma: float = None) -> tuple:
    """
    Returns tuple (C_v, C_p) for ideal gas.
    For monatomic: C_v = (3/2)R, C_p = (5/2)R, gamma = 5/3.
    If gamma is provided, uses C_p = gamma * C_v and C_p - C_v = R.
    Otherwise returns monatomic values.
    """
    if gamma is not None:
        C_v = R / (gamma - 1)
        C_p = gamma * C_v
    else:
        C_v = 1.5 * R
        C_p = 2.5 * R
    return C_v, C_p

def carnot_efficiency(hot_temp: float, cold_temp: float) -> float:
    """Carnot efficiency η = 1 - T_cold / T_hot (temperatures in Kelvin)."""
    if hot_temp <= 0:
        return 0.0
    return 1 - (cold_temp / hot_temp)

def clausius_clapeyron(P1: float, T1: float, T2: float, delta_H_vap: float, R: float = 8.314462618) -> float:
    """
    Clausius-Clapeyron equation for vapor pressure at T2 given P1 at T1.
    Returns P2 = P1 * exp( -(ΔH_vap/R) * (1/T2 - 1/T1) )
    """
    exponent = -(delta_H_vap / R) * (1.0/T2 - 1.0/T1)
    return P1 * math.exp(exponent)
