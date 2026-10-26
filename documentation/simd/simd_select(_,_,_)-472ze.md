# simd_select(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.

## Declaration

```swift
func simd_select(_ x: simd_half2, _ y: simd_half2, _ mask: simd_short2) -> simd_half2
```

```c
static simd_half2 simd_select(simd_half2 x, simd_half2 y, simd_short2 mask);
```

## See Also

### Logic functions
- [func simd_bitselect(simd_half2, simd_half2, simd_short2) -> simd_half2](./simd_bitselect%28_,_,_%29-3g1i8.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_select(_:_:_:)-472ze)*