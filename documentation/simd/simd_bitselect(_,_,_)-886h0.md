# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ulong2, _ y: simd_ulong2, _ mask: simd_long2) -> simd_ulong2
```

```c
static simd_ulong2 simd_bitselect(simd_ulong2 x, simd_ulong2 y, simd_long2 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ulong2) -> simd_bool](./simd_any%28_%29-64g1r.md)
- [func simd_all(simd_ulong2) -> simd_bool](./simd_all%28_%29-1d8u9.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-886h0)*