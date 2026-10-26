# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_float16, _ y: simd_float16, _ mask: simd_int16) -> simd_float16
```

```c
static simd_float16 simd_bitselect(simd_float16 x, simd_float16 y, simd_int16 mask);
```

## See Also

### Logic Functions
- [func simd_select(simd_float16, simd_float16, simd_int16) -> simd_float16](./simd_select%28_,_,_%29-41fgt.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-wjqf)*