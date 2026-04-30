#!/usr/bin/env python3
"""
Test script for math_library.
Run from ~/physicsengine: python test_math_library.py
"""

import traceback
import sys
import numpy as np   # added globally

modules = [
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

def test_import(module_name):
    print(f"\n--- Testing import of {module_name} ---")
    try:
        mod = __import__(f"math_library.{module_name}", fromlist=["*"])
        print(f"✅ {module_name} imported successfully")
        # Basic smoke test
        if module_name == "constants":
            assert hasattr(mod, "PI")
            print("   constants.PI =", mod.PI)
        elif module_name == "calculus":
            result = mod.definite_integral(lambda x: x**2, 0, 1)
            print(f"   ∫x² dx [0,1] = {result} (expected ~0.33333)")
        elif module_name == "linear_algebra":
            A = [[1,2],[3,4]]
            det = mod.determinant(A)
            print(f"   det([[1,2],[3,4]]) = {det} (expected -2.0)")
        elif module_name == "complex_analysis":
            z = 1 + 1j
            arg = mod.complex_argument(z)
            print(f"   arg(1+1j) = {arg} rad (expected ~0.785)")
        elif module_name == "functional":
            hs = mod.HilbertSpace(3)
            v = [1,0,0]
            print(f"   HilbertSpace norm of [1,0,0] = {hs.norm(v)} (expected 1.0)")
        elif module_name == "fourier":
            t = np.linspace(0,1,100)
            sig = np.sin(2*np.pi*5*t)
            freq, spec = mod.fourier_transform_1d(sig, dt=t[1]-t[0])
            max_freq = freq[np.argmax(np.abs(spec))]
            print(f"   peak frequency = {max_freq:.2f} Hz (expected ~5.0)")
        elif module_name == "ode_pde":
            def dummy(t, y):
                return -y
            t, y = mod.solve_ode_ivp(dummy, (0,1), [1.0])
            print(f"   ODE solve: y(1) ≈ {y[0][-1]:.4f} (expected ~0.3679)")
        elif module_name == "differential_geometry":
            assert hasattr(mod, "christoffel_symbols_numeric")
            print("   differential_geometry has christoffel_symbols_numeric")
        elif module_name == "lie_groups":
            Lx = mod.so3_generator('x')
            R = mod.lie_exponential(Lx, np.pi/2)
            print(f"   SO(3) rotation about x by 90°:\n{R}")
        elif module_name == "probability":
            mean = mod.mean([1,2,3,4])
            print(f"   mean([1,2,3,4]) = {mean} (expected 2.5)")
        elif module_name == "qft_math":
            prop = mod.propagator(0, 1)
            print(f"   propagator(p=0,m=1) = {prop}")
        return True
    except Exception as e:
        print(f"❌ Failed to import or test {module_name}:")
        traceback.print_exc()
        return False

def main():
    print("Testing math_library modules...")
    results = []
    for m in modules:
        results.append(test_import(m))
    print("\n" + "="*50)
    if all(results):
        print("\n✅ All modules passed basic tests!")
    else:
        print("\n❌ Some modules failed. See errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
