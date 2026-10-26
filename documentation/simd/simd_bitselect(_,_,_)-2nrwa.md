# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_char2, _ y: simd_char2, _ mask: simd_char2) -> simd_char2
```

```c
static simd_char2 simd_bitselect(simd_char2 x, simd_char2 y, simd_char2 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_char2) -> simd_bool](./simd_any%28_%29-64och.md)
- [func simd_all(simd_char2) -> simd_bool](./simd_all%28_%29-1d0nz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-2nrwa)*