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
var cmatrix: simd_float4x3 { get }
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_float4x3, simd_float4x3) -> Bool](../matrix_equal%28_,_%29-2m44x.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_from_columns(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float4x3](../matrix_from_columns%28_,_,_,_%29-7tq9m.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float3x4) -> float4x3](../matrix_transpose%28_%29-2oa75.md)
  Returns the transpose of a matrix.
- [init(simd_float4x3)](./init%28_%29-6f0m9.md)
  Creates a new matrix with the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float4x3/cmatrix)*