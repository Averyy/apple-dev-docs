# simd_select(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.

## Declaration

```swift
func simd_select(_ x: simd_float2, _ y: simd_float2, _ mask: simd_int2) -> simd_float2
```

```c
static simd_float2 simd_select(simd_float2 x, simd_float2 y, simd_int2 mask);
```

## See Also

### Logic Functions
- [func simd_bitselect(simd_float2, simd_float2, simd_int2) -> simd_float2](./simd_bitselect%28_,_,_%29-5g70k.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_select(_:_:_:)-9jdc0)*