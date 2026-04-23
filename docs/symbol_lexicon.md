# Symbol Lexicon

This lexicon exists to remove notation friction.

It is not a dictionary of every symbol in mathematics. It is a working reference for the symbols, operators, structures, and conventions that repeatedly appear in this repository.

For each item:
- **Symbol**
- **Name**
- **Meaning**
- **Units**
- **Plain English**
- **Notes / common traps**

---

# 1. Equality, approximation, and logical relation symbols

## `=`
**Name:** equals  
**Meaning:** exact equality  
**Units:** both sides must have the same units if the equation is physically meaningful  
**Plain English:** the left-hand side is exactly the same quantity as the right-hand side  
**Notes / common traps:**  
- In physics, an equation is not just arithmetic; it states a relationship between quantities.  
- Unit consistency is mandatory. If units do not match, something is wrong.

## `\approx`
**Name:** approximately equal to  
**Meaning:** not exact, but close enough for the current model or numerical method  
**Units:** both sides must still have matching units  
**Plain English:** these two quantities are close, but not identical  
**Notes / common traps:**  
- Common in numerical methods and approximations.  
- Euler stepping usually gives approximate, not exact, solutions.

## `\propto`
**Name:** proportional to  
**Meaning:** one quantity changes in direct proportion to another  
**Units:** depends on the full equation after the constant of proportionality is introduced  
**Plain English:** if one goes up, the other scales with it  
**Notes / common traps:**  
- `F \propto a` is incomplete; `F = ma` is the full equation.

## `<`, `>`, `\le`, `\ge`
**Name:** inequality symbols  
**Meaning:** less than, greater than, less than or equal to, greater than or equal to  
**Units:** both sides must have comparable units  
**Plain English:** compares magnitudes  
**Notes / common traps:**  
- In physics, comparing quantities with different units is meaningless.

---

# 2. Basic arithmetic operators

## `+`
**Name:** plus  
**Meaning:** addition  
**Units:** terms must have the same units  
**Plain English:** combine like quantities  
**Notes / common traps:**  
- You can add `3 m + 2 m`, but not `3 m + 2 s`.

## `-`
**Name:** minus  
**Meaning:** subtraction or negative sign  
**Units:** terms must have the same units  
**Plain English:** remove one like quantity from another, or indicate direction/sign  
**Notes / common traps:**  
- In mechanics, negative often means direction, not “bad.”  
- `a = -9.81 \,\text{m/s}^2` means acceleration downward if upward is chosen positive.

## `\times` or `*`
**Name:** multiplication  
**Meaning:** product of quantities  
**Units:** units multiply too  
**Plain English:** scale one quantity by another  
**Notes / common traps:**  
- If `v = a t`, then units become `(m/s^2)(s) = m/s`.

## `/`
**Name:** division  
**Meaning:** ratio of quantities  
**Units:** units divide too  
**Plain English:** one quantity per another quantity  
**Notes / common traps:**  
- Velocity is distance divided by time.  
- Density is mass divided by volume.

## `()`
**Name:** parentheses / brackets  
**Meaning:** grouping  
**Units:** depends on contents  
**Plain English:** do this part together  
**Notes / common traps:**  
- Critical for order of operations.  
- `(a+b)c` is not the same as `a+bc`.

---

# 3. Powers, roots, and exponents

## `x^2`
**Name:** x squared  
**Meaning:** `x \cdot x`  
**Units:** units are squared too  
**Plain English:** multiply the quantity by itself  
**Notes / common traps:**  
- If `x` is in metres, `x^2` is in square metres.

## `x^n`
**Name:** x to the power n  
**Meaning:** repeated multiplication  
**Units:** units raised to the same power  
**Plain English:** x multiplied by itself n times  
**Notes / common traps:**  
- Area and volume often involve squared and cubed units.

## `\sqrt{x}`
**Name:** square root of x  
**Meaning:** a number whose square gives x  
**Units:** root applies to units too  
**Plain English:** the quantity that, multiplied by itself, gives x  
**Notes / common traps:**  
- If `x` has units `m^2`, then `\sqrt{x}` has units `m`.

