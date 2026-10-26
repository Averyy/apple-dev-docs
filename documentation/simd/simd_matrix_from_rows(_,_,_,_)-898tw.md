# simd_matrix_from_rows(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_double4, _ row1: simd_double4, _ row2: simd_double4, _ row3: simd_double4) -> simd_double4x4
```

```c
static simd_double4x4 simd_matrix_from_rows(simd_double4 row0, simd_double4 row1, simd_double4 row2, simd_double4 row3);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_double4, simd_double4, simd_double4, simd_double4) -> simd_double4x4](./simd_matrix%28_,_,_,_%29-28at0.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_rows(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>, SIMD4<Double>) -> simd_double4x4](./matrix_from_rows%28_,_,_,_%29-37t0w.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix4x4(simd_quatd) -> simd_double4x4](./simd_matrix4x4%28_%29-20mdz.md)
  Returns a new matrix with the specified quarternion.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2kzr8.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:_:_:)-898tw)*