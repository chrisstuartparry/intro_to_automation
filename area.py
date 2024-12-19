import numpy as np


def area(r, z):
    # abs because (r,z) start on the out-board midplane and r decreases
    return np.abs(np.trapezoid(z, r))
