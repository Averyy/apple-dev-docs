# matrix_from_columns(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_double2x3)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD3<Double>, _ col1: SIMD3<Double>) -> simd_double2x3
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_double2x3, simd_double2x3) -> Bool](./matrix_equal%28_,_%29-52vds.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double3x2) -> double2x3](./matrix_transpose%28_%29-97k0o.md)
  Returns the transpose of a matrix.
- [init(simd_double2x3)](./simd_double2x3/init%28_%29-98rcw.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double2x3](./simd_double2x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:)-61w2n)*