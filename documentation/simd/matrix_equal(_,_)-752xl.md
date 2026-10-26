# matrix_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: ==)

## Declaration

```swift
func matrix_equal(_ lhs: simd_float4x4, _ rhs: simd_float4x4) -> Bool
```

## See Also

### Deprecated Symbols
- [func matrix_invert(simd_float4x4) -> simd_float4x4](./matrix_invert%28_%29-7fevy.md)
  Returns the inverse of the specified matrix.
- [func matrix_from_diagonal(SIMD4<Float>) -> simd_float4x4](./matrix_from_diagonal%28_%29-71pds.md)
  Returns a new matrix with the specified vector on the main diagonal.
- [func matrix_determinant(simd_float4x4) -> Float](./matrix_determinant%28_%29-4yqoy.md)
  Returns the determinant of the specified matrix.
- [func matrix_from_columns(SIMD4<Float>, SIMD4<Float>, SIMD4<Float>, SIMD4<Float>) -> simd_float4x4](./matrix_from_columns%28_,_,_,_%29-5d0yw.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_float4x4) -> float4x4](./matrix_transpose%28_%29-8t44c.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_float4x4](./simd_float4x4/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
- [init(simd_float4x4)](./simd_float4x4/init%28_%29-2ga0f.md)
  Creates a new matrix with the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_equal(_:_:)-752xl)*