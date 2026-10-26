# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_short16, _ min: simd_short16, _ max: simd_short16) -> simd_short16
```

```c
static simd_short16 simd_clamp(simd_short16 x, simd_short16 min, simd_short16 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_short16) -> simd_short16](./simd_abs%28_%29-47an0.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_short16, simd_short16) -> simd_bool](./simd_equal%28_,_%29-220xu.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-9ykva)*