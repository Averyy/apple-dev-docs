# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_uchar3, _ min: simd_uchar3, _ max: simd_uchar3) -> simd_uchar3
```

```c
static simd_uchar3 simd_clamp(simd_uchar3 x, simd_uchar3 min, simd_uchar3 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_uchar3, simd_uchar3) -> simd_bool](./simd_equal%28_,_%29-8iga0.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-6h8i3)*