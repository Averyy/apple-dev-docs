# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ushort3, _ y: simd_ushort3, _ mask: simd_short3) -> simd_ushort3
```

```c
static simd_ushort3 simd_bitselect(simd_ushort3 x, simd_ushort3 y, simd_short3 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ushort3) -> simd_bool](./simd_any%28_%29-69p6w.md)
- [func simd_all(simd_ushort3) -> simd_bool](./simd_all%28_%29-1a7fa.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-7yglw)*