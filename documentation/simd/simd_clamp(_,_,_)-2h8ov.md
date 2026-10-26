# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_half3, _ min: simd_half3, _ max: simd_half3) -> simd_half3
```

```c
static simd_half3 simd_clamp(simd_half3 x, simd_half3 min, simd_half3 max);
```

## See Also

### Common functions
- [func simd_abs(simd_half3) -> simd_half3](./simd_abs%28_%29-8derx.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_half3, simd_half3) -> simd_bool](./simd_equal%28_,_%29-9k8m9.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half3) -> simd_half3](./simd_fract%28_%29-47quw.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half3) -> simd_half3](./simd_sign%28_%29-6gppu.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half3, simd_half3) -> simd_half3](./simd_step%28_,_%29-8w7e.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-2h8ov)*