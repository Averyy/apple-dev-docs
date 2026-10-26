# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_double4, _ y: simd_double4, _ mask: simd_long4) -> simd_double4
```

```c
static simd_double4 simd_bitselect(simd_double4 x, simd_double4 y, simd_long4 mask);
```

## See Also

### Logic Functions
- [func simd_select(simd_double4, simd_double4, simd_long4) -> simd_double4](./simd_select%28_,_,_%29-tq6k.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-1mn6g)*