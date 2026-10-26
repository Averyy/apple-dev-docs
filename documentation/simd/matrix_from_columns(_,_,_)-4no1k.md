# matrix_from_columns(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_double3x4)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD4<Double>, _ col1: SIMD4<Double>, _ col2: SIMD4<Double>) -> simd_double3x4
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_double3x4, simd_double3x4) -> Bool](./matrix_equal%28_,_%29-4qog1.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double4x3) -> double3x4](./matrix_transpose%28_%29-8am0o.md)
  Returns the transpose of a matrix.
- [init(simd_double3x4)](./simd_double3x4/init%28_%29-2qvpe.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double3x4](./simd_double3x4/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:_:)-4no1k)*