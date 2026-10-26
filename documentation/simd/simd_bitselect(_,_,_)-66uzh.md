# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_float8, _ y: simd_float8, _ mask: simd_int8) -> simd_float8
```

```c
static simd_float8 simd_bitselect(simd_float8 x, simd_float8 y, simd_int8 mask);
```

## See Also

### Logic Functions
- [func simd_select(simd_float8, simd_float8, simd_int8) -> simd_float8](./simd_select%28_,_,_%29-5h243.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-66uzh)*