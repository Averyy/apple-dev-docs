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
var cmatrix: simd_float3x4 { get }
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_float3x4, simd_float3x4) -> Bool](../matrix_equal%28_,_%29-6el88.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float3x4](../matrix_from_columns%28_,_,_%29-5nhl4.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float4x3) -> float3x4](../matrix_transpose%28_%29-6ygo1.md)
  Returns the transpose of a matrix.
- [init(simd_float3x4)](./init%28_%29-8fk31.md)
  Creates a new matrix with the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float3x4/cmatrix)*