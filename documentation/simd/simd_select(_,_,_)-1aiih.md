# simd_select(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.

## Declaration

```swift
func simd_select(_ x: simd_double3, _ y: simd_double3, _ mask: simd_long3) -> simd_double3
```

```c
static simd_double3 simd_select(simd_double3 x, simd_double3 y, simd_long3 mask);
```

## See Also

### Logic Functions
- [func simd_bitselect(simd_double3, simd_double3, simd_long3) -> simd_double3](./simd_bitselect%28_,_,_%29-mtv1.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_select(_:_:_:)-1aiih)*