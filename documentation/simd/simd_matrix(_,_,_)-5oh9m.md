# simd_matrix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_half4, _ col1: simd_half4, _ col2: simd_half4) -> simd_half3x4
```

```c
static simd_half3x4 simd_matrix(simd_half4 col0, simd_half4 col1, simd_half4 col2);
```

## See Also

### Matrix creation functions
- [func simd_matrix_from_rows(simd_half3, simd_half3, simd_half3, simd_half3) -> simd_half3x4](./simd_matrix_from_rows%28_,_,_,_%29-9v9ky.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:)-5oh9m)*