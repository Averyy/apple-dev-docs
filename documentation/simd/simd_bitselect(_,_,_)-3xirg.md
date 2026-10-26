# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ulong8, _ y: simd_ulong8, _ mask: simd_long8) -> simd_ulong8
```

```c
static simd_ulong8 simd_bitselect(simd_ulong8 x, simd_ulong8 y, simd_long8 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ulong8) -> simd_bool](./simd_any%28_%29-6p9gh.md)
- [func simd_all(simd_ulong8) -> simd_bool](./simd_all%28_%29-1yolz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-3xirg)*