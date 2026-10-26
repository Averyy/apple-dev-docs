# matrix_from_columns(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_float2x2)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD2<Float>, _ col1: SIMD2<Float>) -> simd_float2x2
```

## See Also

### Deprecated Symbols
- [func matrix_invert(simd_float2x2) -> simd_float2x2](./matrix_invert%28_%29-94e37.md)
  Returns the inverse of the specified matrix.
- [func matrix_transpose(simd_float2x2) -> float2x2](./matrix_transpose%28_%29-77v7g.md)
  Returns the transpose of a matrix.
- [func matrix_from_diagonal(SIMD2<Float>) -> simd_float2x2](./matrix_from_diagonal%28_%29-1v0zl.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_float2x2) -> Float](./matrix_determinant%28_%29-30k4n.md)
  Returns the determinant of the specified matrix.
- [func matrix_equal(simd_float2x2, simd_float2x2) -> Bool](./matrix_equal%28_,_%29-88hz9.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [init(simd_float2x2)](./simd_float2x2/init%28_%29-uyy7.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float2x2](./simd_float2x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:)-5urmx)*