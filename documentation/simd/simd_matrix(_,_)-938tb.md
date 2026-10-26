# simd_matrix(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_double2, _ col1: simd_double2) -> simd_double2x2
```

```c
static simd_double2x2 simd_matrix(simd_double2 col0, simd_double2 col1);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_double2, simd_double2) -> simd_double2x2](./simd_matrix_from_rows%28_,_%29-368td.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD2<Double>, SIMD2<Double>) -> simd_double2x2](./matrix_from_rows%28_,_%29-1w56v.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2rc7a.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:)-938tb)*