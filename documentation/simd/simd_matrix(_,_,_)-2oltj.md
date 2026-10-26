# simd_matrix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_float2, _ col1: simd_float2, _ col2: simd_float2) -> simd_float3x2
```

```c
static simd_float3x2 simd_matrix(simd_float2 col0, simd_float2 col1, simd_float2 col2);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_float3, simd_float3) -> simd_float3x2](./simd_matrix_from_rows%28_,_%29-48bjr.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Float>, SIMD3<Float>) -> simd_float3x2](./matrix_from_rows%28_,_%29-47wrn.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:)-2oltj)*