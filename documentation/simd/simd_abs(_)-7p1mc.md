# simd_abs(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the absolute value of each element in a vector.

## Declaration

```swift
func simd_abs(_ x: simd_half8) -> simd_half8
```

```c
static simd_half8 simd_abs(simd_half8 x);
```

## See Also

### Common functions
- [func simd_clamp(simd_half8, simd_half8, simd_half8) -> simd_half8](./simd_clamp%28_,_,_%29-7a090.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half8, simd_half8) -> simd_bool](./simd_equal%28_,_%29-8nejo.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half8) -> simd_half8](./simd_fract%28_%29-3jdnl.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half8) -> simd_half8](./simd_sign%28_%29-7hck3.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half8, simd_half8) -> simd_half8](./simd_step%28_,_%29-5v3vi.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_abs(_:)-7p1mc)*