## `1/x` or `x^{-1}`
**Name:** reciprocal / inverse  
**Meaning:** multiplicative inverse  
**Units:** inverse units  
**Plain English:** one divided by the quantity  
**Notes / common traps:**  
- Frequency and period are reciprocals.

---

# 4. Common variables in mechanics

## `x`
**Name:** position  
**Meaning:** location along an axis  
**Units:** metres (`m`)  
**Plain English:** where the object is  
**Notes / common traps:**  
- Position is not distance travelled.  
- In 1D, `x` is often horizontal position.

## `y`
**Name:** vertical position  
**Meaning:** location along vertical axis  
**Units:** metres (`m`)  
**Plain English:** height or vertical location  
**Notes / common traps:**  
- Often positive upward, but sign convention must be stated.

## `z`
**Name:** depth / third spatial coordinate  
**Meaning:** position along the third axis  
**Units:** metres (`m`)  
**Plain English:** the third direction in 3D space

## `s`
**Name:** displacement or path variable, context-dependent  
**Meaning:** can mean displacement, arc length, or distance along a path  
**Units:** metres (`m`)  
**Plain English:** how far along the path or how much position changed  
**Notes / common traps:**  
- Must check context. Some books use `s` where others use `x`.

## `r`
**Name:** radius or position magnitude  
**Meaning:** distance from a center or origin  
**Units:** metres (`m`)  
**Plain English:** how far from the centre  
**Notes / common traps:**  
- In vectors, `\mathbf{r}` often means the position vector.

## `t`
**Name:** time  
**Meaning:** time variable  
**Units:** seconds (`s`)  
**Plain English:** when in the motion or process we are  
**Notes / common traps:**  
- Time is not timestep. See `dt`.

## `dt`
**Name:** timestep or differential time element  
**Meaning:** small time interval  
**Units:** seconds (`s`)  
**Plain English:** a small chunk of time  
**Notes / common traps:**  
- In calculus, `dt` can mean an infinitesimal integration variable.  
- In code, `dt` usually means a small but finite timestep.  
- Do not confuse `t` with `dt`.

## `v`
**Name:** velocity  
**Meaning:** rate of change of position with respect to time  
**Units:** metres per second (`m/s`)  
**Plain English:** how fast and in what direction position is changing  
**Notes / common traps:**  
- Velocity includes direction.  
- Speed is the magnitude of velocity.

## `u`
**Name:** initial velocity  
**Meaning:** starting value of velocity  
**Units:** metres per second (`m/s`)  
**Plain English:** velocity at the beginning  
**Notes / common traps:**  
- Common in school physics notation: `v = u + at`.

## `a`
**Name:** acceleration  
**Meaning:** rate of change of velocity with respect to time  
**Units:** metres per second squared (`m/s^2`)  
**Plain English:** how quickly velocity changes  
**Notes / common traps:**  
- Acceleration can be negative depending on coordinate choice.  
- Negative acceleration is not automatically “slowing down”; sign depends on direction.

## `g`
**Name:** gravitational acceleration near Earth  
**Meaning:** magnitude of gravitational acceleration near Earth’s surface  
**Units:** metres per second squared (`m/s^2`)  
**Plain English:** the acceleration due to gravity  
**Notes / common traps:**  
- Often taken as `9.81 \,\text{m/s}^2`.  
- In equations, sign depends on convention. If upward is positive, acceleration due to gravity is often `-g`.

## `m`
**Name:** mass  
**Meaning:** measure of inertia  
**Units:** kilograms (`kg`)  
**Plain English:** how much matter / resistance to acceleration an object has  
**Notes / common traps:**  
- Do not confuse mass with weight.

## `F`
**Name:** force  
**Meaning:** interaction that changes motion  
**Units:** newtons (`N = kg \cdot m/s^2`)  
**Plain English:** push or pull that can accelerate an object  
**Notes / common traps:**  
- Net force, not just any one force, determines acceleration.

