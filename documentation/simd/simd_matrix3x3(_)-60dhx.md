# simd_matrix3x3(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified quarternion.

## Declaration

```swift
func simd_matrix3x3(_ q: simd_quatd) -> simd_double3x3
```

```c
static simd_double3x3 simd_matrix3x3(simd_quatd q);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_double3, simd_double3, simd_double3) -> simd_double3x3](./simd_matrix%28_,_,_%29-5h0nl.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double3, simd_double3, simd_double3) -> simd_double3x3](./simd_matrix_from_rows%28_,_,_%29-48v9h.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>) -> simd_double3x3](./matrix_from_rows%28_,_,_%29-7a60t.md)
  Returns a new matrix with the specified rows.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2nuo5.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix3x3(_:)-60dhx)*