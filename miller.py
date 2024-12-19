import matplotlib.pyplot as plt
import numpy as np


def flux_surface(
    A: float = 2.2,
    kappa: float = 1.5,
    delta: float = 0.3,
    R0: float = 2.5,
    theta: np.ndarray | tuple[np.ndarray | float] = np.linspace(0, 2 * np.pi),
) -> tuple[np.ndarray, np.ndarray]:
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

    r: float = R0 / A
    R_s: np.ndarray = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s: np.ndarray = kappa * r * np.sin(theta)
    return (R_s, Z_s)


def plot_surface(R_s, Z_s, savefig=True) -> None:
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
        plt.savefig("miller.png")


def main():
    R_s, Z_s = flux_surface()
    plot_surface(R_s, Z_s)


if __name__ == "__main__":
    main()
