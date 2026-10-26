# matrix_from_columns(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_float2x4)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD4<Float>, _ col1: SIMD4<Float>) -> simd_float2x4
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_float2x4, simd_float2x4) -> Bool](./matrix_equal%28_,_%29-34fuu.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float4x2) -> float2x4](./matrix_transpose%28_%29-5ymlr.md)
  Returns the transpose of a matrix.
- [init(simd_float2x4)](./simd_float2x4/init%28_%29-3teag.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float2x4](./simd_float2x4/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:)-6tvfl)*