from utils import transfer_function


class LowPassRC:
    """
    RC low-pass filter
    H(s) = 1 / (RC s + 1)
    """

    def __init__(self, R=1, C=1e-3):
        self.R = R
        self.C = C

    def model(self):
        num = [1]
        den = [self.R * self.C, 1]
        return transfer_function(num, den)


class HighPassRC:
    """
    High-pass RC filter
    H(s) = (RC s) / (RC s + 1)
    """

    def __init__(self, R=1, C=1e-3):
        self.R = R
        self.C = C

    def model(self):
        num = [self.R * self.C, 0]
        den = [self.R * self.C, 1]
        return transfer_function(num, den)
