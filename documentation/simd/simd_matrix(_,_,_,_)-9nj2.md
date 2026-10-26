# simd_matrix(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_half2, _ col1: simd_half2, _ col2: simd_half2, _ col3: simd_half2) -> simd_half4x2
```

```c
static simd_half4x2 simd_matrix(simd_half2 col0, simd_half2 col1, simd_half2 col2, simd_half2 col3);
```

## See Also

### Matrix creation functions
- [func simd_matrix_from_rows(simd_half4, simd_half4) -> simd_half4x2](./simd_matrix_from_rows%28_,_%29-74k.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:_:)-9nj2)*