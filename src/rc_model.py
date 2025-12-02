from scipy import signal

def get_rc_transfer_function(R, C):
    return signal.TransferFunction([1], [C, 1/R])
