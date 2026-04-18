# Hundun Engine

**A physics simulation engine built from first principles. Realistic force, consequence, and emergent physical behaviour for worlds that take their own laws seriously.**

Status: Early development — foundational architecture phase
Language: Python (prototyping), Rust (performance layer, future)
Author: Building in public from first principles

---

## What This Is

Hundun is a physics simulation engine.

Not a game engine. Not a rendering pipeline. Not a wrapper around an existing physics library. A simulation engine — a system whose purpose is to calculate what actually happens when force meets mass, when energy propagates through a medium, when impact produces consequence.

The name comes from Hundun (混沌) — the primordial chaos of Chinese cosmology. The undifferentiated state that precedes all structure. Before order, before form, before the ten thousand things: Hundun. It is an appropriate name for an engine whose job is to model the raw behaviour of physical reality before any layer of abstraction is placed on top of it.

---

## Origin

I spent two decades in finance. Investment banking, private equity, capital structure. The work involved understanding systems: how forces move through them, where the leverage points are, what happens when assumptions fail.

When I began seriously studying mathematics and physics in my fifties — working through Spivak's Calculus from first principles, engaging with tensor field theory, studying classical mechanics — I found the same structural thinking applied. Physics is a language. It describes how things actually behave, not how we prefer they should.

The project that demanded this engine was a xianxia universe I have been building for years — a world with its own cosmology, its own metaphysics, its own hierarchy of power. The genre almost universally treats its physics as decoration. Energy is a word. Impact is an animation. Consequence is optional.

I wanted to ask the harder question: what if the physics were real?

That question required an engine that did not exist. So I am building it.

But the engine is not the xianxia world. The xianxia world is where the engine is first demonstrated and stress-tested. The engine belongs to any world whose physics deserve to be taken seriously.

---

## The Core Principle

Most game physics systems work backwards. They start with a desired visual outcome — a satisfying explosion, a dramatic knockback, a spectacular impact — and engineer the numbers to produce it. The physics serves the spectacle.

Hundun works forwards. Physical laws are defined. Forces are applied. Consequences are calculated. Spectacle, where it occurs, is an emergent property of the simulation — not a designed output.

This distinction matters. A system that works forwards produces surprises. It produces interactions nobody scripted. It produces a world that behaves consistently even in situations nobody anticipated. That is what makes a simulated world feel real rather than performed.

---

## What Hundun Simulates

**Force and momentum.** Every body has mass. Every impact transfers momentum. The consequences of force are proportional to the force applied and the resistance of what receives it.

**Energy propagation.** When significant force is applied to a surface or medium, energy propagates outward. A heavy enough impact creates a shockwave. The shockwave has a calculable effect on everything within its radius — terrain, structures, bodies. That effect diminishes with distance according to real physical principles, not designer preference.

**Environmental consequence.** Ground deforms. Structures respond to stress. The environment is not a static backdrop. It is a material system with its own physical properties that interact with the forces applied to it.

**Differential scale.** A being of extraordinary mass and force does not behave like a scaled-up ordinary being. The physics of extreme scale are different. Hundun is designed to handle the full range — from the ordinary to the extreme — without artificial caps or magic numbers.

**Drag and resistance.** Movement through a medium has cost. Air resistance, friction, fluid dynamics at relevant scales. Bodies that move fast or carry great momentum interact with their medium in ways that affect trajectory, stability, and outcome.

---

## Design Philosophy

**Mathematical rigour before implementation.** Before any physical phenomenon is implemented in code, the equations governing it are understood. The mathematics precede the model. The model precedes the code. A physics engine built on misunderstood physics is not a physics engine.

**Layered complexity.** The engine is built in layers. Each layer is correct, tested, and stable before the next is added. The foundation is Newtonian mechanics. Later layers add fluid dynamics, wave propagation, material science, and eventually the extended physical laws of worlds whose constants differ from our own.

**Separation of simulation from presentation.** Hundun does not render. It calculates. What a system built on Hundun does with those calculations — how it renders, animates, or narrates the physical events — is entirely the responsibility of that system. The engine produces true physical state. The application decides how to show it.

**Pragmatism over purity.** This is not a project to reinvent every layer of the stack. Where standard libraries serve the simulation correctly, they are used. Where they do not, they are replaced. The goal is a correct simulation, not a demonstration that everything can be done from scratch.

**Open physical laws.** Hundun is designed to simulate worlds whose physical constants may differ from our own. Gravity can be stronger. Energy fields can behave differently. Material properties can follow different rules. The engine defines a framework for physical laws and simulates consistently within whatever laws are defined — ours, or someone else's.

---

## Architecture Overview

The engine is structured around four core modules. These are the target architecture. Current implementation is foundational.

**Force Module**
Calculates forces acting on bodies: gravitational, applied, reactive, field-based. Produces force vectors that feed into the dynamics module.

