# matrix_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: ==)

## Declaration

```swift
func matrix_equal(_ lhs: simd_double3x2, _ rhs: simd_double3x2) -> Bool
```

## See Also

### Deprecated Symbols
- [func matrix_from_columns(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>) -> simd_double3x2](./matrix_from_columns%28_,_,_%29-9wapk.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_double2x3) -> double3x2](./matrix_transpose%28_%29-7ueg2.md)
  Returns the transpose of a matrix.
- [init(simd_double3x2)](./simd_double3x2/init%28_%29-6yyfq.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double3x2](./simd_double3x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_equal(_:_:)-3dnu)*