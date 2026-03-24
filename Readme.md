### To run
`python lincode.py`

### Algo
1. Finding the bad rows:
   1. Find the `X`'s rank by Gauss elimination.
   1. Find `bad_rows`: removing such row will decrease `X`'s rank by 1.
1. Find C:
   1. Find the basis matrix `B`: Perform Gauss elimination (good rows only).
   1. Calculate the basis for `B @ C.T = 0` system solutions.
1. Fix bad rows:
   1. Precompute syndrome dictionary for small error vectors.
   1. Compute syndromes of `bad_rows`.
   1. Lookup dictionary & find corresponding `errors`.
   1. XOR the `bad_rows` with corresponding `errors`.
1. Check the result: `C @ X_fixed.T = 0`

### Results
See `log.txt`
