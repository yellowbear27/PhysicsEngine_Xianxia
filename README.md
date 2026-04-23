# PhysicsEngine_Xianxia

A physics engine built from first principles.

This repository is the long-form build path of a real simulation tool: a system for modelling motion, force, momentum transfer, environmental response, and other physically meaningful behaviour in rule-defined worlds.

For now, the scope is standard physics. The immediate task is not fantasy physics, not lore systems, and not speculative abstraction. It is to build a correct computational foundation in mathematics, mechanics, numerics, and engineering-science modelling.

The repository also documents the reasoning required to build that engine honestly. It shows the mathematics being learned, the notation being decoded, the models being implemented, the assumptions being stated, and the computational artifacts being tested in public.

---

## What this project is

PhysicsEngine_Xianxia is a public physics-engine project with two simultaneous functions:

1. **Build a useful simulation tool**
   - accumulate reusable primitives, models, scenarios, and experiments;
   - construct a correct physics layer before any UI, rendering, or game-facing abstraction;
   - move gradually from simple Newtonian systems toward richer physical domains.

2. **Demonstrate the path by which that tool is being built**
   - decode mathematical notation and physical formulas carefully;
   - turn theory into worked examples;
   - turn worked examples into Python code;
   - validate the code against known behaviour;
   - leave behind public proof of work.

This repository is therefore both **engine build** and **technical learning record**, but the centre of gravity is the engine.

---

## What this project is not

This repository is **not**:

- a claim to have completed an NUS Engineering Science degree;
- a claim to “know QFT” early;
- a monolithic engine built upfront from vague ambition;
- a branding exercise;
- a substitute for mathematical understanding;
- a game engine or rendering pipeline.

---

## Core idea

The engine is being built on a simple principle:

**No physics code is meaningful unless the symbols are understood, the units are known, the assumptions are stated, and the model can be stress-tested.**

That means every important formula must be understood before it is turned into code.

Default rule:

**Theory → Worked Example → Code → Stress Test → Public Commit**

This repo does not treat coding as a substitute for understanding. It treats code as the computational expression of understood mathematics and physics.

---

## Design principles

### 1. Consequence-first simulation
The goal is to calculate what physically happens when forces act on bodies and energy propagates through systems. Visual spectacle, narrative flavour, or game feel are downstream concerns, not the engine’s starting point.

### 2. Simulation and presentation are separate
The engine computes state. It does not exist to render graphics or produce spectacle. Any later rendering, animation, narration, or UI should sit on top of the physical state produced here.

### 3. Build from small verified layers
The engine should not begin as a giant architecture. It should grow by accumulating correct layers:

- concepts
- primitives
- models
- scenarios
- experiments

Only later should orchestration, dashboards, selectors, or more elaborate interfaces appear.

### 4. Honest mathematics
Unread notation is treated as a real bottleneck, not ignored. Mathematical compression is earned, not assumed.

### 5. Public proof over private complexity
A small correct model, published and explained, is better than a large speculative architecture.

---

## Engine scope

The long-run aim is a modular simulation engine capable of handling multiple physical systems through a layered architecture.

Near-term scope:

- kinematics
- Newtonian mechanics
- numerical integration
- simple oscillators
- basic circuits
- fluids at an introductory engineering level
- error comparison and validation experiments

Later scope:

- more advanced continuum models
- PDE-flavoured numerical toys
- stronger field-based modelling
- performance-sensitive implementations in Rust
- possible future support for explicitly defined nonstandard law systems

That final point is a future possibility, not a present promise.

---

## Honest positioning

This repository may use the NUS Engineering Science curriculum as a structural backbone for subject sequencing, because it includes a strong engineering-science mix: calculus, differential equations, linear algebra, numerical methods and statistics, thermodynamics and heat transfer, electromagnetics, signals and systems, and applied quantum physics. But this repository does **not** claim degree completion, institutional affiliation, or equivalence to the full programme. The actual degree includes broader graduation requirements across common curriculum, major requirements, and unrestricted electives. 

Likewise, this repository may aim over time toward the prerequisites needed for advanced theoretical physics, including eventual quantum field theory readiness. But that is a distant horizon. Serious QFT sits downstream of substantial prior quantum mechanics and more advanced preparation; it is not an early sprint target.

---

## Governing learning-build rule

Every meaningful study block should produce at least one of the following:

1. a decoded concept note;
2. a worked example;
3. a computational artifact.

Pure reading with no residue is weak.
Pure coding with no theory is disallowed.

---

## Formula policy

Before a formula enters notes or code, five questions must be answered:

1. What does each variable or operator mean?
2. What are the units?
3. Why does the relationship make physical or mathematical sense?
4. Under what assumptions is it valid?
5. What cases invalidate it or force a modified model?

Default explanation standard for nontrivial formulas:

- each symbol;
- units;
- plain-English meaning;
- assumptions;
- simplest valid numerical example;
- failure conditions / domain of validity.

---

## Repository functions

This repository serves four distinct functions:

1. **Curriculum log**  
   Tracks what is being studied and in what sequence.

2. **Symbol and notation lexicon**  
   Stores decoded mathematical notation, definitions, and recurring expressions.

3. **Computational model library**  
   Holds reusable primitives, models, scenarios, and validation experiments.

4. **Public journal of technical progress**  
   Shows what has actually been understood, implemented, tested, and shipped.

These functions should stay structurally distinct.

---

## Working classification rules

Before creating a file or feature, classify it correctly.

- **CONCEPT** = note / understanding object
- **PRIMITIVE** = reusable small function or data structure
- **MODEL** = coherent mathematical/computational system
- **SCENARIO** = parameterized runnable case
- **EXPERIMENT** = comparison / stress test / validation task
- **HYGIENE** = README, structure, naming, cleanup

Do not call everything an “engine”.

---

## Repository structure

```text
PhysicsEngine_Xianxia/
├── README.md
├── core/
│   ├── state.py
│   ├── integrators.py
│   ├── simulation.py
│   └── utils.py
├── curriculum/
│   ├── roadmap.md
│   ├── symbol_lexicon.md
│   ├── module_index.md
│   └── weekly_sprints.md
├── concepts/
│   ├── algebra/
│   ├── calculus/
│   ├── linear_algebra/
│   ├── differential_equations/
│   ├── mechanics/
│   ├── fluids/
│   ├── electromagnetism/
│   ├── thermo/
│   ├── signals/
│   └── quantum_intro/
├── primitives/
│   ├── math/
│   ├── numerics/
│   ├── vectors/
│   └── units/
├── models/
│   ├── mechanics/
│   ├── fluids/
│   ├── oscillators/
│   ├── circuits/
│   └── fields/
├── scenarios/
│   ├── projectile_motion.py
│   ├── gravity_drop.py
│   ├── harmonic_oscillator.py
│   ├── pipe_flow.py
│   ├── tank_drain.py
│   └── rc_response.py
├── experiments/
│   ├── comparison_runs/
│   ├── error_analysis/
│   └── visualization/
├── journal/
│   ├── weekly_log.md
│   └── concept_reflections.md
└── tests/
    ├── numerical_checks/
    └── sanity_checks/
