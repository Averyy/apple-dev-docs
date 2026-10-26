# simd_matrix_from_rows(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_double2, _ row1: simd_double2) -> simd_double2x2
```

```c
static simd_double2x2 simd_matrix_from_rows(simd_double2 row0, simd_double2 row1);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_double2, simd_double2) -> simd_double2x2](./simd_matrix%28_,_%29-938tb.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_rows(SIMD2<Double>, SIMD2<Double>) -> simd_double2x2](./matrix_from_rows%28_,_%29-1w56v.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2rc7a.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:)-368td)*