# simd_matrix_from_rows(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_float2, _ row1: simd_float2, _ row2: simd_float2) -> simd_float2x3
```

```c
static simd_float2x3 simd_matrix_from_rows(simd_float2 row0, simd_float2 row1, simd_float2 row2);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_float3, simd_float3) -> simd_float2x3](./simd_matrix%28_,_%29-7qavs.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_rows(SIMD2<Float>, SIMD2<Float>, SIMD2<Float>) -> simd_float2x3](./matrix_from_rows%28_,_,_%29-m0hw.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:_:)-9kksc)*