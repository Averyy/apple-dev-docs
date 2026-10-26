# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_short2, _ y: simd_short2, _ mask: simd_short2) -> simd_short2
```

```c
static simd_short2 simd_bitselect(simd_short2 x, simd_short2 y, simd_short2 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_short2) -> simd_bool](./simd_any%28_%29-64jj5.md)
- [func simd_all(simd_short2) -> simd_bool](./simd_all%28_%29-1d5nj.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-625jo)*