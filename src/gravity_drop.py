from euler_step import euler_step


def exact_position(x0, v0, a, t):
    return x0 + v0 * t + 0.5 * a * t * t


def exact_velocity(v0, a, t):
    return v0 + a * t


def run_gravity_drop():
    initial_position = 10.0
    initial_velocity = 0.0
    acceleration = -9.81
    dt = 0.1
    total_time = 1.0

    position = initial_position
    velocity = initial_velocity
    time = 0.0
    steps = int(total_time / dt)

    print("time_s, euler_position_m, exact_position_m, euler_velocity_m_per_s, exact_velocity_m_per_s")

    for _ in range(steps + 1):
        exact_x = exact_position(initial_position, initial_velocity, acceleration, time)
        exact_v = exact_velocity(initial_velocity, acceleration, time)

        print(
            f"{time:.2f}, "
            f"{position:.4f}, {exact_x:.4f}, "
            f"{velocity:.4f}, {exact_v:.4f}"
        )

        if time < total_time:
            position, velocity = euler_step(position, velocity, acceleration, dt)
            time += dt


if __name__ == "__main__":
    run_gravity_drop()

