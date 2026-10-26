# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_long4, _ y: simd_long4, _ mask: simd_long4) -> simd_long4
```

```c
static simd_long4 simd_bitselect(simd_long4 x, simd_long4 y, simd_long4 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_long4) -> simd_bool](./simd_any%28_%29-6cnfh.md)
- [func simd_all(simd_long4) -> simd_bool](./simd_all%28_%29-1jv5n.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-9f5q6)*