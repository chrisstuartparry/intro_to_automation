import matplotlib.pyplot as plt
import numpy as np

import miller

def area(r, z):
    # abs because (r,z) start on the out-board midplane and r decreases
    return np.abs(np.trapezoid(z, r))


def plot_area(area, delta):
    plt.plot(area, delta)

def main():
    

if __name__ == "__main__":
    main()