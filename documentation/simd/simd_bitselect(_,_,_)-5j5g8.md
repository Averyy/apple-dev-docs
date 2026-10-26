# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_float3, _ y: simd_float3, _ mask: simd_int3) -> simd_float3
```

```c
static simd_float3 simd_bitselect(simd_float3 x, simd_float3 y, simd_int3 mask);
```

## See Also

### Logic Functions
- [func simd_select(simd_float3, simd_float3, simd_int3) -> simd_float3](./simd_select%28_,_,_%29-9gbqb.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-5j5g8)*