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
init(_ cmatrix: simd_float3x2)
```

## See Also

### Deprecated Symbols
- [func matrix_from_columns(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>) -> simd_float3x2](../matrix_from_columns%28_,_,_%29-6ua0c.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_float3x2, simd_float3x2) -> Bool](../matrix_equal%28_,_%29-1kgro.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float3x2) -> float2x3](../matrix_transpose%28_%29-92iqd.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_float3x2](./cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float3x2/init(_:)-323m3)*