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
var cmatrix: simd_float3x2 { get }
```

## See Also

### Deprecated Symbols
- [func matrix_from_columns(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>) -> simd_float3x2](../matrix_from_columns%28_,_,_%29-6ua0c.md)
  Returns a new matrix with the specified columns.
- [func matrix_equal(simd_float3x2, simd_float3x2) -> Bool](../matrix_equal%28_,_%29-1kgro.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float3x2) -> float2x3](../matrix_transpose%28_%29-92iqd.md)
  Returns the transpose of a matrix.
- [init(simd_float3x2)](./init%28_%29-323m3.md)
  Creates a new matrix with the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float3x2/cmatrix)*