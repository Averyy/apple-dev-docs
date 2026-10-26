# matrix_from_columns(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_double4x4)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD4<Double>, _ col1: SIMD4<Double>, _ col2: SIMD4<Double>, _ col3: SIMD4<Double>) -> simd_double4x4
```

## See Also

### Deprecated Symbols
- [func matrix_invert(simd_double4x4) -> simd_double4x4](./matrix_invert%28_%29-84fxh.md)
  Returns the inverse of the specified matrix.
- [func matrix_from_diagonal(SIMD4<Double>) -> simd_double4x4](./matrix_from_diagonal%28_%29-2r6tr.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_double4x4) -> Double](./matrix_determinant%28_%29-2n34p.md)
  Returns the determinant of the specified matrix.
- [func matrix_equal(simd_double4x4, simd_double4x4) -> Bool](./matrix_equal%28_,_%29-3jmfe.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double4x4) -> double4x4](./matrix_transpose%28_%29-66ecl.md)
  Returns the transpose of a matrix.
- [init(simd_double4x4)](./simd_double4x4/init%28_%29-4fie3.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double4x4](./simd_double4x4/cmatrix.md)
  Creates a new matrix with the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:_:_:)-61q4l)*