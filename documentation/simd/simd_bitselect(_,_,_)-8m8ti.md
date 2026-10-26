# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_short3, _ y: simd_short3, _ mask: simd_short3) -> simd_short3
```

```c
static simd_short3 simd_bitselect(simd_short3 x, simd_short3 y, simd_short3 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_short3) -> simd_bool](./simd_any%28_%29-69f7s.md)
- [func simd_all(simd_short3) -> simd_bool](./simd_all%28_%29-1ahau.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-8m8ti)*