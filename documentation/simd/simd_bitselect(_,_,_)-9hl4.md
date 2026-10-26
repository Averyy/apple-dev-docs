# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_long3, _ y: simd_long3, _ mask: simd_long3) -> simd_long3
```

```c
static simd_long3 simd_bitselect(simd_long3 x, simd_long3 y, simd_long3 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_long3) -> simd_bool](./simd_any%28_%29-698ng.md)
- [func simd_all(simd_long3) -> simd_bool](./simd_all%28_%29-1ao6q.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-9hl4)*