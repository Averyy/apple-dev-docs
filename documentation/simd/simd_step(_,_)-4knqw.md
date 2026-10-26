# simd_step(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns zero for each element in a vector less than a specified edge, and otherwise returns one.

## Declaration

```swift
func simd_step(_ edge: simd_half4, _ x: simd_half4) -> simd_half4
```

```c
static simd_half4 simd_step(simd_half4 edge, simd_half4 x);
```

## See Also

### Common functions
- [func simd_abs(simd_half4) -> simd_half4](./simd_abs%28_%29-81q3k.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_half4, simd_half4, simd_half4) -> simd_half4](./simd_clamp%28_,_,_%29-2vvpa.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half4, simd_half4) -> simd_bool](./simd_equal%28_,_%29-6nuuw.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half4) -> simd_half4](./simd_fract%28_%29-3w251.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half4) -> simd_half4](./simd_sign%28_%29-7533b.md)
  Returns the sign of each element in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_step(_:_:)-4knqw)*