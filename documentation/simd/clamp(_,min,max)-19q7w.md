# clamp(_:min:max:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func clamp(_ x: SIMD4<Float>, min: SIMD4<Float>, max: SIMD4<Float>) -> SIMD4<Float>
```

## See Also

### Common Functions
- [func simd_abs(simd_float4) -> simd_float4](./simd_abs%28_%29-81qo8.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD4<Float>) -> SIMD4<Float>](./abs%28_%29-1fzhv.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float4, simd_float4, simd_float4) -> simd_float4](./simd_clamp%28_,_,_%29-6vmhh.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<Float>, min: Float, max: Float) -> SIMD4<Float>](./clamp%28_,min,max%29-46ay6.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_float4, simd_float4) -> simd_bool](./simd_equal%28_,_%29-6sa26.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_float4) -> simd_float4](./simd_fract%28_%29-3w2rh.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD4<Float>) -> SIMD4<Float>](./fract%28_%29-9s3df.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_float4) -> simd_float4](./simd_sign%28_%29-74zwz.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD4<Float>) -> SIMD4<Float>](./sign%28_%29-167c1.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float4, simd_float4) -> simd_float4](./simd_step%28_,_%29-1fxwh.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD4<Float>, edge: SIMD4<Float>) -> SIMD4<Float>](./step%28_,edge%29-8we4c.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/clamp(_:min:max:)-19q7w)*