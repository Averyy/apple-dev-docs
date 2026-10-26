# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ushort16, _ y: simd_ushort16, _ mask: simd_short16) -> simd_ushort16
```

```c
static simd_ushort16 simd_bitselect(simd_ushort16 x, simd_ushort16 y, simd_short16 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ushort16) -> simd_bool](./simd_any%28_%29-938p6.md)
- [func simd_all(simd_ushort16) -> simd_bool](./simd_all%28_%29-iffg.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-144l9)*