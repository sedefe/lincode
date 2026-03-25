## To run
`python lincode.py`

## Algo
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

## Results
See `log.txt`

## Issues
### Distances of X(4) and X(24)
Following triplets of `X`'s rows sum up to vectors with weight=**2**:
```
X(17) + X( 4) + X( 2) -> [0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0]
X(18) + X( 4) + X( 1) -> [0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0]
X(19) + X( 6) + X( 4) -> [0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0]
X(20) + X( 4) + X( 0) -> [0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0]
X(22) + X( 4) + X( 3) -> [0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0]
X(23) + X(12) + X( 4) -> [0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0]
X(24) + X( 8) + X( 0) -> [0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0]
X(24) + X(10) + X( 6) -> [0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0]
X(24) + X(14) + X( 2) -> [0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0]
X(24) + X(15) + X( 7) -> [0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0]
X(25) + X(10) + X( 4) -> [0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0]
X(26) + X( 9) + X( 4) -> [0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0]
X(26) + X(24) + X(22) -> [0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0]
X(27) + X(14) + X( 4) -> [0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0]
X(28) + X( 7) + X( 4) -> [0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0]
X(30) + X(24) + X(23) -> [0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0]
X(31) + X(11) + X( 4) -> [0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0]
X(31) + X(24) + X(18) -> [0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0]
```
Note: this only occur with X(4) or X(24), any other vector appears above at most twice.

That means, _any linear code containing X(4)/X(24) will have a minimal distance **2**_ and won't be able to fix even 1-bit error. Thus, X(4) and X(24) are the outliers.

### Distances of other vectors
On the other hand, following triplets sum up to vectors with weight=**4**:
```
X( 8) + X( 3) + X( 1) -> [1 0 0 1 0 1 1 0 0 0 0 0 0 0 0 0]
X(17) + X(11) + X( 5) -> [0 0 0 0 0 0 0 0 1 0 0 1 1 0 0 1]
X(18) + X(12) + X( 9) -> [0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0]
X(19) + X( 6) + X( 2) -> [0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 1]
X(20) + X(13) + X(10) -> [0 0 0 0 0 0 0 0 0 1 0 1 1 0 1 0]
X(21) + X(15) + X(14) -> [0 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1]
X(27) + X(26) + X(22) -> [0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 1]
X(30) + X(29) + X(28) -> [0 0 1 1 0 0 1 1 0 0 0 0 0 0 0 0]
```
That means, that _a linear code containing these vectors will have a minimal distance **4**_ and won't be able to fix 2-bit errors that vectors X(4) and X(24) have.
