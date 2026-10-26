# simd_matrix3x3(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified quarternion.

## Declaration

```swift
func simd_matrix3x3(_ q: simd_quatf) -> simd_float3x3
```

```c
static simd_float3x3 simd_matrix3x3(simd_quatf q);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_float3, simd_float3, simd_float3) -> simd_float3x3](./simd_matrix%28_,_,_%29-52z0s.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_float3, simd_float3, simd_float3) -> simd_float3x3](./simd_matrix_from_rows%28_,_,_%29-1tn2x.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float3x3](./matrix_from_rows%28_,_,_%29-15v2l.md)
  Returns a new matrix with the specified rows.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2nvn1.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix3x3(_:)-60cx9)*