# simd_step(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns zero for each element in a vector less than a specified edge, and otherwise returns one.

## Declaration

```swift
func simd_step(_ edge: Float16, _ x: Float16) -> Float16
```

```c
static _Float16 simd_step(_Float16 edge, _Float16 x);
```

## See Also

### Common functions
- [func simd_clamp(Float16, Float16, Float16) -> Float16](./simd_clamp%28_,_,_%29-c4d6.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_fract(Float16) -> Float16](./simd_fract%28_%29-1wwew.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(Float16) -> Float16](./simd_sign%28_%29-9365i.md)
  Returns the sign of each element in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_step(_:_:)-u24h)*