**Dynamics Module**
Applies forces to bodies with defined mass and physical properties. Calculates resulting acceleration, velocity, and trajectory. Handles collision detection and response.

**Propagation Module**
Models energy propagation through media: shockwaves, pressure waves, heat propagation, field effects. Takes impact events from the dynamics module and calculates their effects on the surrounding environment.

**World State Module**
Maintains the physical state of the simulated world: positions, velocities, material properties, structural integrity of terrain and objects. Receives updates from all other modules and provides the ground truth state that any application layer reads from.

---

## First Proving Ground: Myriad Worlds

The first world Hundun will simulate is Myriad Worlds (三千大千世界) — a xianxia universe with its own cosmological structure and a defined physical law system.

In Myriad Worlds, the energy field known as Qi is a rank-2 tensor field. It transforms correctly under coordinate changes. It obeys conservation laws. Its behaviour follows a 64-hexagram framework derived from the I Ching, with the eight primary hexagrams holding foundational authority over the field's behaviour.

This is not decoration. It is a defined extension of the engine's physical law framework. Hundun's open physical laws architecture means that Qi as a tensor field is implementable within the same simulation framework that handles Newtonian mechanics — not as a special case, but as a naturally extending set of field equations.

This is the stress test. If the engine can handle both the physics of our world and the extended physics of a world with additional field structure, it is general enough to be genuinely useful.

---

## Relationship to Other Projects

Hundun is a standalone engine. It does not belong to any single game or world.

Its first application is Myriad Worlds — both the novel and the RPG being developed in a separate repository. The RPG built on Myriad Worlds will use Hundun as its simulation layer, providing the physical consequence and environmental response that the game's design philosophy demands.

But the engine's ambitions are broader than any single application. A physics simulation engine that correctly models force propagation, environmental consequence, and emergent physical behaviour at differential scale is useful wherever realistic simulation is needed.

Other developers are welcome to build on it. That is the point of doing this in public.

---

## The 3Blue1Brown Parallel

Grant Sanderson built Manim — a mathematical animation engine — to visualise the concepts he was studying and teaching. The engine was not the goal. Understanding was the goal. The engine was the artefact of that understanding made useful.

Hundun is being built the same way. The physics I am studying — mechanics, tensor theory, energy propagation, numerical methods — are being implemented in the engine as they are understood. The engine grows with the understanding. The understanding deepens through the act of implementation.

This means the commit history of this repository is also an education record. A reader who follows the commits from beginning to end is watching someone learn physics by building the system physics describes.

---

## Current Status

Foundational. The study path that informs the engine — Spivak's Calculus, tensor field theory, classical mechanics — is underway. The architecture is defined. Early implementation of the Force and Dynamics modules is in progress.

Current milestone: a correct Python implementation of Newtonian impact between two bodies of defined mass and velocity, producing accurate force transfer, momentum exchange, and a propagating pressure effect on a defined surface.

That is the first brick. The engine will grow from there.

---

## Roadmap

This is a long-horizon project. The roadmap reflects honest expectations, not optimistic ones.

**Phase 1 — Newtonian Foundation**
Force, momentum, collision, basic energy propagation. Demonstrated through simple impact scenarios. Python implementation.

**Phase 2 — Environmental Response**
Terrain deformation, structural stress, shockwave radius effects. The simulation begins to model consequences beyond the immediate impact point.

**Phase 3 — Extended Field Systems**
Implementation of Qi as a tensor field within the Myriad Worlds law framework. The engine demonstrates that its open physical laws architecture can handle field equations beyond Newtonian mechanics.

**Phase 4 — Performance Layer**
Python prototypes validated. Rust implementation begins for performance-critical modules. The engine becomes capable of real-time simulation.

**Phase 5 — Application Layer**
Hundun serves as the physics backend for the Myriad Worlds RPG. The proving ground becomes a shipped product.

---

## Learning Objectives

This project is engineered to teach:

- Classical mechanics — implemented, not just understood
- Tensor mathematics — in code, not just on paper
- Numerical methods — how to simulate continuous systems discretely
- Rust — for performance-critical simulation work
- Systems architecture — how to design a modular engine whose components are independent and composable
- The discipline of building something that will outlast the enthusiasm that started it

---

## Why This Is Public

Because building an engine in public is the hardest version of building an engine. Every design decision is visible. Every misunderstanding is in the commit history. Every revision is documented.

That visibility creates accountability. It also creates the possibility of collaboration — other developers who find the problem interesting, who have solved adjacent problems, who want to build on a foundation being laid carefully and honestly.

And because this project, like everything else in this portfolio, is an argument: that genuine curiosity pursued with discipline produces genuine capability, regardless of when it starts.

The engine will be what the understanding makes possible. The understanding is being built now, one line at a time.

---

*Hundun. Before order, the potential for all things.*
