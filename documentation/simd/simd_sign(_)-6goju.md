# simd_sign(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the sign of each element in a vector.

## Declaration

```swift
func simd_sign(_ x: simd_double3) -> simd_double3
```

```c
static simd_double3 simd_sign(simd_double3 x);
```

## See Also

### Common Functions
- [func simd_abs(simd_double3) -> simd_double3](./simd_abs%28_%29-8db3x.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD3<Double>) -> SIMD3<Double>](./abs%28_%29-8miv.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_double3, simd_double3, simd_double3) -> simd_double3](./simd_clamp%28_,_,_%29-2jao.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Double>, min: Double, max: Double) -> SIMD3<Double>](./clamp%28_,min,max%29-5otf7.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Double>, min: SIMD3<Double>, max: SIMD3<Double>) -> SIMD3<Double>](./clamp%28_,min,max%29-6m2so.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_double3, simd_double3) -> simd_bool](./simd_equal%28_,_%29-4v2cb.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_double3) -> simd_double3](./simd_fract%28_%29-47n4w.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD3<Double>) -> SIMD3<Double>](./fract%28_%29-swov.md)
  Returns the fractional part of each element in a vector.
- [func sign(SIMD3<Double>) -> SIMD3<Double>](./sign%28_%29-2qtea.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_double3, simd_double3) -> simd_double3](./simd_step%28_,_%29-2gbx7.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD3<Double>, edge: SIMD3<Double>) -> SIMD3<Double>](./step%28_,edge%29-4azct.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_sign(_:)-6goju)*