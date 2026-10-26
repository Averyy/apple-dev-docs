# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_uchar16, _ min: simd_uchar16, _ max: simd_uchar16) -> simd_uchar16
```

```c
static simd_uchar16 simd_clamp(simd_uchar16 x, simd_uchar16 min, simd_uchar16 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_uchar16, simd_uchar16) -> simd_bool](./simd_equal%28_,_%29-6la77.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-1zlhc)*