# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the absolute value of each element in a vector.

## Declaration

```swift
func simd_clamp(_ x: simd_long8, _ min: simd_long8, _ max: simd_long8) -> simd_long8
```

```c
static simd_long8 simd_clamp(simd_long8 x, simd_long8 min, simd_long8 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_long8) -> simd_long8](./simd_abs%28_%29-7osxw.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_long8, simd_long8) -> simd_bool](./simd_equal%28_,_%29-1fygf.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-7h5og)*