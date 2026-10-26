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
var cmatrix: simd_double4x3 { get }
```

## See Also

### Deprecated Symbols
- [func matrix_from_columns(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>, SIMD3<Double>) -> simd_double4x3](../matrix_from_columns%28_,_,_,_%29-7g6mu.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_double4x3, simd_double4x3) -> Bool](../matrix_equal%28_,_%29-1x3ox.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double3x4) -> double4x3](../matrix_transpose%28_%29-23ibz.md)
  Returns the transpose of a matrix.
- [init(simd_double4x3)](./init%28_%29-30jps.md)
  Creates a new matrix with the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double4x3/cmatrix)*