# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_half32, _ min: simd_half32, _ max: simd_half32) -> simd_half32
```

```c
static simd_half32 simd_clamp(simd_half32 x, simd_half32 min, simd_half32 max);
```

## See Also

### Common functions
- [func simd_abs(simd_half32) -> simd_half32](./simd_abs%28_%29-2byol.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_half32, simd_half32) -> simd_bool](./simd_equal%28_,_%29-5620v.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half32) -> simd_half32](./simd_fract%28_%29-4zj0y.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half32) -> simd_half32](./simd_sign%28_%29-9r24j.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half32, simd_half32) -> simd_half32](./simd_step%28_,_%29-2kbac.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-868pk)*