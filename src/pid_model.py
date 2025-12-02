from scipy import signal
from utils import transfer_function


class PIDController:
    def __init__(self, kp=1, ki=0, kd=0):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def model(self):
        num = [self.kd, self.kp, self.ki]
        den = [1, 0]
        return transfer_function(num, den)
