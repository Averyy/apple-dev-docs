# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_int16, _ min: simd_int16, _ max: simd_int16) -> simd_int16
```

```c
static simd_int16 simd_clamp(simd_int16 x, simd_int16 min, simd_int16 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_int16) -> simd_int16](./simd_abs%28_%29-477j8.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_int16, simd_int16) -> simd_bool](./simd_equal%28_,_%29-5fwh2.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-5xcny)*