## `W`
**Name:** weight or work, context-dependent  
**Meaning:** can mean gravitational force (`mg`) or work done  
**Units:** newtons (`N`) if weight; joules (`J`) if work  
**Plain English:** check context carefully  
**Notes / common traps:**  
- One of the most overloaded letters.

## `p`
**Name:** momentum or pressure, context-dependent  
**Meaning:** can mean linear momentum or pressure  
**Units:**  
- momentum: `kg \cdot m/s`  
- pressure: pascals (`Pa = N/m^2`)  
**Plain English:** context matters  
**Notes / common traps:**  
- In mechanics `p = mv` often means momentum.  
- In fluids/thermo `p` often means pressure.

## `E`
**Name:** energy  
**Meaning:** capacity associated with work, motion, configuration, fields, etc.  
**Units:** joules (`J`)  
**Plain English:** a conserved bookkeeping quantity in many systems  
**Notes / common traps:**  
- Must specify kinetic, potential, internal, etc.

## `K`
**Name:** kinetic energy  
**Meaning:** energy of motion  
**Units:** joules (`J`)  
**Plain English:** motion energy  
**Notes / common traps:**  
- Usually `K = \frac{1}{2}mv^2`.

## `U`
**Name:** potential energy  
**Meaning:** stored energy associated with configuration  
**Units:** joules (`J`)  
**Plain English:** energy due to position or configuration  
**Notes / common traps:**  
- Gravitational potential energy often `mgh` near Earth’s surface.

---

# 5. Greek letters that appear constantly

## `\Delta`
**Name:** capital delta  
**Meaning:** finite change in a quantity  
**Units:** same as the quantity being changed  
**Plain English:** change in  
**Notes / common traps:**  
- `\Delta x = x_{\text{final}} - x_{\text{initial}}`  
- Finite change, not derivative.

## `\delta`
**Name:** lowercase delta  
**Meaning:** small change or variation, depending on context  
**Units:** depends on quantity  
**Plain English:** a small difference or variation  
**Notes / common traps:**  
- Meaning varies by field.

## `\theta`
**Name:** theta  
**Meaning:** angle  
**Units:** radians usually, sometimes degrees  
**Plain English:** angular position  
**Notes / common traps:**  
- In serious math/physics, radians are usually preferred.

## `\omega`
**Name:** omega  
**Meaning:** angular velocity or angular frequency  
**Units:** radians per second (`rad/s`)  
**Plain English:** rate of angular change  
**Notes / common traps:**  
- Must distinguish from ordinary frequency `f`.

## `\alpha`
**Name:** alpha  
**Meaning:** often angular acceleration, coefficient, or parameter  
**Units:** depends on context  
**Plain English:** context-dependent symbol  
**Notes / common traps:**  
- In rotational mechanics, often angular acceleration.

## `\rho`
**Name:** rho  
**Meaning:** density  
**Units:** kilograms per cubic metre (`kg/m^3`)  
**Plain English:** mass per volume  
**Notes / common traps:**  
- Common in fluids and continuum mechanics.

## `\mu`
**Name:** mu  
**Meaning:** coefficient, reduced mass, permeability, micro-prefix, etc.  
**Units:** context-dependent  
**Plain English:** overloaded symbol; always check context  
**Notes / common traps:**  
- `\mu_k` and `\mu_s` often mean friction coefficients.

## `\sigma`
**Name:** sigma  
**Meaning:** stress, standard deviation, conductivity, sum symbol when capitalized  
**Units:** context-dependent  
**Plain English:** overloaded symbol  
**Notes / common traps:**  
- `\Sigma` and `\sigma` are not the same.

## `\lambda`
**Name:** lambda  
**Meaning:** wavelength, eigenvalue, parameter, decay rate, etc.  
**Units:** context-dependent  
**Plain English:** another overloaded symbol

