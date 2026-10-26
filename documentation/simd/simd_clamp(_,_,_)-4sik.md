# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_long2, _ min: simd_long2, _ max: simd_long2) -> simd_long2
```

```c
static simd_long2 simd_clamp(simd_long2 x, simd_long2 min, simd_long2 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_long2) -> simd_long2](./simd_abs%28_%29-88ipu.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_long2, simd_long2) -> simd_bool](./simd_equal%28_,_%29-2qcs1.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-4sik)*