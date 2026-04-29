"""Soul Formation – Continuum mechanics: stress, strain, fluids."""

import math
import numpy as np

def stress(F: float, A: float) -> float:
    """σ = F / A (normal stress)"""
    return F / A

def strain(L0: float, delta_L: float) -> float:
    """ε = ΔL / L₀"""
    return delta_L / L0

def youngs_modulus(sigma: float, epsilon: float) -> float:
    """E = σ / ε (within elastic limit)"""
    return sigma / epsilon

def buoyant_force(rho_fluid: float, V_displaced: float, g: float = 9.80665) -> float:
    """F_b = ρ * V * g"""
    return rho_fluid * V_displaced * g

def drag_force(rho: float, Cd: float, A: float, v: float) -> float:
    """F_d = ½ ρ Cd A v² (quadratic drag)"""
    return 0.5 * rho * Cd * A * v**2

def continuity(A1: float, v1: float, A2: float) -> float:
    """v2 = (A1 v1)/A2 (incompressible)"""
    return (A1 * v1) / A2

def bernoulli_pressure(P1: float, v1: float, h1: float, v2: float, h2: float, rho: float, g: float = 9.80665) -> float:
    """P2 = P1 + ½ρ(v1² - v2²) + ρg(h1 - h2)"""
    return P1 + 0.5 * rho * (v1**2 - v2**2) + rho * g * (h1 - h2)

def viscosity_shear_stress(eta: float, dv_dz: float) -> float:
    """τ = η (dv/dz) (Newtonian fluid)"""
    return eta * dv_dz

def stress_tensor_2d(sigma_xx: float, sigma_yy: float, tau_xy: float) -> np.ndarray:
    """
    2D stress tensor (plane stress) as a 2x2 numpy array.
    [[σ_xx, τ_xy],
     [τ_xy, σ_yy]]
    """
    return np.array([[sigma_xx, tau_xy],
                     [tau_xy, sigma_yy]])

def navier_stokes_simplified(rho: float, mu: float, v: np.ndarray, grad_p: np.ndarray, body_force: np.ndarray) -> np.ndarray:
    """
    Simplified (incompressible, Newtonian) Navier‑Stokes equation.
    Returns acceleration du/dt = - (1/ρ) ∇p + (μ/ρ) ∇²v + f_body
    For a 2D or 3D vector field.
    This is a placeholder returning an estimate; a full solver would require PDE discretization.
    Here we assume gradients are given as constants.
    """
    # In a full implementation, you would need to compute Laplacian and pressure gradient.
    # For demonstration: return sum of contributions.
    # This function is a skeleton for physical understanding.
    # Use numerical libraries for real simulation.
    inv_rho = 1.0 / rho
    pressure_term = -inv_rho * grad_p
    viscosity_term = (mu * inv_rho) * np.gradient(v)  # simplified placeholder
    return pressure_term + viscosity_term + body_force

def poiseuille_flow_rate(radius: float, delta_P: float, viscosity: float, length: float) -> float:
    """
    Volumetric flow rate Q (m³/s) for laminar flow in a cylindrical pipe.
    Q = (π * r⁴ * ΔP) / (8 * μ * L)
    """
    return (math.pi * radius**4 * delta_P) / (8 * viscosity * length)

def surface_tension_pressure(surface_tension: float, radius1: float, radius2: float) -> float:
    """
    Young‑Laplace pressure difference across a curved interface.
    ΔP = γ (1/R1 + 1/R2)
    """
    return surface_tension * (1/radius1 + 1/radius2)
