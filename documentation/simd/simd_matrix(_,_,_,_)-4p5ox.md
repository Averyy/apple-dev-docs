# simd_matrix(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_float4, _ col1: simd_float4, _ col2: simd_float4, _ col3: simd_float4) -> simd_float4x4
```

```c
static simd_float4x4 simd_matrix(simd_float4 col0, simd_float4 col1, simd_float4 col2, simd_float4 col3);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_float4, simd_float4, simd_float4, simd_float4) -> simd_float4x4](./simd_matrix_from_rows%28_,_,_,_%29-34hac.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float4x4](./matrix_from_rows%28_,_,_,_%29-18jb3.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix4x4(simd_quatf) -> simd_float4x4](./simd_matrix4x4%28_%29-20lv7.md)
  Returns a new matrix with the specified quarternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:_:)-4p5ox)*