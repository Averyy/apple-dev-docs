# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_double2, _ y: simd_double2, _ mask: simd_long2) -> simd_double2
```

```c
static simd_double2 simd_bitselect(simd_double2 x, simd_double2 y, simd_long2 mask);
```

## See Also

### Logic Functions
- [func simd_select(simd_double2, simd_double2, simd_long2) -> simd_double2](./simd_select%28_,_,_%29-7sz6k.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-3ys1a)*