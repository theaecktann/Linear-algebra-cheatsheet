import numpy as np
from typing import Tuple

# Basic vector operations
def vector_basics() -> Tuple[np.ndarray, np.ndarray]:
    v1 = np.array([3, 4])
    v2 = np.array([1, -2])

    print("Vectors:")
    print(f"v1 = {v1}, v2 = {v2}")
    print(f"Sum: {v1 + v2}")
    print(f"Norm of v1: {np.linalg.norm(v1):.2f}")
    print(f"Dot product: {np.dot(v1, v2)}")
    return v1, v2

# Basic matrix operations
def matrix_operations() -> Tuple[np.ndarray, np.ndarray]:
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Matrices:")
    print(f"A =\n{A}\nB =\n{B}")
    print(f"A @ B (matrix multiplication) =\n{A @ B}")
    print(f"A * B (element-wise multiplication) =\n{A * B}")
    return A, B

# Eigenvalues and eigenvectors
def eigen_decomposition() -> Tuple[np.ndarray, np.ndarray]:
    C = np.array([[4, 2], [2, 3]])
    vals, vecs = np.linalg.eigh(C)  # eigh is optimized for symmetric matrixes

    print("Eigen decomposition:")
    print(f"Eigenvalues (lambda): {np.round(vals, 2)}")
    print(f"Eigenvectors (v):\n{np.round(vecs, 2)}")

    v0 = vecs[:, 0]
    lam0 = vals[0]
    print(f"Check C @ v0 == lambda0 * v0: {np.allclose(C @ v0, lam0 * v0)}")
    return vals, vecs