# simd_matrix_from_rows(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_double3, _ row1: simd_double3, _ row2: simd_double3) -> simd_double3x3
```

```c
static simd_double3x3 simd_matrix_from_rows(simd_double3 row0, simd_double3 row1, simd_double3 row2);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_double3, simd_double3, simd_double3) -> simd_double3x3](./simd_matrix%28_,_,_%29-5h0nl.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_rows(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>) -> simd_double3x3](./matrix_from_rows%28_,_,_%29-7a60t.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix3x3(simd_quatd) -> simd_double3x3](./simd_matrix3x3%28_%29-60dhx.md)
  Returns a new matrix with the specified quarternion.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2nuo5.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:_:)-48v9h)*