# matrix_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: ==)

## Declaration

```swift
func matrix_equal(_ lhs: simd_float2x2, _ rhs: simd_float2x2) -> Bool
```

## See Also

### Deprecated Symbols
- [func matrix_invert(simd_float2x2) -> simd_float2x2](./matrix_invert%28_%29-94e37.md)
  Returns the inverse of the specified matrix.
- [func matrix_transpose(simd_float2x2) -> float2x2](./matrix_transpose%28_%29-77v7g.md)
  Returns the transpose of a matrix.
- [func matrix_from_diagonal(SIMD2<Float>) -> simd_float2x2](./matrix_from_diagonal%28_%29-1v0zl.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_from_columns(SIMD2<Float>, SIMD2<Float>) -> simd_float2x2](./matrix_from_columns%28_,_%29-5urmx.md)
  Returns a new matrix with the specified columns.
- [func matrix_determinant(simd_float2x2) -> Float](./matrix_determinant%28_%29-30k4n.md)
  Returns the determinant of the specified matrix.
- [init(simd_float2x2)](./simd_float2x2/init%28_%29-uyy7.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float2x2](./simd_float2x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_equal(_:_:)-88hz9)*