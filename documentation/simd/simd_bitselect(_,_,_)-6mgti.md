# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ushort32, _ y: simd_ushort32, _ mask: simd_short32) -> simd_ushort32
```

```c
static simd_ushort32 simd_bitselect(simd_ushort32 x, simd_ushort32 y, simd_short32 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ushort32) -> simd_bool](./simd_any%28_%29-3au8l.md)
- [func simd_all(simd_ushort32) -> simd_bool](./simd_all%28_%29-1kmnn.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-6mgti)*