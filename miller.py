from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def flux_surface(A=2.2, kappa=1.5, delta=0.3, R0=2.5, theta=np.linspace(0, 2 * np.pi)):
    """Calculates flux surface, I think

    Args:
        A (float, optional): _description_. Defaults to 2.2.
        kappa (float, optional): _description_. Defaults to 1.5.
        delta (float, optional): _description_. Defaults to 0.3.
        R0 (float, optional): _description_. Defaults to 2.5.
        theta (_type_, optional): _description_. Defaults to np.linspace(0, 2 * np.pi).

    Returns:
        _type_: _description_
    """

    r = R0 / A
    R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s = kappa * r * np.sin(theta)
    return (R_s, Z_s)


def generate_image_filepath(file_name="miller.png"):
    current_path = Path.cwd()
    new_filedir = current_path / "figures"
    new_filedir.mkdir(exist_ok=True)
    new_filepath = new_filedir / file_name
    return new_filepath


def plot_surface(R_s, Z_s, file_path, savefig=True):
    """Plots the results from flux_surface()

    Args:
        R_s (_type_): _description_
        Z_s (_type_): _description_
    """
    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    if savefig:
        plt.savefig(file_path)


def main():
    R_s, Z_s = flux_surface()
    plot_surface(R_s, Z_s, generate_image_filepath())


if __name__ == "__main__":
    main()
