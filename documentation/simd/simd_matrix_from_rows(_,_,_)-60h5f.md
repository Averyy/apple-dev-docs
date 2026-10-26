# simd_matrix_from_rows(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_half3, _ row1: simd_half3, _ row2: simd_half3) -> simd_half3x3
```

```c
static simd_half3x3 simd_matrix_from_rows(simd_half3 row0, simd_half3 row1, simd_half3 row2);
```

## See Also

### Matrix creation functions
- [func simd_matrix(simd_half3, simd_half3, simd_half3) -> simd_half3x3](./simd_matrix%28_,_,_%29-2bbz7.md)
  Returns a new matrix with the specified columns.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2nygl.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:_:)-60h5f)*