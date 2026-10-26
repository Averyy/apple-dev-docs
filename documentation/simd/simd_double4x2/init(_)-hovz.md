# init(_:)

**Framework**: simd  
**Kind**: init  
**Role**: Initializer

Creates a new matrix with the specified matrix.

**Availability**:
- Swift - Deprecated in 4.0

> **Deprecated**: This conversion is no longer necessary; use `cmatrix` directly.

## Declaration

```swift
init(_ cmatrix: simd_double4x2)
```

## See Also

### Deprecated Symbols
- [func matrix_from_columns(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>, SIMD2<Double>) -> simd_double4x2](../matrix_from_columns%28_,_,_,_%29-6tb78.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_double4x2, simd_double4x2) -> Bool](../matrix_equal%28_,_%29-5v8g0.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_double2x4) -> double4x2](../matrix_transpose%28_%29-7ttoe.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_double4x2](./cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double4x2/init(_:)-hovz)*