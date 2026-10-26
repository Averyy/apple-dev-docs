# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: Float16, _ min: Float16, _ max: Float16) -> Float16
```

```c
static _Float16 simd_clamp(_Float16 x, _Float16 min, _Float16 max);
```

## See Also

### Common functions
- [func simd_fract(Float16) -> Float16](./simd_fract%28_%29-1wwew.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(Float16) -> Float16](./simd_sign%28_%29-9365i.md)
  Returns the sign of each element in a vector.
- [func simd_step(Float16, Float16) -> Float16](./simd_step%28_,_%29-u24h.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-c4d6)*