# simd_sign(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the sign of each element in a vector.

## Declaration

```swift
func simd_sign(_ x: simd_half2) -> simd_half2
```

```c
static simd_half2 simd_sign(simd_half2 x);
```

## See Also

### Common functions
- [func simd_abs(simd_half2) -> simd_half2](./simd_abs%28_%29-889zu.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_half2, simd_half2, simd_half2) -> simd_half2](./simd_clamp%28_,_,_%29-8crce.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half2, simd_half2) -> simd_bool](./simd_equal%28_,_%29-6mu96.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half2) -> simd_half2](./simd_fract%28_%29-42lx3.md)
  Returns the fractional part of each element in a vector.
- [func simd_step(simd_half2, simd_half2) -> simd_half2](./simd_step%28_,_%29-4dqzp.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_sign(_:)-6jn8t)*