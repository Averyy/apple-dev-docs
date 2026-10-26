# simd_select(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.

## Declaration

```swift
func simd_select(_ x: simd_half32, _ y: simd_half32, _ mask: simd_short32) -> simd_half32
```

```c
static simd_half32 simd_select(simd_half32 x, simd_half32 y, simd_short32 mask);
```

## See Also

### Logic functions
- [func simd_bitselect(simd_half32, simd_half32, simd_short32) -> simd_half32](./simd_bitselect%28_,_,_%29-81xk8.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_select(_:_:_:)-63scw)*