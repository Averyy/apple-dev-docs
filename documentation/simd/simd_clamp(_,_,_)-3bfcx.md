# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_uchar32, _ min: simd_uchar32, _ max: simd_uchar32) -> simd_uchar32
```

```c
static simd_uchar32 simd_clamp(simd_uchar32 x, simd_uchar32 min, simd_uchar32 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_uchar32, simd_uchar32) -> simd_bool](./simd_equal%28_,_%29-qmif.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-3bfcx)*