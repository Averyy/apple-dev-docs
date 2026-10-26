# matrix_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: ==)

## Declaration

```swift
func matrix_equal(_ lhs: simd_float3x4, _ rhs: simd_float3x4) -> Bool
```

## See Also

### Deprecated Symbols
- [func matrix_from_columns(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float3x4](./matrix_from_columns%28_,_,_%29-5nhl4.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float4x3) -> float3x4](./matrix_transpose%28_%29-6ygo1.md)
  Returns the transpose of a matrix.
- [init(simd_float3x4)](./simd_float3x4/init%28_%29-8fk31.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float3x4](./simd_float3x4/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_equal(_:_:)-6el88)*