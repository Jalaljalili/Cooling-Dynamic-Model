from pid_model import PIDController
from rc_model import LowPassRC
from utils import plot_step_response, plot_bode


def main():
    # --- PID example ---
    pid = PIDController(kp=1, ki=5, kd=0.2)
    G_pid = pid.model()

    print("PID System Transfer Function:")
    print(G_pid)

    plot_step_response(G_pid, "PID Step Response")
    plot_bode(G_pid, "PID Bode Plot")

    # --- RC example ---
    rc = LowPassRC(R=1, C=0.001)
    G_rc = rc.model()

    print("RC Low Pass Transfer Function:")
    print(G_rc)

    plot_step_response(G_rc, "RC Step Response")
    plot_bode(G_rc, "RC Bode Plot")


if __name__ == "__main__":
    main()
