def euler_step(position, velocity, acceleration, dt):
    """
    Advance position and velocity by one Euler timestep.

    Parameters
    ----------
    position : float
        Current position in metres.
    velocity : float
        Current velocity in metres per second.
    acceleration : float
        Current acceleration in metres per second squared.
    dt : float
        Timestep in seconds.

    Returns
    -------
    tuple[float, float]
        (new_position, new_velocity)
    """
    new_velocity = velocity + acceleration * dt
    new_position = position + velocity * dt
    return new_position, new_velocity

