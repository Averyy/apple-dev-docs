# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_half4, _ y: simd_half4, _ mask: simd_short4) -> simd_half4
```

```c
static simd_half4 simd_bitselect(simd_half4 x, simd_half4 y, simd_short4 mask);
```

## See Also

### Logic functions
- [func simd_select(simd_half4, simd_half4, simd_short4) -> simd_half4](./simd_select%28_,_,_%29-4vjt.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-6gy8u)*