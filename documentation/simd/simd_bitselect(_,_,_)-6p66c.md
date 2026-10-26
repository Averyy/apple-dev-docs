# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_int2, _ y: simd_int2, _ mask: simd_int2) -> simd_int2
```

```c
static simd_int2 simd_bitselect(simd_int2 x, simd_int2 y, simd_int2 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_int2) -> simd_bool](./simd_any%28_%29-64rh5.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_int2) -> simd_bool](./simd_all%28_%29-1cxjv.md)
  Returns true if the high-order bit of every element is set; false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-6p66c)*