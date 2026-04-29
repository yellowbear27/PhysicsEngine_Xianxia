from euler_step import euler_step


def exact_position(x0, v0, a, t):
    return x0 + v0 * t + 0.5 * a * t * t


def simulate(dt):
    position = 10.0
    velocity = 0.0
    acceleration = -9.81
    total_time = 1.0

    steps = int(total_time / dt)

    for _ in range(steps):
        position, velocity = euler_step(position, velocity, acceleration, dt)

    return position


def main():
    x0 = 10.0
    v0 = 0.0
    a = -9.81
    t = 1.0

    exact = exact_position(x0, v0, a, t)

    print("dt, euler_position, exact_position, abs_error")

    for dt in [0.1, 0.05, 0.01, 0.001]:
        numerical = simulate(dt)
        error = abs(numerical - exact)

        print(f"{dt:.3f}, {numerical:.6f}, {exact:.6f}, {error:.6f}")


if __name__ == "__main__":
    main()

