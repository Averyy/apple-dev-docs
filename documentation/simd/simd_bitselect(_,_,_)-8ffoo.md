# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_long2, _ y: simd_long2, _ mask: simd_long2) -> simd_long2
```

```c
static simd_long2 simd_bitselect(simd_long2 x, simd_long2 y, simd_long2 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_long2) -> simd_bool](./simd_any%28_%29-64pz3.md)
- [func simd_all(simd_long2) -> simd_bool](./simd_all%28_%29-1cyyp.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-8ffoo)*