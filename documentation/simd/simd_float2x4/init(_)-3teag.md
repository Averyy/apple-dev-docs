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
init(_ cmatrix: simd_float2x4)
```

## See Also

### Deprecated Symbols
- [func matrix_from_columns(SIMD4<Float>, SIMD4<Float>) -> simd_float2x4](../matrix_from_columns%28_,_%29-6tvfl.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_float2x4, simd_float2x4) -> Bool](../matrix_equal%28_,_%29-34fuu.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float4x2) -> float2x4](../matrix_transpose%28_%29-5ymlr.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_float2x4](./cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float2x4/init(_:)-3teag)*