# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_char3, _ y: simd_char3, _ mask: simd_char3) -> simd_char3
```

```c
static simd_char3 simd_bitselect(simd_char3 x, simd_char3 y, simd_char3 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_char3) -> simd_bool](./simd_any%28_%29-69a7c.md)
- [func simd_all(simd_char3) -> simd_bool](./simd_all%28_%29-1aml2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-4kbjh)*