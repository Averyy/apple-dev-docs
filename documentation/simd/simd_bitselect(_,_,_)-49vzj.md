# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_uchar32, _ y: simd_uchar32, _ mask: simd_char32) -> simd_uchar32
```

```c
static simd_uchar32 simd_bitselect(simd_uchar32 x, simd_uchar32 y, simd_char32 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_uchar32) -> simd_bool](./simd_any%28_%29-3apcl.md)
- [func simd_all(simd_uchar32) -> simd_bool](./simd_all%28_%29-1khgz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-49vzj)*