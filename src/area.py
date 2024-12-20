import matplotlib.pyplot as plt
import numpy as np

import miller


def calculate_area(r, z):
    # abs because (r,z) start on the out-board midplane and r decreases
    return np.abs(np.trapezoid(z, r))


def plot_area(area, delta):
    plt.plot(area, delta)


def main():
    deltas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    areas = []
    for delta in deltas:
        R_s, Z_s = miller.flux_surface(delta=delta)
        areas.append(calculate_area(R_s, Z_s))
    plt.plot(areas, deltas)
    plt.show()


if __name__ == "__main__":
    main()
