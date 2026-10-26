# simd_matrix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_float4, _ col1: simd_float4, _ col2: simd_float4) -> simd_float3x4
```

```c
static simd_float3x4 simd_matrix(simd_float4 col0, simd_float4 col1, simd_float4 col2);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_float3, simd_float3, simd_float3, simd_float3) -> simd_float3x4](./simd_matrix_from_rows%28_,_,_,_%29-6irzy.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float3x4](./matrix_from_rows%28_,_,_,_%29-4bn2a.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:)-1vwb0)*