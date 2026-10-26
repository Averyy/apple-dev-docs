# matrix_from_columns(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_double3x2)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD2<Double>, _ col1: SIMD2<Double>, _ col2: SIMD2<Double>) -> simd_double3x2
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_double3x2, simd_double3x2) -> Bool](./matrix_equal%28_,_%29-3dnu.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double2x3) -> double3x2](./matrix_transpose%28_%29-7ueg2.md)
  Returns the transpose of a matrix.
- [init(simd_double3x2)](./simd_double3x2/init%28_%29-6yyfq.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double3x2](./simd_double3x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:_:)-9wapk)*