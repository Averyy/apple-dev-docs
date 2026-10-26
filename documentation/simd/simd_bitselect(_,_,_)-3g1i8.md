# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_half2, _ y: simd_half2, _ mask: simd_short2) -> simd_half2
```

```c
static simd_half2 simd_bitselect(simd_half2 x, simd_half2 y, simd_short2 mask);
```

## See Also

### Logic functions
- [func simd_select(simd_half2, simd_half2, simd_short2) -> simd_half2](./simd_select%28_,_,_%29-472ze.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-3g1i8)*