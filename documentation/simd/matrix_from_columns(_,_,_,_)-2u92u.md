# matrix_from_columns(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_float4x2)

## Declaration

```swift
func matrix_from_columns(_ col0: SIMD2<Float>, _ col1: SIMD2<Float>, _ col2: SIMD2<Float>, _ col3: SIMD2<Float>) -> simd_float4x2
```

## See Also

### Deprecated Symbols
- [func matrix_equal(simd_float4x2, simd_float4x2) -> Bool](./matrix_equal%28_,_%29-1izln.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_transpose(simd_float2x4) -> float4x2](./matrix_transpose%28_%29-260wn.md)
  Returns the transpose of a matrix.
- [var cmatrix: simd_float4x2](./simd_float4x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.
- [init(simd_float4x2)](./simd_float4x2/init%28_%29-2e140.md)
  Creates a new matrix with the specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_columns(_:_:_:_:)-2u92u)*