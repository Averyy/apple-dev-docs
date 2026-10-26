# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_uchar2, _ y: simd_uchar2, _ mask: simd_char2) -> simd_uchar2
```

```c
static simd_uchar2 simd_bitselect(simd_uchar2 x, simd_uchar2 y, simd_char2 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_uchar2) -> simd_bool](./simd_any%28_%29-64ekh.md)
- [func simd_all(simd_uchar2) -> simd_bool](./simd_all%28_%29-1dafz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-2yxn9)*