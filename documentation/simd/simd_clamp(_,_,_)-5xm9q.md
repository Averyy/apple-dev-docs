# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_char3, _ min: simd_char3, _ max: simd_char3) -> simd_char3
```

```c
static simd_char3 simd_clamp(simd_char3 x, simd_char3 min, simd_char3 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_char3) -> simd_char3](./simd_abs%28_%29-8d1l3.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_char3, simd_char3) -> simd_bool](./simd_equal%28_,_%29-ymae.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-5xm9q)*