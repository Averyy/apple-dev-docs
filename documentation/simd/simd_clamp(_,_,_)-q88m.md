# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_double8, _ min: simd_double8, _ max: simd_double8) -> simd_double8
```

```c
static simd_double8 simd_clamp(simd_double8 x, simd_double8 min, simd_double8 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_double8) -> simd_double8](./simd_abs%28_%29-7p0dw.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_double8, simd_double8) -> simd_bool](./simd_equal%28_,_%29-8pk1m.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_double8) -> simd_double8](./simd_fract%28_%29-3jcfd.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_double8) -> simd_double8](./simd_sign%28_%29-7hb8r.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_double8, simd_double8) -> simd_double8](./simd_step%28_,_%29-1vckv.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-q88m)*