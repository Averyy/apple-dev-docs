# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_short16, _ y: simd_short16, _ mask: simd_short16) -> simd_short16
```

```c
static simd_short16 simd_bitselect(simd_short16 x, simd_short16 y, simd_short16 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_short16) -> simd_bool](./simd_any%28_%29-92yq2.md)
- [func simd_all(simd_short16) -> simd_bool](./simd_all%28_%29-i5jw.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-3vpt5)*