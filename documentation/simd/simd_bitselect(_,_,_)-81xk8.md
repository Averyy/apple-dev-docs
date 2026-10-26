# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_half32, _ y: simd_half32, _ mask: simd_short32) -> simd_half32
```

```c
static simd_half32 simd_bitselect(simd_half32 x, simd_half32 y, simd_short32 mask);
```

## See Also

### Logic functions
- [func simd_select(simd_half32, simd_half32, simd_short32) -> simd_half32](./simd_select%28_,_,_%29-63scw.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-81xk8)*