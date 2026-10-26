# simd_fract(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the fractional part of each element in a vector.

## Declaration

```swift
func simd_fract(_ x: simd_float16) -> simd_float16
```

```c
static simd_float16 simd_fract(simd_float16 x);
```

## See Also

### Common Functions
- [func simd_abs(simd_float16) -> simd_float16](./simd_abs%28_%29-47h6g.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float16, simd_float16, simd_float16) -> simd_float16](./simd_clamp%28_,_,_%29-92son.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_float16, simd_float16) -> simd_bool](./simd_equal%28_,_%29-376kl.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_sign(simd_float16) -> simd_float16](./simd_sign%28_%29-tc2v.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float16, simd_float16) -> simd_float16](./simd_step%28_,_%29-14cn0.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_fract(_:)-6v1ix)*