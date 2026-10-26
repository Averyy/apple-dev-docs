# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_uchar4, _ y: simd_uchar4, _ mask: simd_char4) -> simd_uchar4
```

```c
static simd_uchar4 simd_bitselect(simd_uchar4 x, simd_uchar4 y, simd_char4 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_uchar4) -> simd_bool](./simd_any%28_%29-6d22b.md)
- [func simd_all(simd_uchar4) -> simd_bool](./simd_all%28_%29-1jo4t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-46k0t)*