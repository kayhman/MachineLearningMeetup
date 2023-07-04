import numpy as np

# The matrix A contains
# our system.
A = [[2, 1,    1, -1],
     [0, 1.5, -1,  0],
     [0, 0,    3, -1],
     [0, 0,    0,  1]]

# the column matrix B
# contains the right-hand side
B = [0, 0, 2, 43]

# The Gauss Seidel function
# calculates an approximate
# solution to our system.
def gaussSeidel(A, B, maxIter):
    nligsA, ncolsA = len(A), len(A[0])
    X = [0.0] * ncolsA

    for j in range(0, maxIter):
        for i in range(0, ncolsA):
            X[i] = 0
            X[i] = (B[i] - np.dot([col for col in A[i]], X)) / A[i][i]
    return X

# With only one iteration
# we are far from the result.
print(gaussSeidel(A, B, 1))
# > [0.0, 0.0, 0.666, 43.0]
# With one more
# we get closer
print(gaussSeidel(A, B, 2))
# > [21.166666666666668, 0.4444444444444444, 15.0, 43.0]

# and two more
# are enough to find the
# exact solution.
print(gaussSeidel(A, B, 4))
# > [9.0, 10.0, 15.0, 43.0]