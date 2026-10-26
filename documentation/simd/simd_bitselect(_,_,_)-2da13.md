# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_char32, _ y: simd_char32, _ mask: simd_char32) -> simd_char32
```

```c
static simd_char32 simd_bitselect(simd_char32 x, simd_char32 y, simd_char32 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_char32) -> simd_bool](./simd_any%28_%29-3az4l.md)
- [func simd_all(simd_char32) -> simd_bool](./simd_all%28_%29-1k7jn.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-2da13)*