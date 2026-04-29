# PHYSICSREADME – Complete Library Blueprint

## 正脉·清华物理修仙全境界 (Orthodox Tsinghua Physics Cultivation)

| Cultivation Realm | Chinese | File | Functions (Status) |
|:---|:---|:---|:---|
| **Qi Condensation**<br>(Kinematics) | 炼气期 | `kinematics.py` | `final_velocity` ✅<br>`displacement` ✅<br>`velocity_squared` ✅<br>`average_velocity` ✅<br>`projectile_range` ✅<br>`projectile_max_height` ✅<br>`projectile_time_of_flight` ✅<br>`projectile_motion_vector` ➕<br>`relative_velocity` ➕ |
| **Foundation Establishment**<br>(Forces) | 筑基期 | `dynamics.py` | `net_force` ✅<br>`weight` ✅<br>`hookes_force` ✅<br>`kinetic_friction` ✅<br>`static_friction_max` ✅<br>`centripetal_force` ✅<br>`centripetal_acceleration` ✅<br>`tension_with_acceleration` ➕<br>`friction_inclined_plane` ➕<br>`spring_force_vector` ➕ |
| **Golden Core**<br>(Work, Energy, Momentum) | 金丹期 | `work_energy.py`<br>`momentum_collisions.py` | `work_constant_force` ✅<br>`kinetic_energy` ✅<br>`gravitational_pe` ✅<br>`elastic_pe` ✅<br>`power_constant_force` ✅<br>`work_variable_force` ➕<br>`work_energy_theorem` ➕<br><br>`momentum` ✅<br>`impulse` ✅<br>`impulse_from_momentum` ✅<br>`elastic_collision_v1/v2` ✅<br>`inelastic_common_velocity` ✅<br>`coefficient_of_restitution` ✅<br>`collision_2d` ➕ |
| **Nascent Soul**<br>(Rotation & Gravitation) | 元婴期 | `rotation.py`<br>`gravitation.py` | `torque` ✅<br>`angular_acceleration` ✅<br>`angular_velocity` ✅<br>`angular_displacement` ✅<br>`moment_inertia_point / disk / rod_center / rod_end` ✅<br>`angular_momentum` ✅<br>`rotational_ke` ✅<br>`parallel_axis_theorem` ➕<br>`rotational_dynamics_composite` ➕<br><br>`gravitational_force` ✅<br>`gravitational_potential_energy` ✅<br>`gravitational_field` ✅<br>`kepler_third_law` ➕<br>`orbital_velocity` ➕ |
| **Soul Formation**<br>(Continuum Mechanics) | 化神期 | `continuum.py` | `stress` ✅<br>`strain` ✅<br>`youngs_modulus` ✅<br>`buoyant_force` ✅<br>`drag_force` ✅<br>`continuity` ✅<br>`bernoulli_pressure` ✅<br>`viscosity_shear_stress` ✅<br>`stress_tensor_2d` ➕<br>`navier_stokes_simplified` ➕<br>`poiseuille_flow_rate` ➕<br>`surface_tension_pressure` ➕ |
| **Tribulation Transcendence**<br>(Electromagnetism & Thermodynamics) | 渡劫期 | `electromagnetism.py`<br>`thermodynamics.py` | `coulomb_force` ✅<br>`electric_field_point` ✅<br>`lorentz_force_magnitude` ✅<br>`electric_flux` ✅<br>`magnetic_force_on_wire` ✅<br>`maxwell_faraday_law` ➕<br>`maxwell_ampere_law` ➕<br>`poynting_vector` ➕<br>`electromagnetic_wave_speed` ➕<br><br>`ideal_gas_pressure` ✅<br>`internal_energy_monatomic` ✅<br>`entropy_change_heat` ✅<br>`boltzmann_entropy` ✅<br>`average_kinetic_energy` ✅<br>`maxwell_boltzmann_probability` ✅<br>`heat_capacity_cp_cv` ➕<br>`carnot_efficiency` ➕<br>`clausius_clapeyron` ➕ |
| **Mahayana**<br>(Relativity, Waves, Quantum) | 大乘期 | `relativity.py`<br>`waves_optics.py`<br>`quantum.py` | `lorentz_factor` ✅<br>`time_dilation` ✅<br>`length_contraction` ✅<br>`relativistic_momentum` ✅<br>`energy_total` ✅<br>`energy_rest` ✅<br>`kinetic_energy_relativistic` ✅<br>`schwarzschild_radius` ➕<br>`gravitational_time_dilation` ➕<br><br>`simple_harmonic_motion` ✅<br>`angular_frequency_spring` ✅<br>`period_spring` ✅<br>`wave_speed` ✅<br>`doppler_shift_approaching` ✅<br>`snells_law` ✅<br>`lensmaker_formula` ✅<br>`thin_lens_equation` ➕<br>`interference_maxima` ➕<br><br>`photon_energy` ✅<br>`photon_wavelength` ✅<br>`de_broglie_wavelength` ✅<br>`uncertainty_position_momentum` ✅<br>`uncertainty_energy_time` ✅<br>`infinite_well_energy` ✅<br>`infinite_well_wavefunction` ✅<br>`quantum_harmonic_oscillator_energy` ➕<br>`tunneling_probability` ➕<br>`time_independent_schrodinger_1d` ➕ |

---

## 📜 Implementation Notes

- **Existing files** already contain all ✅ functions.
- **➕ functions** will be added directly to the respective `.py` files.
- **Vector operations** (e.g., `projectile_motion_vector`, `collision_2d`) will use `numpy` arrays (import `numpy as np`).
- **Simplified GR** includes only Schwarzschild radius and gravitational time dilation – no full tensor equations.
- **Quantum** additions include a basic numeric solver for 1D Schrödinger equation (finite difference) to illustrate the concept.
- **Testing** will be done later in separate files.

---

## 💎 Cultivator's Summary

> **此册既全，万法可通。**  
> *This manual is complete; all techniques become accessible.*

> **缺者当补，补则无漏。**  
> *What is missing shall be added; once added, nothing is lacking.*

> **阅罢准行，吾将执笔。**  
> *After you approve, I will write the code.*
