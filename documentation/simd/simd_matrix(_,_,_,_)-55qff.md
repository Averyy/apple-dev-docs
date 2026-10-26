# simd_matrix(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_float3, _ col1: simd_float3, _ col2: simd_float3, _ col3: simd_float3) -> simd_float4x3
```

```c
static simd_float4x3 simd_matrix(simd_float3 col0, simd_float3 col1, simd_float3 col2, simd_float3 col3);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_float4, simd_float4, simd_float4) -> simd_float4x3](./simd_matrix_from_rows%28_,_,_%29-81rfz.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float4x3](./matrix_from_rows%28_,_,_%29-ld0y.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:_:)-55qff)*