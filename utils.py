import numpy as np


# Matmul over Z(2)
def bin_mul(A, B):
    return (A@B) % 2


# Filter rows from a matrix A
def remove_rows(A, rows):
    mask = np.ones(A.shape[0], dtype=bool)
    mask[rows] = False
    return A[mask].copy()


# Rank-revealing Gaussian elimination
def get_rank(A):
    A = A.astype(int).copy()
    m, n = A.shape
    row = 0
    rank = 0
    pivot_cols = []

    for col in range(n):
        pivot = None
        for r in range(row, m):
            if A[r, col] == 1:
                pivot = r
                break
        if pivot is None:
            continue

        pivot_cols.append(col)

        A[[row, pivot]] = A[[pivot, row]]

        for r in range(0, m):
            if r == row:
                continue
            if A[r, col] == 1:
                A[r] ^= A[row]

        rank += 1
        row += 1
        if row == m:
            break

    return rank, A, pivot_cols
