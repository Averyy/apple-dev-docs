# simd_matrix4x4(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified quarternion.

## Declaration

```swift
func simd_matrix4x4(_ q: simd_quatf) -> simd_float4x4
```

```c
static simd_float4x4 simd_matrix4x4(simd_quatf q);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_float4, simd_float4, simd_float4, simd_float4) -> simd_float4x4](./simd_matrix%28_,_,_,_%29-4p5ox.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float4, simd_float4, simd_float4, simd_float4) -> simd_float4x4](./simd_matrix_from_rows%28_,_,_,_%29-34hac.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float4x4](./matrix_from_rows%28_,_,_,_%29-18jb3.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix4x4(_:)-20lv7)*