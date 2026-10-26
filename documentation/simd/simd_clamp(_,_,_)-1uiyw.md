# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_uchar8, _ min: simd_uchar8, _ max: simd_uchar8) -> simd_uchar8
```

```c
static simd_uchar8 simd_clamp(simd_uchar8 x, simd_uchar8 min, simd_uchar8 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_uchar8, simd_uchar8) -> simd_bool](./simd_equal%28_,_%29-5o6ip.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-1uiyw)*