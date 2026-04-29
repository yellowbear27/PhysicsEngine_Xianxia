# Euler Gravity Drop: Exact vs Numerical Comparison

## Setup

We simulate a falling object with:

- initial position: \(x_0 = 10.0 \, \text{m}\)
- initial velocity: \(v_0 = 0.0 \, \text{m/s}\)
- constant acceleration: \(a = -9.81 \, \text{m/s}^2\)
- total simulation time: \(t = 1.0 \, \text{s}\)

Upward is taken as positive, so gravity is negative.

---

## Exact solution

For constant acceleration:

\[
x(t) = x_0 + v_0 t + \frac{1}{2} a t^2
\]

\[
v(t) = v_0 + at
\]

At \(t=1.0\):

\[
x(1) = 10.0 + 0.0 + \frac{1}{2}(-9.81)(1.0)^2 = 5.095 \, \text{m}
\]

\[
v(1) = 0.0 + (-9.81)(1.0) = -9.81 \, \text{m/s}
\]

---

## Euler update equations

\[
v_{n+1} = v_n + a_n dt
\]

\[
x_{n+1} = x_n + v_n dt
\]

These are discrete timestep updates.

---

## Numerical result for \(dt = 0.1\)

At \(t=1.0\):

- Euler position = \(5.5855 \, \text{m}\)
- Exact position = \(5.0950 \, \text{m}\)
- Absolute error = \(0.4905 \, \text{m}\)

- Euler velocity = \(-9.8100 \, \text{m/s}\)
- Exact velocity = \(-9.8100 \, \text{m/s}\)

---

## Error vs timestep

| dt | Euler position | Exact position | Absolute error |
|---|---:|---:|---:|
| 0.100 | 5.585500 | 5.095000 | 0.490500 |
| 0.050 | 5.340250 | 5.095000 | 0.245250 |
| 0.010 | 5.144050 | 5.095000 | 0.049050 |
| 0.001 | 5.099905 | 5.095000 | 0.004905 |

---

## Interpretation

As the timestep becomes smaller, the position error becomes smaller.

In this experiment, reducing \(dt\) by a factor of 10 reduces the error by about a factor of 10.

That suggests first-order error scaling in \(dt\) for the Euler position update in this constant-acceleration problem.

---

## Why the position is wrong but the velocity is right

The velocity update is exact here because acceleration is constant.

The position update is approximate because it uses the current velocity over the full timestep:

\[
x_{n+1} = x_n + v_n dt
\]

But the object is accelerating during the step, so the true motion over that interval is not captured exactly by holding velocity fixed at its old value.

That is why Euler overestimates the height of the falling object.

---

## Conclusion

This experiment shows three important points:

1. Euler stepping can produce physically sensible motion.
2. Exact benchmarks are necessary to judge numerical quality.
3. Smaller timesteps improve accuracy, but at greater computational cost.
