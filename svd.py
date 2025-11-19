import numpy as np

A = np.array([[1,2],
              [3,4]])

U, S, VT = np.linalg.svd(A)

print("U:\n", U)
print("Singular Values:\n", S)
print("V^T:\n", VT)
