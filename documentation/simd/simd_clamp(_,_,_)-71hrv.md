# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_uchar2, _ min: simd_uchar2, _ max: simd_uchar2) -> simd_uchar2
```

```c
static simd_uchar2 simd_clamp(simd_uchar2 x, simd_uchar2 min, simd_uchar2 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_uchar2, simd_uchar2) -> simd_bool](./simd_equal%28_,_%29-7ujh6.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-71hrv)*