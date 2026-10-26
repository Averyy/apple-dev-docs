# simd_fract(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the fractional part of each element in a vector.

## Declaration

```swift
func simd_fract(_ x: simd_half32) -> simd_half32
```

```c
static simd_half32 simd_fract(simd_half32 x);
```

## See Also

### Common functions
- [func simd_abs(simd_half32) -> simd_half32](./simd_abs%28_%29-2byol.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_half32, simd_half32, simd_half32) -> simd_half32](./simd_clamp%28_,_,_%29-868pk.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half32, simd_half32) -> simd_bool](./simd_equal%28_,_%29-5620v.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_sign(simd_half32) -> simd_half32](./simd_sign%28_%29-9r24j.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half32, simd_half32) -> simd_half32](./simd_step%28_,_%29-2kbac.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_fract(_:)-4zj0y)*