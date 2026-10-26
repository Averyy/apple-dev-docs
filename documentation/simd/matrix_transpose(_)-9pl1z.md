# matrix_transpose(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the transpose of a matrix.

**Availability**:
- Swift - Deprecated in 4.0

> **Deprecated**: Use the .transpose property instead.

## Declaration

```swift
func matrix_transpose(_ x: simd_float3x3) -> float3x3
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
- [func matrix_from_columns(SIMD3<Float>, SIMD3<Float>, SIMD3<Float>) -> simd_float3x3](./matrix_from_columns%28_,_,_%29-4c7qb.md)
  Returns a new matrix with the specified columns.
- [init(simd_float3x3)](./simd_float3x3/init%28_%29-7ymye.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float3x3](./simd_float3x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_transpose(_:)-9pl1z)*