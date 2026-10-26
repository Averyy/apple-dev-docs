# matrix_invert(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the inverse of the specified matrix.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 10.0+
- watchOS 3.0+
- Swift - Deprecated in 4.0

> **Deprecated**: Use the .inverse property instead.

## Declaration

```swift
func matrix_invert(_ x: simd_double4x4) -> simd_double4x4
```

## See Also

### Deprecated Symbols
- [func matrix_from_columns(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>, SIMD4<Double>) -> simd_double4x4](./matrix_from_columns%28_,_,_,_%29-61q4l.md)
  Returns a new matrix with the specified columns.
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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_invert(_:)-84fxh)*