## `\pi`
**Name:** pi  
**Meaning:** mathematical constant about `3.14159`  
**Units:** dimensionless  
**Plain English:** the constant relating circle circumference to diameter  
**Notes / common traps:**  
- Not a variable unless explicitly defined otherwise.

---

# 6. Subscripts and superscripts

## `x_0`
**Name:** x naught / x zero  
**Meaning:** initial value of x  
**Units:** same as `x`  
**Plain English:** the starting position  
**Notes / common traps:**  
- Subscript often marks initial condition or index.

## `v_i`
**Name:** v sub i  
**Meaning:** initial velocity or ith component/value depending on context  
**Units:** same as `v`  
**Plain English:** check whether `i` means “initial” or an index  
**Notes / common traps:**  
- Notation is context-sensitive.

## `x_f`
**Name:** x sub f  
**Meaning:** final position  
**Units:** metres (`m`)  
**Plain English:** ending position

## `v_x`, `v_y`, `v_z`
**Name:** x/y/z components of velocity  
**Meaning:** component of velocity along each axis  
**Units:** metres per second (`m/s`)  
**Plain English:** how much of the velocity points in each direction  
**Notes / common traps:**  
- Components are not separate velocities of separate objects.

## `a_n`
**Name:** nth value of a sequence or nth time-step acceleration  
**Meaning:** indexed quantity  
**Units:** same as `a`  
**Plain English:** the acceleration at step n or the nth listed acceleration

## `x^2`
**Name:** superscript power  
**Meaning:** square of x  
**Units:** squared units  
**Plain English:** x multiplied by itself  
**Notes / common traps:**  
- Superscripts can also indicate components in tensor notation in advanced contexts; do not assume every superscript is a power.

---

# 7. Functions and mappings

## `f(x)`
**Name:** f of x  
**Meaning:** function evaluated at x  
**Units:** depends on the function  
**Plain English:** the output of the function when the input is x  
**Notes / common traps:**  
- `f(x)` is not always multiplication of `f` and `x`.

## `\sin\theta`, `\cos\theta`, `\tan\theta`
**Name:** sine, cosine, tangent  
**Meaning:** trigonometric functions  
**Units:** dimensionless outputs for dimensionless angular input  
**Plain English:** standard angle-based ratios / functions  
**Notes / common traps:**  
- In calculus/physics, angle input is usually in radians.

## `\ln x`
**Name:** natural logarithm of x  
**Meaning:** logarithm base `e`  
**Units:** argument should usually be dimensionless  
**Plain English:** the power to which `e` must be raised to get x  
**Notes / common traps:**  
- Logs of dimensional quantities are dangerous unless normalized.

## `e^x`
**Name:** exponential  
**Meaning:** `e` raised to x  
**Units:** exponent should be dimensionless  
**Plain English:** exponential growth/decay form  
**Notes / common traps:**  
- Common in decay, oscillation, and differential equations.

---

# 8. Calculus notation

## `\frac{dx}{dt}`
**Name:** derivative of x with respect to t  
**Meaning:** instantaneous rate of change of x with time  
**Units:** units of `x` divided by units of `t`  
**Plain English:** how fast x is changing right now  
**Notes / common traps:**  
- If `x` is position, then `dx/dt = v`.

## `\frac{dv}{dt}`
**Name:** derivative of velocity with respect to time  
**Meaning:** instantaneous acceleration  
**Units:** `m/s^2`  
**Plain English:** how fast velocity is changing right now  
**Notes / common traps:**  
- If acceleration is constant, this derivative is constant.

## `\frac{d^2x}{dt^2}`
**Name:** second derivative of x with respect to t  
**Meaning:** acceleration if x is position  
**Units:** `m/s^2`  
**Plain English:** the rate of change of the rate of change of position  
**Notes / common traps:**  
- This is not “x squared.”

## `\int`
**Name:** integral sign  
**Meaning:** accumulation / continuous sum  
**Units:** integrand units multiplied by integration variable units  
**Plain English:** add up infinitely many tiny contributions  
**Notes / common traps:**  
- If you integrate velocity over time, you get displacement.

