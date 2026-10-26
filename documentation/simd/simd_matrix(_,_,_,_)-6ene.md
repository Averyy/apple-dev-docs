# simd_matrix(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_half3, _ col1: simd_half3, _ col2: simd_half3, _ col3: simd_half3) -> simd_half4x3
```

```c
static simd_half4x3 simd_matrix(simd_half3 col0, simd_half3 col1, simd_half3 col2, simd_half3 col3);
```

## See Also

### Matrix creation functions
- [func simd_matrix_from_rows(simd_half4, simd_half4, simd_half4) -> simd_half4x3](./simd_matrix_from_rows%28_,_,_%29-7bb0v.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:_:)-6ene)*