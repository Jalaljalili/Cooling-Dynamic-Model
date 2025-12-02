import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def rc_transfer_function(R, C):
    return signal.TransferFunction([1], [C, 1/R])


def show_step_response(system):
    t, y = signal.step(system)
    plt.figure()
    plt.plot(t, y)
    plt.title("Step Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature")
    plt.grid(True)
    plt.show()


def show_bode(system):
    w, mag, phase = signal.bode(system)

    plt.figure()
    plt.semilogx(w, mag)
    plt.title("Bode Magnitude")
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.semilogx(w, phase)
    plt.title("Bode Phase")
    plt.grid(True)
    plt.show()


def pid_compare(R, C, factor, sim_time):
    tau = R * C
    t = np.linspace(0, sim_time, 300)

    y_no_ctrl = 1 - np.exp(-t / tau)
    y_pid = 1 - np.exp(-t / (tau / factor))

    plt.figure()
    plt.plot(t, y_no_ctrl, label="No Control")
    plt.plot(t, y_pid, label="PID Approx")
    plt.legend()
    plt.grid(True)
    plt.show()


def pid_final_sim(R, C, Kp, Ki, Kd, T_initial,
                  T_set, U_MAX, sim_time, dt,
                  d_start, d_end, d_value):

    tau = R * C
    t = np.arange(0, sim_time, dt)
    T = np.zeros_like(t)
    T[0] = T_initial

    integral = 0
    prev_error = 0

    dist = np.zeros_like(t)
    dist[int(d_start / dt):int(d_end / dt)] = d_value

    for i in range(1, len(t)):
        error = T_set - T[i-1]
        integral += error * dt
        derivative = (error - prev_error) / dt

        u = Kp*error + Ki*integral + Kd*derivative
        u = np.clip(u, 0, U_MAX)

        dT = (-(T[i-1]) + u*R + dist[i]) / tau
        T[i] = T[i-1] + dT*dt

        prev_error = error

    plt.figure()
    plt.plot(t, T)
    plt.axhline(T_set, color="r", linestyle="--")
    plt.grid(True)
    plt.title("PID Temperature Control")
    plt.show()


if __name__ == "__main__":
    print("--- Thermal & PID Control Simulation ---")
    R = float(input("R: "))
    C = float(input("C: "))

    G = rc_transfer_function(R, C)
    show_step_response(G)
    show_bode(G)

    factor = float(input("PID factor: "))
    pid_compare(R, C, factor, sim_time=40)

    print("\nPID Parameters:")
    Kp = float(input("Kp: "))
    Ki = float(input("Ki: "))
    Kd = float(input("Kd: "))

    T_initial = float(input("Initial temp: "))
    T_set = float(input("Set temp: "))
    U_MAX = float(input("Max heater: "))
    sim_time = float(input("Simulation time: "))
    dt = float(input("dt: "))
    d_start = float(input("dist start: "))
    d_end = float(input("dist end: "))
    d_value = float(input("dist value: "))

    pid_final_sim(
        R, C, Kp, Ki, Kd, T_initial, T_set,
        U_MAX, sim_time, dt,
        d_start, d_end, d_value
    )
