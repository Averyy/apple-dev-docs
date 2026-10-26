# simd_matrix_from_rows(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_float3, _ row1: simd_float3, _ row2: simd_float3, _ row3: simd_float3) -> simd_float3x4
```

```c
static simd_float3x4 simd_matrix_from_rows(simd_float3 row0, simd_float3 row1, simd_float3 row2, simd_float3 row3);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_float4, simd_float4, simd_float4) -> simd_float3x4](./simd_matrix%28_,_,_%29-1vwb0.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_rows(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float3x4](./matrix_from_rows%28_,_,_,_%29-4bn2a.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:_:_:)-6irzy)*