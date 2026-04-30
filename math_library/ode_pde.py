"""Golden Core (金丹期) – Partial differential equations.
ODEs: solve_ivp, odeint; PDEs: heat and wave equation explicit finite difference.
"""

import numpy as np
from scipy.integrate import solve_ivp, odeint

def solve_ode_ivp(ode_func, t_span, y0, method='RK45', t_eval=None, args=()):
    """Solve ODE initial value problem using SciPy's solve_ivp."""
    sol = solve_ivp(ode_func, t_span, y0, method=method, t_eval=t_eval, args=args)
    return sol.t, sol.y

def solve_ode_odeint(ode_func, y0, t, args=()):
    """Solve ODE using odeint (simpler API)."""
    return odeint(ode_func, y0, t, args=args)

def heat_equation_1d_explicit(u0, dx, dt, D, n_steps, boundary='dirichlet', bc_value=0):
    """
    Explicit finite difference: ∂u/∂t = D ∂²u/∂x².
    Stability: D*dt/dx² ≤ 0.5.
    """
    nx = len(u0)
    u = u0.copy().astype(float)
    alpha = D * dt / dx**2
    if alpha > 0.5:
        raise ValueError("Stability condition violated")
    for _ in range(n_steps):
        u_new = u.copy()
        for i in range(1, nx-1):
            u_new[i] = u[i] + alpha * (u[i+1] - 2*u[i] + u[i-1])
        if boundary == 'dirichlet':
            u_new[0] = bc_value
            u_new[-1] = bc_value
        u = u_new
    return u

def wave_equation_1d_explicit(u0, v0, dx, dt, c, n_steps):
    """Explicit finite difference for wave equation: ∂²u/∂t² = c² ∂²u/∂x²."""
    nx = len(u0)
    u = u0.astype(float)
    u_prev = u0.astype(float) - dt * v0   # backstep for initial velocity
    for _ in range(n_steps):
        u_next = np.zeros_like(u)
        for i in range(1, nx-1):
            u_next[i] = 2*u[i] - u_prev[i] + (c*dt/dx)**2 * (u[i+1] - 2*u[i] + u[i-1])
        u_prev, u = u, u_next
    return u
