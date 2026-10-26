# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ushort4, _ y: simd_ushort4, _ mask: simd_short4) -> simd_ushort4
```

```c
static simd_ushort4 simd_bitselect(simd_ushort4 x, simd_ushort4 y, simd_short4 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ushort4) -> simd_bool](./simd_any%28_%29-6cx6b.md)
- [func simd_all(simd_ushort4) -> simd_bool](./simd_all%28_%29-1jswd.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-ryof)*