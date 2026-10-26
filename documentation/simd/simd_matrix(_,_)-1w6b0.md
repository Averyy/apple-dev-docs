# simd_matrix(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_half2, _ col1: simd_half2) -> simd_half2x2
```

```c
static simd_half2x2 simd_matrix(simd_half2 col0, simd_half2 col1);
```

## See Also

### Matrix creation functions
- [func simd_matrix_from_rows(simd_half2, simd_half2) -> simd_half2x2](./simd_matrix_from_rows%28_,_%29-9lrpr.md)
  Returns a new matrix with the specified rows.
- [simd_diagonal_matrix](./simd_diagonal_matrix-2rg1i.md)
  Returns a new matrix with the specified vector on the main diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:)-1w6b0)*