# Hundun Engine

A physics simulation engine built from first principles. Models realistic force propagation, momentum transfer, environmental consequence, and emergent physical behaviour within rule-defined worlds.

---

## Overview

Hundun is a simulation engine — not a game engine, not a rendering pipeline. Its function is to calculate what physically happens when force meets mass, when energy propagates through a medium, when impact produces consequence in a defined physical environment.

The engine is designed around an open physical law architecture. It can simulate standard Newtonian mechanics or the extended physics of worlds whose constants and field behaviours are explicitly defined to differ from our own. The simulation layer is entirely decoupled from any presentation or rendering layer.

The name references Hundun (混沌) — the primordial undifferentiated state in Chinese cosmology that precedes all structure and order. It is an appropriate name for a system whose purpose is to model the raw behaviour of physical reality before abstraction is applied.

---

## Design Principles

**Consequence-forward simulation.** Forces are applied, physics are calculated, consequences follow. Spectacle is an emergent property of the simulation — not a designed output reverse-engineered from a desired visual effect.

**Open physical law framework.** Physical constants, field behaviours, and force interactions are defined parameters, not hardcoded assumptions. The engine simulates consistently within whatever law set is defined.

**Strict separation of simulation and presentation.** Hundun outputs physical state. What any application does with that state — rendering, narration, animation — is entirely outside the engine's scope.

**Layered construction.** Each simulation layer is correct, tested, and stable before the next is added. Newtonian mechanics form the foundation. Additional layers — fluid dynamics, wave propagation, tensor field systems — are added progressively.

---

## Architecture

The engine is structured around four core modules:

**Force Module** — Calculates all forces acting on bodies: gravitational, applied, reactive, and field-based. Outputs force vectors.

**Dynamics Module** — Applies forces to bodies with defined mass and physical properties. Computes acceleration, velocity, trajectory, and collision response.

**Propagation Module** — Models energy propagation through media: pressure waves, shockwaves, field effects. Takes impact events from the Dynamics module and calculates radial effects on surrounding environment and bodies.

**World State Module** — Maintains the complete physical state of the simulated environment. Receives updates from all modules. Serves as the ground truth read by any application layer.

---

## Primary Application: Myriad Worlds

The first world Hundun simulates is Myriad Worlds (三千大千世界) — a defined fictional universe with an explicit physical law system documented in the companion repository `RPG_MortalWorld`.

In Myriad Worlds, the energy field known as Qi is formalised as a rank-2 tensor field. It transforms correctly under coordinate changes, obeys conservation laws, and follows a 64-hexagram behavioural framework derived from the I Ching. This extended field system is implemented within the same open law architecture as standard Newtonian mechanics — not as a special case, but as a naturally extending set of field equations.

Myriad Worlds serves as the engine's proving ground. A simulation framework capable of handling both standard physics and a well-defined extended field system demonstrates genuine generality.

---

## Repository Structure

```
PhysicsEngine_Xianxia/
├── core/
│   ├── force.py          # Force calculation module (in development)
│   ├── dynamics.py       # Dynamics and collision module (in development)
│   ├── propagation.py    # Energy propagation module (planned)
│   └── world_state.py    # World state management (planned)
├── tests/                # Unit tests per module
├── docs/                 # Technical documentation and physics references
├── requirements.txt
└── README.md
```

---

## Current Status

Foundational phase. Force and Dynamics module architecture is defined. Initial implementation targeting correct Newtonian impact simulation between two bodies — accurate momentum transfer, force calculation, and surface propagation effect.

---

## Roadmap

Phase 1 — Newtonian foundation: force, momentum, collision, basic propagation (current)
Phase 2 — Environmental response: terrain interaction, structural stress, shockwave radius effects
Phase 3 — Extended field systems: Qi tensor field implementation for Myriad Worlds law set
Phase 4 — Performance layer: Rust implementation of performance-critical modules
Phase 5 — Application integration: serving as physics backend for Myriad Worlds RPG

---

## Language

Python (prototyping and development). Rust (performance layer, future phases).

---

## License

MIT
