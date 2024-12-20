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
        A (float, optional): Area. Defaults to 2.2.
        kappa (float, optional): Elongation. Defaults to 1.5.
        delta (float, optional): Triangularity. Defaults to 0.3.
        R0 (float, optional): Major radius of the magnetic axis. Defaults to 2.5.
        theta (_type_, optional): Geometric poloidal angle. Defaults to np.linspace(0, 2 * np.pi).

    Returns:
        tuple[np.ndarray, np.ndarray]: Tuple of major radius of the flux surface and the vertical coordinate of the flux surface.
    """

    r: float = R0 / A
    R_s: np.ndarray = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s: np.ndarray = kappa * r * np.sin(theta)
    return (R_s, Z_s)


def plot_surface(R_s, Z_s, ax=None, savefig=True) -> None:
    """Plots the results from flux_surface()

    Args:
        R_s (np.ndarray): Major radius of the flux surface
        Z_s (np.ndarray): Vertical coordinate of the flux surface
    """
    if ax is None:
        _, ax = plt.subplots()

    ax.plot(R_s, Z_s)
    ax.axis("equal")
    ax.set_xlabel("R [m]")
    ax.set_ylabel("Z [m]")

    if savefig:
        plt.savefig("miller.png")


def main():
    R_s, Z_s = flux_surface()
    plot_surface(R_s, Z_s)


if __name__ == "__main__":
    main()
