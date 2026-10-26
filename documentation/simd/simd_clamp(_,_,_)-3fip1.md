# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_short4, _ min: simd_short4, _ max: simd_short4) -> simd_short4
```

```c
static simd_short4 simd_clamp(simd_short4 x, simd_short4 min, simd_short4 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_short4) -> simd_short4](./simd_abs%28_%29-81n9o.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_short4, simd_short4) -> simd_bool](./simd_equal%28_,_%29-51wsu.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-3fip1)*