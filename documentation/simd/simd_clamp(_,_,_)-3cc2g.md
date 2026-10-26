# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_short8, _ min: simd_short8, _ max: simd_short8) -> simd_short8
```

```c
static simd_short8 simd_clamp(simd_short8 x, simd_short8 min, simd_short8 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_short8) -> simd_short8](./simd_abs%28_%29-7otzk.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_short8, simd_short8) -> simd_bool](./simd_equal%28_,_%29-4n1gi.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-3cc2g)*