import numpy as np
import matplotlib.pyplot as plt

# --- Simulation settings ---
dt = 0.1
time = 20
steps = int(time / dt)

setpoint = 10

# --- Gains (adjust these) ---
Kp = 0.8
Ki = 0.2
Kd = 0.5

# --- System function ---
def simulate(controller_type):
    position = 0
    velocity = 0

    integral = 0
    prev_error = 0

    positions = []

    for step in range(steps):
        error = setpoint - position

        # Controllers
        if controller_type == "P":
            output = Kp * error

        elif controller_type == "PI":
            integral += error * dt
            output = Kp * error + Ki * integral

        elif controller_type == "PID":
            integral += error * dt
            derivative = (error - prev_error) / dt
            output = Kp * error + Ki * integral + Kd * derivative
            prev_error = error

        # Physics (mass = 1)
        acceleration = output
        velocity += acceleration * dt
        position += velocity * dt

        positions.append(position)

    return positions


# --- Run simulations ---
time_axis = np.arange(0, time, dt)

p_response = simulate("P")
pi_response = simulate("PI")
pid_response = simulate("PID")

# --- Plot ---
plt.figure(figsize=(10, 5))

plt.plot(time_axis, p_response, label="P Controller")
plt.plot(time_axis, pi_response, label="PI Controller")
plt.plot(time_axis, pid_response, label="PID Controller")

plt.axhline(setpoint, linestyle="--", label="Setpoint")

plt.xlabel("Time")
plt.ylabel("Position")
plt.title("P vs PI vs PID Control Comparison")
plt.legend()

plt.savefig("output.png", dpi=300, bbox_inches="tight")