# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_uchar64, _ min: simd_uchar64, _ max: simd_uchar64) -> simd_uchar64
```

```c
static simd_uchar64 simd_clamp(simd_uchar64 x, simd_uchar64 min, simd_uchar64 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_uchar64, simd_uchar64) -> simd_bool](./simd_equal%28_,_%29-494kp.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-52h9h)*