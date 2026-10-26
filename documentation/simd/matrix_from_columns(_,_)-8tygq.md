# matrix_from_columns(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_float2x3)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD3<Float>, _ col1: SIMD3<Float>) -> simd_float2x3
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_float2x3, simd_float2x3) -> Bool](./matrix_equal%28_,_%29-he2l.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float2x3) -> float3x2](./matrix_transpose%28_%29-71xii.md)
  Returns the transpose of a matrix.
- [init(simd_float2x3)](./simd_float2x3/init%28_%29-55t2w.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_float2x3](./simd_float2x3/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:)-8tygq)*