## `\int_a^b f(x)\,dx`
**Name:** definite integral  
**Meaning:** accumulated quantity from x = a to x = b  
**Units:** units of `f(x)` times units of `x`  
**Plain English:** add up the contribution of `f(x)` from a to b  
**Notes / common traps:**  
- Bounds matter.

## `d`
**Name:** differential symbol  
**Meaning:** indicates the variable of differentiation or integration  
**Units:** same as the variable  
**Plain English:** tiny change in  
**Notes / common traps:**  
- In code, `dt` is usually finite. In calculus, `dt` is part of exact notation.

## `\partial`
**Name:** partial derivative symbol  
**Meaning:** derivative with respect to one variable while holding others fixed  
**Units:** depends on variables involved  
**Plain English:** rate of change in one direction while freezing the rest  
**Notes / common traps:**  
- Important for multivariable calculus and fields.

## `\nabla`
**Name:** nabla / del operator  
**Meaning:** vector differential operator  
**Units:** inverse length in spatial use  
**Plain English:** a compact symbol used for gradient, divergence, and curl  
**Notes / common traps:**  
- Appears later in fields, fluids, and electromagnetism.

---

# 9. Vector notation

## `\mathbf{v}`
**Name:** vector v  
**Meaning:** quantity with magnitude and direction  
**Units:** same physical units as its components  
**Plain English:** a directed quantity  
**Notes / common traps:**  
- Boldface marks vector status in many texts.

## `|\mathbf{v}|` or `\|\mathbf{v}\|`
**Name:** magnitude / norm of vector v  
**Meaning:** size of the vector regardless of direction  
**Units:** same as the vector  
**Plain English:** how big the vector is  
**Notes / common traps:**  
- Speed is the magnitude of velocity.

## `\hat{\mathbf{i}}, \hat{\mathbf{j}}, \hat{\mathbf{k}}`
**Name:** unit vectors in x, y, z directions  
**Meaning:** basis directions  
**Units:** dimensionless  
**Plain English:** pure directions with length 1  
**Notes / common traps:**  
- Used to write vectors as component sums.

## `\mathbf{a} \cdot \mathbf{b}`
**Name:** dot product  
**Meaning:** scalar product of two vectors  
**Units:** product of vector units  
**Plain English:** measures alignment and combines magnitudes  
**Notes / common traps:**  
- Gives a scalar, not a vector.

## `\mathbf{a} \times \mathbf{b}`
**Name:** cross product  
**Meaning:** vector product in 3D  
**Units:** product of vector units  
**Plain English:** produces a vector perpendicular to both  
**Notes / common traps:**  
- Order matters: `\mathbf{a} \times \mathbf{b} = -(\mathbf{b} \times \mathbf{a})`.

---

# 10. Common numerical-method symbols

## `n`
**Name:** step index  
**Meaning:** counts discrete time steps  
**Units:** dimensionless  
**Plain English:** which step of the computation we are on  
**Notes / common traps:**  
- `x_n` means x at step n.

## `n+1`
**Name:** next step index  
**Meaning:** the value after one numerical update  
**Units:** dimensionless  
**Plain English:** the next computed step

## `x_n`
**Name:** x at step n  
**Meaning:** position at the current discrete step  
**Units:** metres (`m`)  
**Plain English:** the position now, in the discrete update scheme

## `x_{n+1}`
**Name:** x at step n plus one  
**Meaning:** position after one update  
**Units:** metres (`m`)  
**Plain English:** the next position after one timestep

## `v_{n+1} = v_n + a_n \, dt`
**Name:** Euler velocity update  
**Meaning:** discrete approximation for the next velocity  
**Units:** `m/s` on both sides  
**Plain English:** next velocity equals current velocity plus acceleration times timestep  
**Notes / common traps:**  
- Exact only in limited cases such as constant acceleration over the step.  
- Otherwise approximate.

