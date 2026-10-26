# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_char8, _ y: simd_char8, _ mask: simd_char8) -> simd_char8
```

```c
static simd_char8 simd_bitselect(simd_char8 x, simd_char8 y, simd_char8 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_char8) -> simd_bool](./simd_any%28_%29-6plnr.md)
- [func simd_all(simd_char8) -> simd_bool](./simd_all%28_%29-1yyw9.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-5bgc3)*