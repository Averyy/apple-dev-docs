# simd_matrix_from_rows(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_half4, _ row1: simd_half4, _ row2: simd_half4, _ row3: simd_half4) -> simd_half4x4
```

```c
static simd_half4x4 simd_matrix_from_rows(simd_half4 row0, simd_half4 row1, simd_half4 row2, simd_half4 row3);
```

## See Also

### Matrix creation functions
- [func simd_matrix(simd_half4, simd_half4, simd_half4, simd_half4) -> simd_half4x4](./simd_matrix%28_,_,_,_%29-7ltt0.md)
  Returns a new matrix with the specified columns.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2l1as.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:_:_:)-31gpp)*