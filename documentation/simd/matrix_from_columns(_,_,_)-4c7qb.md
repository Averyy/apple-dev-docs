# matrix_from_columns(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_float3x3)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD3<Float>, _ col1: SIMD3<Float>, _ col2: SIMD3<Float>) -> simd_float3x3
```

## See Also

### Deprecated Symbols
- [func matrix_invert(simd_float3x3) -> simd_float3x3](./matrix_invert%28_%29-15kif.md)
  Returns the inverse of the specified matrix.
- [func matrix_from_diagonal(SIMD3<Float>) -> simd_float3x3](./matrix_from_diagonal%28_%29-61643.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_float3x3) -> Float](./matrix_determinant%28_%29-2m4vm.md)
  Returns the determinant of the specified matrix.
- [func matrix_equal(simd_float3x3, simd_float3x3) -> Bool](./matrix_equal%28_,_%29-14gko.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float3x3) -> float3x3](./matrix_transpose%28_%29-9pl1z.md)
  Returns the transpose of a matrix.
- [init(simd_float3x3)](./simd_float3x3/init%28_%29-7ymye.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float3x3](./simd_float3x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:_:)-4c7qb)*