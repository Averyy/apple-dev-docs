# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_long4, _ min: simd_long4, _ max: simd_long4) -> simd_long4
```

```c
static simd_long4 simd_clamp(simd_long4 x, simd_long4 min, simd_long4 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_long4) -> simd_long4](./simd_abs%28_%29-81f1k.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_long4, simd_long4) -> simd_bool](./simd_equal%28_,_%29-4wnv3.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-69473)*