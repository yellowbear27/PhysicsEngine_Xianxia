# PhysicsEngine_Xianxia

A physics and mathematics library built from first principles. Organised by Xianxia cultivation tiers — a sequencing and motivation framework for fans of the genre.

---

## Evolution

Started as a folder-based architecture blueprint. Evolved into a library-based design with `physics_lib/` and `math_lib/` as the spine. Both libraries are now substantially built. Current phase: working through each module tier by tier, documenting and validating as we go.

---

## Principles

Code often. Keep it clean. Optimise for execution speed and numerical accuracy. Best practices are the target; we are not there yet.

---

## Repository structure

```text
PhysicsEngine_Xianxia/
├── README.md
├── physicsreadme.md          # Physics library blueprint — realm map, module index, function status
├── mathreadme.md             # Mathematics library blueprint — realm map, subject sequence
├── physics_lib/
│   ├── kinematics.py         # 炼气期 — Qi Condensation
│   ├── dynamics.py           # 筑基期 — Foundation Establishment
│   ├── work_energy.py        # 金丹期 — Golden Core (Part 1)
│   ├── momentum_collisions.py# 金丹期 — Golden Core (Part 2)
│   ├── rotation.py           # 元婴期 — Nascent Soul (Part 1)
│   ├── gravitation.py        # 元婴期 — Nascent Soul (Part 2)
│   ├── continuum.py          # 化神期 — Soul Formation
│   ├── electromagnetism.py   # 渡劫期 — Tribulation Transcendence (Part 1)
│   ├── thermodynamics.py     # 渡劫期 — Tribulation Transcendence (Part 2)
│   ├── relativity.py         # 大乘期 — Mahayana (Part 1)
│   ├── waves_optics.py       # 大乘期 — Mahayana (Part 2)
│   └── quantum.py            # 大乘期 — Mahayana (Part 3)
├── math_lib/
│   ├── constants.py              # Physical and mathematical constants
│   ├── calculus.py               # 凡人凝期/炼气期 — single and multi-variable calculus
│   ├── linear_algebra.py         # 筑基期 — vector spaces, eigenvalues, diagonalization
│   ├── complex_analysis.py       # 筑基期 — contour integration, residues
│   ├── ode_pde.py                # 金丹期 — ODEs and PDEs
│   ├── functional.py             # 金丹期 — Hilbert spaces, operators, spectral theory
│   ├── fourier.py                # 金丹期 — Fourier series, transforms, convolutions
│   ├── differential_geometry.py  # 元婴期 — manifolds, tensors, differential forms
│   ├── lie_groups.py             # 化神期 — Lie groups, Lie algebras, representations
│   ├── probability.py            # 化神期 — probability spaces, inference, statistics
│   └── qft_math.py               # 渡劫期/大乘期 — measure theory, path integrals, renormalisation
├── scenarios/                # Runnable cases — import from physics_lib and math_lib
├── experiments/              # Validation, error analysis, stress tests
├── journal/
│   ├── weekly_log.md
│   └── concept_reflections.md
└── tests/
    ├── numerical_checks/
    └── sanity_checks/
```

---

## Cultivation map

Full function-level detail lives in the sub-READMEs.

### Physics — `physics_lib/`

| Realm | Chinese | Module | Domain |
|:---|:---|:---|:---|
| Qi Condensation | 炼气期 | `kinematics.py` | Motion without force |
| Foundation Establishment | 筑基期 | `dynamics.py` | Newtonian force laws |
| Golden Core | 金丹期 | `work_energy.py` · `momentum_collisions.py` | Energy and momentum |
| Nascent Soul | 元婴期 | `rotation.py` · `gravitation.py` | Rotation and gravitation |
| Soul Formation | 化神期 | `continuum.py` | Stress, fluids, continuum |
| Tribulation Transcendence | 渡劫期 | `electromagnetism.py` · `thermodynamics.py` | Fields and heat |
| Mahayana | 大乘期 | `relativity.py` · `waves_optics.py` · `quantum.py` | Relativity, waves, quantum |

### Mathematics — `math_lib/`

| Realm | Chinese | Module | Domain |
|:---|:---|:---|:---|
| Mortal Condensation / Qi Condensation | 凡人凝期 / 炼气期 | `calculus.py` | Single and multi-variable calculus |
| Foundation Establishment | 筑基期 | `linear_algebra.py` · `complex_analysis.py` | Linear algebra, complex analysis |
| Golden Core | 金丹期 | `ode_pde.py` · `functional.py` · `fourier.py` | ODEs, PDEs, functional analysis, Fourier |
| Nascent Soul | 元婴期 | `differential_geometry.py` | Manifolds, tensors, differential forms |
| Soul Formation | 化神期 | `lie_groups.py` · `probability.py` | Lie theory, probability and statistics |
| Tribulation Transcendence / Mahayana | 渡劫期 / 大乘期 | `qft_math.py` | Measure theory, path integrals, renormalisation |

→ See `physicsreadme.md` for full function inventory and build status.  
→ See `mathreadme.md` for the mathematics cultivation path through QFT.

---

## Honest positioning

The mathematics path targets QFT readiness as a long-run horizon. Serious QFT sits downstream of substantial prior work in quantum mechanics, differential geometry, functional analysis, and Lie theory. 

