# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_float4, _ y: simd_float4, _ mask: simd_int4) -> simd_float4
```

```c
static simd_float4 simd_bitselect(simd_float4 x, simd_float4 y, simd_int4 mask);
```

## See Also

### Logic Functions
- [func simd_select(simd_float4, simd_float4, simd_int4) -> simd_float4](./simd_select%28_,_,_%29-7vjx6.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-7g1os)*