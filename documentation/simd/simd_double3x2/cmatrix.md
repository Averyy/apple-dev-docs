# cmatrix

**Framework**: simd  
**Kind**: property  
**Role**: Instance Property

Returns the matrix as the corresponding C matrix type.

**Availability**:
- Swift - Deprecated in 4.0

> **Deprecated**: This property is no longer needed; use the matrix itself.

## Declaration

```swift
var cmatrix: simd_double3x2 { get }
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_double3x2, simd_double3x2) -> Bool](../matrix_equal%28_,_%29-3dnu.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>) -> simd_double3x2](../matrix_from_columns%28_,_,_%29-9wapk.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_double2x3) -> double3x2](../matrix_transpose%28_%29-7ueg2.md)
  Returns the transpose of a matrix.
- [init(simd_double3x2)](./init%28_%29-6yyfq.md)
  Creates a new matrix with the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double3x2/cmatrix)*