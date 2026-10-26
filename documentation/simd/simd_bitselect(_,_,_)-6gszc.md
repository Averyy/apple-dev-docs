# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ulong4, _ y: simd_ulong4, _ mask: simd_long4) -> simd_ulong4
```

```c
static simd_ulong4 simd_bitselect(simd_ulong4 x, simd_ulong4 y, simd_long4 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ulong4) -> simd_bool](./simd_any%28_%29-6cxel.md)
- [func simd_all(simd_ulong4) -> simd_bool](./simd_all%28_%29-1jlbv.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-6gszc)*