"""Golden Core – Momentum, impulse, collisions."""

import numpy as np

def momentum(m: float, v: float) -> float:
    """p = m v (scalar)"""
    return m * v

def impulse(F: float, dt: float) -> float:
    """J = F Δt"""
    return F * dt

def impulse_from_momentum(p_initial: float, p_final: float) -> float:
    """J = Δp"""
    return p_final - p_initial

def elastic_collision_v1(m1: float, m2: float, u1: float, u2: float) -> float:
    """v1 after 1D elastic collision."""
    return ((m1 - m2)/(m1 + m2)) * u1 + ((2*m2)/(m1 + m2)) * u2

def elastic_collision_v2(m1: float, m2: float, u1: float, u2: float) -> float:
    """v2 after 1D elastic collision."""
    return ((2*m1)/(m1 + m2)) * u1 + ((m2 - m1)/(m1 + m2)) * u2

def inelastic_common_velocity(m1: float, m2: float, u1: float, u2: float) -> float:
    """V = (m1 u1 + m2 u2)/(m1+m2) (perfectly inelastic)"""
    return (m1*u1 + m2*u2) / (m1 + m2)

def coefficient_of_restitution(v_sep: float, v_app: float) -> float:
    """e = v_separation / v_approach (positive)"""
    return abs(v_sep / v_app)

def collision_2d(m1: float, m2: float, v1_i: np.ndarray, v2_i: np.ndarray, e: float = 1.0) -> tuple:
    """
    2D elastic/inelastic collision (simplified: head‑on in center‑of‑mass frame).
    Returns final velocities (v1_f, v2_f) as numpy arrays.
    This implementation handles the component along the line of centers.
    For full 2D, you would need to rotate coordinates.
    Here we assume velocities are already along the line of centers (1D in 2D form).
    For general case, add coordinate rotation.
    """
    # For simplicity, we treat it as 2D vectors but only the component along
    # the difference in positions matters. This function assumes the collision axis is
    # along the x‑axis (or given vectors are already aligned). For a more complete version,
    # you would compute relative velocity and apply restitution along the normal direction.
    # Here we provide a basic version.
    v_rel = v1_i - v2_i
    # If velocities are along x‑axis, we can apply 1D formulas component‑wise.
    v1_f_x = elastic_collision_v1(m1, m2, v1_i[0], v2_i[0]) if e == 1 else \
             ((m1 - e*m2)/(m1 + m2))*v1_i[0] + ((1+e)*m2/(m1+m2))*v2_i[0]
    v2_f_x = elastic_collision_v2(m1, m2, v1_i[0], v2_i[0]) if e == 1 else \
             ((1+e)*m1/(m1+m2))*v1_i[0] + ((m2 - e*m1)/(m1+m2))*v2_i[0]
    # For y‑component, if no force in y, velocities remain unchanged (if collision is purely along x).
    # This is a simplified 2D collision where the collision normal is along x.
    v1_f = np.array([v1_f_x, v1_i[1]])
    v2_f = np.array([v2_f_x, v2_i[1]])
    return v1_f, v2_f
