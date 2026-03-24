import numpy as np
from tqdm import tqdm

from utils import bin_mul, remove_rows, get_rank
from data import data


def main():
    X = np.array(data)
    m, n = X.shape
    print(f'X: {m} rows, {n} cols')

    original_rank, _, _ = get_rank(X)
    print(f'Rank: {original_rank}')

    # Find bad rows
    bad_rows = []
    for i in range(m):
        X1 = remove_rows(X, bad_rows+[i])
        basis_rank, _, _ = get_rank(X1)
        if basis_rank < original_rank - len(bad_rows):
            bad_rows.append(i)
    print(f'Bad rows: {bad_rows}')

    # Build basis for good rows
    X1 = remove_rows(X, bad_rows)
    basis_rank, A, pivots = get_rank(X1)
    B = A[:basis_rank, :]
    print(f'Basis:')
    print(B)

    # Build a basis for B * C^T = 0 solutions space
    C = np.zeros((n-basis_rank, n), dtype=int)
    j = 0
    for i in range(n):
        if i in pivots:
            continue
        C[j, :] = bin_mul(B[:, i].T, B)
        j += 1
    print(f'C:')
    print(C)

    # Precompute syndromes for 1-bit and 2-bit errors
    lookup_syndromes = {}
    for i in range(n):
        for j in range(i, n):
            e = np.zeros(n, dtype=int)
            e[i] = e[j] = 1
            syn = tuple(bin_mul(C, e))
            lookup_syndromes[syn] = e
    
    # Fix bad rows
    X_fixed = X.copy()
    for row in bad_rows:
        syn = tuple(bin_mul(C, X[row, :].T))
        if syn in lookup_syndromes:
            print(f'Row {row:2}: syndrome {np.array(syn)}, fix by {lookup_syndromes[syn]}')
            X_fixed[row, :] ^= lookup_syndromes[syn]
        else:
            print(f'Unable to fix row {row}')
    
    # Check
    res = bin_mul(C, X_fixed.T)
    print('=' * 20)
    print(f'Checking C @ X_fixed.T:')
    print(res)


if __name__ == "__main__":
    main()
