# simd_abs(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the absolute value of each element in a vector.

## Declaration

```swift
func simd_abs(_ x: simd_float3) -> simd_float3
```

```c
static simd_float3 simd_abs(simd_float3 x);
```

## See Also

### Common Functions
- [func abs(SIMD3<Float>) -> SIMD3<Float>](./abs%28_%29-6lc19.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float3, simd_float3, simd_float3) -> simd_float3](./simd_clamp%28_,_,_%29-5szev.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Float>, min: Float, max: Float) -> SIMD3<Float>](./clamp%28_,min,max%29-3esdw.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Float>, min: SIMD3<Float>, max: SIMD3<Float>) -> SIMD3<Float>](./clamp%28_,min,max%29-9eeiz.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_float3, simd_float3) -> simd_bool](./simd_equal%28_,_%29-6i7q4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func fract(SIMD3<Float>) -> SIMD3<Float>](./fract%28_%29-3rsxo.md)
  Returns the fractional part of each element in a vector.
- [func simd_fract(simd_float3) -> simd_float3](./simd_fract%28_%29-47mh4.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_float3) -> simd_float3](./simd_sign%28_%29-6gp3q.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD3<Float>) -> SIMD3<Float>](./sign%28_%29-9p5uo.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float3, simd_float3) -> simd_float3](./simd_step%28_,_%29-9ygnw.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD3<Float>, edge: SIMD3<Float>) -> SIMD3<Float>](./step%28_,edge%29-48vbr.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_abs(_:)-8dafp)*