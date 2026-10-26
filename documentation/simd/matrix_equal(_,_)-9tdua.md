# matrix_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: ==)

## Declaration

```swift
func matrix_equal(_ lhs: simd_double3x3, _ rhs: simd_double3x3) -> Bool
```

## See Also

### Deprecated Symbols
- [func matrix_invert(simd_double3x3) -> simd_double3x3](./matrix_invert%28_%29-2lv98.md)
  Returns the inverse of the specified matrix.
- [func matrix_from_columns(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>) -> simd_double3x3](./matrix_from_columns%28_,_,_%29-4bc62.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_diagonal(SIMD3<Double>) -> simd_double3x3](./matrix_from_diagonal%28_%29-3jtgg.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_double3x3) -> Double](./matrix_determinant%28_%29-4bxkm.md)
  Returns the determinant of the specified matrix.
- [func matrix_transpose(simd_double3x3) -> double3x3](./matrix_transpose%28_%29-3ectl.md)
  Returns the transpose of a matrix.
- [init(simd_double3x3)](./simd_double3x3/init%28_%29-2o4jh.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double3x3](./simd_double3x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_equal(_:_:)-9tdua)*