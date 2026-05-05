# MATHREADME — Mathematics Cultivation Path

Purpose: mathematics path toward QFT-readiness.

Role: curriculum map.

Scaffold: Xianxia cultivation realms.

Method: symbol → meaning → example → code → physics use.

Status: personal learning curriculum. Not a textbook. Not a claim of mastery.

---

## 正脉·数学修仙全境界

Orthodox Mathematics Cultivation Path Toward Quantum Field Theory

| Cultivation Realm | Chinese | Core Techniques | Role |
|:---|:---|:---|:---|
| **Mortal Condensation** | 凡人凝期 | Single-variable calculus, limits, derivatives, integrals, basic algebra, elementary vectors and matrices | computational survival |
| **Qi Condensation** | 炼气期 | Multivariable calculus, gradients, divergence, curl, multiple integrals, complex numbers, basic ODEs | change, motion, local behaviour |
| **Foundation Establishment** | 筑基期 | Linear algebra, vector spaces, linear maps, eigenvalues, diagonalisation, abstract algebra, complex analysis | structure, symmetry, transformation |
| **Golden Core** | 金丹期 | Functional analysis, Hilbert spaces, operators, Fourier series, Fourier transforms, ODEs, PDEs | waves, operators, spaces of functions |
| **Nascent Soul** | 元婴期 | Differential geometry, manifolds, tangent spaces, tensors, differential forms, topology, calculus of variations | geometry becomes physics |
| **Soul Formation** | 化神期 | Lie groups, Lie algebras, Lorentz group, Poincaré group, SU(n), representations, probability, statistics | symmetry, particles, inference |
| **Tribulation Transcendence** | 渡劫期 | Measure theory, Lebesgue integration, Banach spaces, advanced PDEs, path integrals, canonical quantisation | mathematical machinery behind QFT |
| **Mahayana** | 大乘期 | QED, Yang-Mills, gauge theory, renormalisation group, symmetry breaking, functional methods, statistical mechanics | serious QFT territory |
| **Ascension** | 飞升期 | CFT, string theory, supersymmetry, AdS/CFT, algebraic geometry, K-theory, modular forms, vertex algebras | frontier research; not current target |

---

## Sequence Logic

凡人凝期: calculate before proving.

炼气期: understand change in more than one dimension.

筑基期: learn spaces, maps, symmetry, and complex structure.

金丹期: functions become objects.

元婴期: geometry enters physics.

化神期: symmetry becomes law.

渡劫期: analysis becomes brutal; hand-waving dies.

大乘期: fields, particles, symmetries, and renormalisation meet.

飞升期: research frontier. Not the current battle.

---

## Current Code Link

The current mathematics code lives in:

```text
math_library/
```

Current modules:

```text
constants.py
calculus.py
linear_algebra.py
complex_analysis.py
fourier.py
ode_pde.py
functional.py
differential_geometry.py
lie_groups.py
probability.py
qft_math.py
```

These modules are anchors.

They do not mean the full subject is mastered.

They mean there is now a place to convert abstract ideas into code.

---

## QFT Dependency Chain

Minimal spine:

```text
calculus
linear algebra
complex analysis
ODE / PDE
Fourier analysis
functional analysis
differential geometry
Lie groups
probability
quantum mechanics
QFT mathematics
```

More specific QFT chain:

```text
vector spaces
→ Hilbert spaces
→ operators
→ Fourier modes
→ fields
→ symmetries
→ Lie groups
→ action principles
→ path integrals
→ renormalisation
```

---

## Development Rule

Each important mathematical idea should eventually have:

- definition
- notation
- plain English meaning
- minimal example
- Python implementation if useful
- test
- physics connection

A concept is not owned just because the name is familiar.

---

## Secret Teachings

| Chinese | English |
|:---|:---|
| 数理合一，道法自然 | Mathematics and physics must meet; otherwise both float. |
| 层层递进，不可逾越 | Progress layer by layer; skipped foundations return as confusion. |
| 知其名，不如验其式 | Knowing the name is weaker than testing the formula. |
| 会其式，不如明其义 | Using the formula is weaker than understanding its meaning. |

---

## Cultivator's Summary

> **数学为骨，物理为血。**  
> Mathematics is the skeleton; physics is the blood.

> **符号不明，则大道不显。**  
> If the symbols are unclear, the path remains hidden.

> **逐式而修，终向场论。**  
> Cultivate formula by formula; the road points toward field theory.
