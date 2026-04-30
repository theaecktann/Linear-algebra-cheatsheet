import matplotlib.pyplot as plt
import numpy as np
import os

ASSETS_DIR = "assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def plot_vectors(v1: np.ndarray, v2: np.ndarray):
    plt.figure(figsize=(5, 5))
    plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
    plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
    plt.xlim(-3, 5)
    plt.ylim(-3, 5)
    plt.grid(True)
    plt.legend()
    plt.title("Vectors in R2")
    path = os.path.join(ASSETS_DIR, "vectors.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Plot saved to: {path}")

def plot_matrix_heatmap(A: np.ndarray):
    plt.figure(figsize=(4, 4))
    plt.imshow(A, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title("Matrix A (heatmap)")
    path = os.path.join(ASSETS_DIR, "matrix_heatmap.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Plot saved to: {path}")