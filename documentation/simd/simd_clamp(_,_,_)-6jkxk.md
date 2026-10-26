# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_char64, _ min: simd_char64, _ max: simd_char64) -> simd_char64
```

```c
static simd_char64 simd_clamp(simd_char64 x, simd_char64 min, simd_char64 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_char64) -> simd_char64](./simd_abs%28_%29-1p85t.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_char64, simd_char64) -> simd_bool](./simd_equal%28_,_%29-8ghe2.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-6jkxk)*