## `x_{n+1} = x_n + v_n \, dt`
**Name:** Euler position update  
**Meaning:** discrete approximation for next position  
**Units:** metres (`m`) on both sides  
**Plain English:** next position equals current position plus current velocity times timestep  
**Notes / common traps:**  
- This uses current velocity, not future velocity.  
- Approximation quality depends on timestep size and model behaviour.

## `O(dt)`
**Name:** order dt / big-O notation  
**Meaning:** error scales like timestep size  
**Units:** depends on context  
**Plain English:** the error shrinks roughly in proportion to dt  
**Notes / common traps:**  
- Common when comparing numerical methods.  
- Later topic, but worth recognizing early.

---

# 11. Units shorthand that will recur constantly

## `m`
**Name:** metre  
**Meaning:** unit of length

## `s`
**Name:** second  
**Meaning:** unit of time

## `kg`
**Name:** kilogram  
**Meaning:** unit of mass

## `N`
**Name:** newton  
**Meaning:** unit of force  
**Definition:** `1 N = 1 kg \cdot m/s^2`

## `J`
**Name:** joule  
**Meaning:** unit of energy / work  
**Definition:** `1 J = 1 N \cdot m = 1 kg \cdot m^2/s^2`

## `Pa`
**Name:** pascal  
**Meaning:** unit of pressure / stress  
**Definition:** `1 Pa = 1 N/m^2`

## `Hz`
**Name:** hertz  
**Meaning:** unit of frequency  
**Definition:** `1 Hz = 1/s`

## `rad`
**Name:** radian  
**Meaning:** angular measure  
**Notes / common traps:**  
- Often treated as dimensionless in analysis, but physically useful to track conceptually.

---

# 12. First formulas to read fluently

## `v = \frac{dx}{dt}`
**Meaning:** velocity is the rate of change of position with respect to time  
**Plain English:** velocity tells how fast position changes

## `a = \frac{dv}{dt}`
**Meaning:** acceleration is the rate of change of velocity with respect to time  
**Plain English:** acceleration tells how fast velocity changes

## `F = ma`
**Meaning:** net force equals mass times acceleration  
**Plain English:** stronger force or smaller mass gives greater acceleration  
**Unit check:** `kg \cdot m/s^2 = N`

## `p = mv`
**Meaning:** momentum equals mass times velocity  
**Plain English:** moving mass carries momentum

## `K = \frac{1}{2}mv^2`
**Meaning:** kinetic energy  
**Plain English:** moving objects carry energy that scales with mass and with velocity squared

## `v_{n+1} = v_n + a_n dt`
**Meaning:** discrete velocity update  
**Plain English:** new velocity is old velocity plus acceleration over one timestep

## `x_{n+1} = x_n + v_n dt`
**Meaning:** discrete position update  
**Plain English:** new position is old position plus velocity over one timestep

---

# 13. Common traps summary

1. **Position is not distance travelled.**
2. **Velocity is not speed.**
3. **Acceleration is not the same thing as velocity.**
4. **Negative sign often means direction, not “less motion.”**
5. **`dt` in code is finite; `dt` in calculus notation is idealized.**
6. **You cannot add quantities with different units.**
7. **A superscript is not always a power in advanced notation.**
8. **A letter does not have one eternal meaning across all physics. Context rules.**
9. **Euler updates are approximations, not exact truth.**
10. **Every physically meaningful equation must balance dimensionally.**

---

# 14. Minimum operational fluency target

For Sprint 1, the reader should be able to look at

\[
x_{n+1} = x_n + v_n dt
\]

and say, without hesitation:

- `x_{n+1}` = next position
- `x_n` = current position
- `v_n` = current velocity
- `dt` = timestep
- units: metres = metres + (metres/second)(seconds)
- plain English: next position equals current position plus movement during one timestep
- status: discrete approximation used in numerical simulation

Likewise for

\[
v_{n+1} = v_n + a_n dt
\]

the reader should be able to decode every symbol, state units, and explain why it is only exact under limited assumptions.
