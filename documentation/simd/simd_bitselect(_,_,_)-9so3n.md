# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_short32, _ y: simd_short32, _ mask: simd_short32) -> simd_short32
```

```c
static simd_short32 simd_bitselect(simd_short32 x, simd_short32 y, simd_short32 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_short32) -> simd_bool](./simd_any%28_%29-3b445.md)
- [func simd_all(simd_short32) -> simd_bool](./simd_all%28_%29-1kcj7.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-9so3n)*