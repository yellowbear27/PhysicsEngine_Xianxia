# PHYSICSREADME — Physics Cultivation Map

Purpose: physics path toward QFT-readiness.

Role: curriculum map + module inventory.

Scaffold: Xianxia cultivation realms.

Method: learn the law → implement the formula → test the behaviour → understand the physics.

Status: active personal learning engine. Not a complete physics engine. Not a finished QFT system.

---

## Legend

| Marker | Meaning |
|:---|:---|
| ✅ | implemented |
| ➕ | planned / pending |
| ⚠️ | implemented but needs validation |
| 🧪 | needs stronger tests |

---

## 正脉·物理修仙全境界

Orthodox Physics Cultivation Path

| Cultivation Realm | Chinese | File | Functions |
|:---|:---|:---|:---|
| **Qi Condensation**<br>Kinematics | 炼气期 | `kinematics.py` | `final_velocity` ✅<br>`displacement` ✅<br>`velocity_squared` ✅<br>`average_velocity` ✅<br>`projectile_range` ✅<br>`projectile_max_height` ✅<br>`projectile_time_of_flight` ✅<br>`projectile_motion_vector` ➕<br>`relative_velocity` ➕ |
| **Foundation Establishment**<br>Forces | 筑基期 | `dynamics.py` | `net_force` ✅<br>`weight` ✅<br>`hookes_force` ✅<br>`kinetic_friction` ✅<br>`static_friction_max` ✅<br>`centripetal_force` ✅<br>`centripetal_acceleration` ✅<br>`tension_with_acceleration` ➕<br>`friction_inclined_plane` ➕<br>`spring_force_vector` ➕ |
| **Golden Core**<br>Work, Energy, Momentum | 金丹期 | `work_energy.py`<br>`momentum_collisions.py` | `work_constant_force` ✅<br>`kinetic_energy` ✅<br>`gravitational_pe` ✅<br>`elastic_pe` ✅<br>`power_constant_force` ✅<br>`work_variable_force` ➕<br>`work_energy_theorem` ➕<br><br>`momentum` ✅<br>`impulse` ✅<br>`impulse_from_momentum` ✅<br>`elastic_collision_v1/v2` ✅<br>`inelastic_common_velocity` ✅<br>`coefficient_of_restitution` ✅<br>`collision_2d` ➕ |
| **Nascent Soul**<br>Rotation & Gravitation | 元婴期 | `rotation.py`<br>`gravitation.py` | `torque` ✅<br>`angular_acceleration` ✅<br>`angular_velocity` ✅<br>`angular_displacement` ✅<br>`moment_inertia_point / disk / rod_center / rod_end` ✅<br>`angular_momentum` ✅<br>`rotational_ke` ✅<br>`parallel_axis_theorem` ➕<br>`rotational_dynamics_composite` ➕<br><br>`gravitational_force` ✅<br>`gravitational_potential_energy` ✅<br>`gravitational_field` ✅<br>`kepler_third_law` ➕<br>`orbital_velocity` ➕ |
| **Soul Formation**<br>Continuum Mechanics | 化神期 | `continuum.py` | `stress` ✅<br>`strain` ✅<br>`youngs_modulus` ✅<br>`buoyant_force` ✅<br>`drag_force` ✅<br>`continuity` ✅<br>`bernoulli_pressure` ✅<br>`viscosity_shear_stress` ✅<br>`stress_tensor_2d` ➕<br>`navier_stokes_simplified` ➕<br>`poiseuille_flow_rate` ➕<br>`surface_tension_pressure` ➕ |
| **Tribulation Transcendence**<br>Electromagnetism & Thermodynamics | 渡劫期 | `electromagnetism.py`<br>`thermodynamics.py` | `coulomb_force` ✅<br>`electric_field_point` ✅<br>`lorentz_force_magnitude` ✅<br>`electric_flux` ✅<br>`magnetic_force_on_wire` ✅<br>`maxwell_faraday_law` ➕<br>`maxwell_ampere_law` ➕<br>`poynting_vector` ➕<br>`electromagnetic_wave_speed` ➕<br><br>`ideal_gas_pressure` ✅<br>`internal_energy_monatomic` ✅<br>`entropy_change_heat` ✅<br>`boltzmann_entropy` ✅<br>`average_kinetic_energy` ✅<br>`maxwell_boltzmann_probability` ✅<br>`heat_capacity_cp_cv` ➕<br>`carnot_efficiency` ➕<br>`clausius_clapeyron` ➕ |
| **Mahayana**<br>Relativity, Waves, Quantum | 大乘期 | `relativity.py`<br>`waves_optics.py`<br>`quantum.py` | `lorentz_factor` ✅<br>`time_dilation` ✅<br>`length_contraction` ✅<br>`relativistic_momentum` ✅<br>`energy_total` ✅<br>`energy_rest` ✅<br>`kinetic_energy_relativistic` ✅<br>`schwarzschild_radius` ✅<br>`gravitational_time_dilation` ✅<br><br>`simple_harmonic_motion` ✅<br>`angular_frequency_spring` ✅<br>`period_spring` ✅<br>`wave_speed` ✅<br>`doppler_shift_approaching` ✅<br>`snells_law` ✅<br>`lensmaker_formula` ✅<br>`thin_lens_equation` ➕<br>`interference_maxima` ➕<br><br>`photon_energy` ✅<br>`photon_wavelength` ✅<br>`de_broglie_wavelength` ✅<br>`uncertainty_position_momentum` ✅<br>`uncertainty_energy_time` ✅<br>`infinite_well_energy` ✅<br>`infinite_well_wavefunction` ✅<br>`quantum_harmonic_oscillator_energy` ➕<br>`tunneling_probability` ➕<br>`time_independent_schrodinger_1d` ➕ |

---

## Realm Logic

炼气期: motion before force.

筑基期: force before energy.

金丹期: energy and momentum as conserved structure.

元婴期: rotation and gravitation; systems stop being purely linear.

化神期: matter becomes continuous; point particles are no longer enough.

渡劫期: fields, heat, entropy, waves of influence.

大乘期: relativity, waves, quantum; classical intuition starts to break.

QFT direction: fields become the main object.

---

## Implementation Notes

Existing ✅ functions are implemented in `physics_library/`.

Pending ➕ functions are planned techniques.

Vector operations should use `numpy`.

Simplified GR means only entry-level formulas for now:

- Schwarzschild radius
- gravitational time dilation

No full Einstein field equations yet.

Quantum functions are basic learning implementations.

No pretending this is complete.

---

## Testing Notes

Testing has begun.

Current smoke tests run through `pytest`.

Current command:

`python -m pytest -q`

Current known result:

`11 passed`

Next testing direction:

- basic formula checks
- unit sanity checks
- edge cases
- numerical examples
- one test per important formula

---

## Development Rule

Each important physics formula should eventually have:

- equation
- plain English meaning
- units
- Python function
- example input
- expected output
- test
- note on assumptions

A formula is not owned just because it exists in code.

---

## Cultivator's Summary

> **此册为图，非为终点。**  
> This manual is a map, not the destination.

> **缺者当补，疑者当验。**  
> What is missing shall be added; what is doubtful shall be tested.

> **逐境而行，终向场论。**  
> Proceed realm by realm; the road points toward field theory.
