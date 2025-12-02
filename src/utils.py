import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def plot_step_response(system, title="Step Response"):
    t, y = signal.step(system)
    plt.figure()
    plt.plot(t, y)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()


def plot_bode(system, title="Bode Plot"):
    w, mag, phase = signal.bode(system)

    plt.figure()
    plt.semilogx(w, mag)
    plt.title(f"{title} - Magnitude")
    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)

    plt.figure()
    plt.semilogx(w, phase)
    plt.title(f"{title} - Phase")
    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("Phase (deg)")
    plt.grid(True)
    plt.show()


def transfer_function(num, den):
    return signal.TransferFunction(num, den)
