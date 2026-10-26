# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_uchar16, _ y: simd_uchar16, _ mask: simd_char16) -> simd_uchar16
```

```c
static simd_uchar16 simd_bitselect(simd_uchar16 x, simd_uchar16 y, simd_char16 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_uchar16) -> simd_bool](./simd_any%28_%29-933sa.md)
- [func simd_all(simd_uchar16) -> simd_bool](./simd_all%28_%29-ikbg.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-9i5ku)*