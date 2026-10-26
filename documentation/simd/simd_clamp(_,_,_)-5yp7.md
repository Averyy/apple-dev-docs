# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_uint2, _ min: simd_uint2, _ max: simd_uint2) -> simd_uint2
```

```c
static simd_uint2 simd_clamp(simd_uint2 x, simd_uint2 min, simd_uint2 max);
```

## See Also

### Common Functions
- [func clamp(SIMD2<UInt32>, min: UInt32, max: UInt32) -> SIMD2<UInt32>](./clamp%28_,min,max%29-5cyx4.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<UInt32>, min: SIMD2<UInt32>, max: SIMD2<UInt32>) -> SIMD2<UInt32>](./clamp%28_,min,max%29-59rk7.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uint2, simd_uint2) -> simd_bool](./simd_equal%28_,_%29-2urgh.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-5yp7)*