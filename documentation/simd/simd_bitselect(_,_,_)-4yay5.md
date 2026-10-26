# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ushort8, _ y: simd_ushort8, _ mask: simd_short8) -> simd_ushort8
```

```c
static simd_ushort8 simd_bitselect(simd_ushort8 x, simd_ushort8 y, simd_short8 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ushort8) -> simd_bool](./simd_any%28_%29-6pgp3.md)
- [func simd_all(simd_ushort8) -> simd_bool](./simd_all%28_%29-1yk7d.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-4yay5)*