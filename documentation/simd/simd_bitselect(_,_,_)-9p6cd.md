# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ushort2, _ y: simd_ushort2, _ mask: simd_short2) -> simd_ushort2
```

```c
static simd_ushort2 simd_bitselect(simd_ushort2 x, simd_ushort2 y, simd_short2 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ushort2) -> simd_bool](./simd_any%28_%29-649i9.md)
- [func simd_all(simd_ushort2) -> simd_bool](./simd_all%28_%29-1dffj.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-9p6cd)*