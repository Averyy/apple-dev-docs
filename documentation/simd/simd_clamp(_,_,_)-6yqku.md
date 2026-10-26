# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_long3, _ min: simd_long3, _ max: simd_long3) -> simd_long3
```

```c
static simd_long3 simd_clamp(simd_long3 x, simd_long3 min, simd_long3 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_long3) -> simd_long3](./simd_abs%28_%29-8d3rx.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_long3, simd_long3) -> simd_bool](./simd_equal%28_,_%29-1ikxk.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-6yqku)*