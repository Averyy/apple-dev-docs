# simd_matrix_from_rows(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_float2, _ row1: simd_float2) -> simd_float2x2
```

```c
static simd_float2x2 simd_matrix_from_rows(simd_float2 row0, simd_float2 row1);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_float2, simd_float2) -> simd_float2x2](./simd_matrix%28_,_%29-1ftcm.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_rows(SIMD2<Float>, SIMD2<Float>) -> simd_float2x2](./matrix_from_rows%28_,_%29-2pi8i.md)
  Returns a new matrix with the specified rows.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2rboq.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:)-3mqrr)*