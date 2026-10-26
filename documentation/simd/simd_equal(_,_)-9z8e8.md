# simd_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.

## Declaration

```swift
func simd_equal(_ x: simd_float2, _ y: simd_float2) -> simd_bool
```

```c
static simd_bool simd_equal(simd_float2 x, simd_float2 y);
```

## See Also

### Common Functions
- [func simd_abs(simd_float2) -> simd_float2](./simd_abs%28_%29-886vq.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD2<Float>) -> SIMD2<Float>](./abs%28_%29-6ckob.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float2, simd_float2, simd_float2) -> simd_float2](./simd_clamp%28_,_,_%29-9b6uf.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Float>, min: Float, max: Float) -> SIMD2<Float>](./clamp%28_,min,max%29-5rthg.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Float>, min: SIMD2<Float>, max: SIMD2<Float>) -> SIMD2<Float>](./clamp%28_,min,max%29-3oo0f.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_fract(simd_float2) -> simd_float2](./simd_fract%28_%29-42ipv.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD2<Float>) -> SIMD2<Float>](./fract%28_%29-7rplw.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_float2) -> simd_float2](./simd_sign%28_%29-6jld1.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD2<Float>) -> SIMD2<Float>](./sign%28_%29-2e6do.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float2, simd_float2) -> simd_float2](./simd_step%28_,_%29-9xjdc.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD2<Float>, edge: SIMD2<Float>) -> SIMD2<Float>](./step%28_,edge%29-1pthr.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_equal(_:_:)-9z8e8)*