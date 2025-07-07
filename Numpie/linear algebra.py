# linear algebra

# | Function                   | Purpose                        |
# | -------------------------- | ------------------------------ |
# | `np.dot()` / `np.matmul()` | Matrix multiplication          |
# | `np.transpose()`           | Transpose a matrix             |
# | `np.linalg.inv()`          | Matrix inverse                 |
# | `np.linalg.det()`          | Determinant                    |
# | `np.linalg.eig()`          | Eigenvalues & eigenvectors     |
# | `np.linalg.norm()`         | Vector/matrix norm (magnitude) |

import numpy as np

# Define 2D square matrix A and vector b
A = np.array([[2, 1], [1, 3]])
b = np.array([8, 13])

print("Matrix A:\n", A)
print("Vector b:", b)

# 1. Matrix Transpose
print("\nTranspose of A:\n", A.T)

# 2. Matrix Multiplication
dot_result = np.dot(A, b)
print("\nDot Product A • b:", dot_result)

# 3. Matrix Inverse
inv_A = np.linalg.inv(A)
print("\nInverse of A:\n", inv_A)

# 4. Solve Ax = b using inverse
x = np.dot(inv_A, b)
print("\nSolution x (from inv):", x)

# 5. Solve Ax = b directly (more stable)
x_direct = np.linalg.solve(A, b)
print("Solution x (using solve):", x_direct)

# 6. Determinant of A
det = np.linalg.det(A)
print("\nDeterminant of A:", det)

# 7. Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
