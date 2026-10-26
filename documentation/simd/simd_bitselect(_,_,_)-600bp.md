# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_ulong3, _ y: simd_ulong3, _ mask: simd_long3) -> simd_ulong3
```

```c
static simd_ulong3 simd_bitselect(simd_ulong3 x, simd_ulong3 y, simd_long3 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_ulong3) -> simd_bool](./simd_any%28_%29-69ij0.md)
- [func simd_all(simd_ulong3) -> simd_bool](./simd_all%28_%29-1adyq.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-600bp)*