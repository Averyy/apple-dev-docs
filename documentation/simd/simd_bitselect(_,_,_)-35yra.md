# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_uint16, _ y: simd_uint16, _ mask: simd_int16) -> simd_uint16
```

```c
static simd_uint16 simd_bitselect(simd_uint16 x, simd_uint16 y, simd_int16 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_uint16) -> simd_bool](./simd_any%28_%29-931x2.md)
- [func simd_all(simd_uint16) -> simd_bool](./simd_all%28_%29-inj8.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-35yra)*