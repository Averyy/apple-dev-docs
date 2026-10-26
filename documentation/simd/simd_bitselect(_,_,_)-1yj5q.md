# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_double8, _ y: simd_double8, _ mask: simd_long8) -> simd_double8
```

```c
static simd_double8 simd_bitselect(simd_double8 x, simd_double8 y, simd_long8 mask);
```

## See Also

### Logic Functions
- [func simd_select(simd_double8, simd_double8, simd_long8) -> simd_double8](./simd_select%28_,_,_%29-8wti7.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-1yj5q)*