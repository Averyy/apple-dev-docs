# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_uchar8, _ y: simd_uchar8, _ mask: simd_char8) -> simd_uchar8
```

```c
static simd_uchar8 simd_bitselect(simd_uchar8 x, simd_uchar8 y, simd_char8 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_uchar8) -> simd_bool](./simd_any%28_%29-6pbmv.md)
- [func simd_all(simd_uchar8) -> simd_bool](./simd_all%28_%29-1yp2h.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-9gyx6)*