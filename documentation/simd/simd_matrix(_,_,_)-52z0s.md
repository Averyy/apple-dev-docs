# simd_matrix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_float3, _ col1: simd_float3, _ col2: simd_float3) -> simd_float3x3
```

```c
static simd_float3x3 simd_matrix(simd_float3 col0, simd_float3 col1, simd_float3 col2);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_float3, simd_float3, simd_float3) -> simd_float3x3](./simd_matrix_from_rows%28_,_,_%29-1tn2x.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float3x3](./matrix_from_rows%28_,_,_%29-15v2l.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix3x3(simd_quatf) -> simd_float3x3](./simd_matrix3x3%28_%29-60cx9.md)
  Returns a new matrix with the specified quarternion.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2nvn1.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:)-52z0s)*