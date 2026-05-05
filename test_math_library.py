#!/usr/bin/env python3
"""
Smoke tests for math_library.

Run from repo root:

    python -m pytest -q
"""

import importlib
import numpy as np
import pytest


MODULES = [
    "constants",
    "calculus",
    "linear_algebra",
    "complex_analysis",
    "functional",
    "fourier",
    "ode_pde",
    "differential_geometry",
    "lie_groups",
    "probability",
    "qft_math",
]


@pytest.mark.parametrize("module_name", MODULES)
def test_import_math_module(module_name):
    mod = importlib.import_module(f"math_library.{module_name}")

    if module_name == "constants":
        assert hasattr(mod, "PI")

    elif module_name == "calculus":
        result = mod.definite_integral(lambda x: x**2, 0, 1)
        assert abs(result - 1 / 3) < 1e-2

    elif module_name == "linear_algebra":
        A = [[1, 2], [3, 4]]
        det = mod.determinant(A)
        assert abs(det + 2.0) < 1e-9

    elif module_name == "complex_analysis":
        z = 1 + 1j
        arg = mod.complex_argument(z)
        assert abs(arg - np.pi / 4) < 1e-2

    elif module_name == "functional":
        hs = mod.HilbertSpace(3)
        v = [1, 0, 0]
        assert abs(hs.norm(v) - 1.0) < 1e-9

    elif module_name == "fourier":
        t = np.linspace(0, 1, 100)
        sig = np.sin(2 * np.pi * 5 * t)
        freq, spec = mod.fourier_transform_1d(sig, dt=t[1] - t[0])
        max_freq = freq[np.argmax(np.abs(spec))]
        assert abs(abs(max_freq) - 5.0) < 1.0

    elif module_name == "ode_pde":
        def dummy(t, y):
            return -y

        t, y = mod.solve_ode_ivp(dummy, (0, 1), [1.0])
        assert abs(y[0][-1] - 0.3679) < 0.05

    elif module_name == "differential_geometry":
        assert hasattr(mod, "christoffel_symbols_numeric")

    elif module_name == "lie_groups":
        Lx = mod.so3_generator("x")
        R = mod.lie_exponential(Lx, np.pi / 2)
        assert R.shape == (3, 3)

    elif module_name == "probability":
        mean = mod.mean([1, 2, 3, 4])
        assert abs(mean - 2.5) < 1e-9

    elif module_name == "qft_math":
        prop = mod.propagator(0, 1)
        assert prop is not None
