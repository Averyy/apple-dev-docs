# simd_step(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns zero for each element in a vector less than a specified edge, and otherwise returns one.

## Declaration

```swift
func simd_step(_ edge: simd_double2, _ x: simd_double2) -> simd_double2
```

```c
static simd_double2 simd_step(simd_double2 edge, simd_double2 x);
```

## See Also

### Common Functions
- [func simd_abs(simd_double2) -> simd_double2](./simd_abs%28_%29-8869e.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD2<Double>) -> SIMD2<Double>](./abs%28_%29-1p8t7.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_double2, simd_double2, simd_double2) -> simd_double2](./simd_clamp%28_,_,_%29-6puwa.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Double>, min: Double, max: Double) -> SIMD2<Double>](./clamp%28_,min,max%29-7n2jv.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Double>, min: SIMD2<Double>, max: SIMD2<Double>) -> SIMD2<Double>](./clamp%28_,min,max%29-6d1s7.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_double2, simd_double2) -> simd_bool](./simd_equal%28_,_%29-vmn4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_double2) -> simd_double2](./simd_fract%28_%29-42i3r.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD2<Double>) -> SIMD2<Double>](./fract%28_%29-2gjrn.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_double2) -> simd_double2](./simd_sign%28_%29-6jlx9.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD2<Double>) -> SIMD2<Double>](./sign%28_%29-5fczz.md)
  Returns the sign of each element in a vector.
- [func step(SIMD2<Double>, edge: SIMD2<Double>) -> SIMD2<Double>](./step%28_,edge%29-2qauk.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_step(_:_:)-8jlf2)*