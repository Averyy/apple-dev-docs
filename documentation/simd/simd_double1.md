# simd_double1

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of one 64-bit floating-point element.

## Declaration

```swift
typealias simd_double1 = Double
```

```c
typedef double simd_double1;
```

## Topics

### Common Functions
- [func step(Double, edge: Double) -> Double](./step%28_,edge%29-382a5.md)
- [func simd_step(Double, Double) -> Double](./simd_step%28_,_%29-8mpre.md)
- [func simd_clamp(Double, Double, Double) -> Double](./simd_clamp%28_,_,_%29-1ktlk.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_fract(Double) -> Double](./simd_fract%28_%29-1wsn4.md)
  Returns the fractional part of each element in a vector.
- [func sign(Double) -> Double](./sign%28_%29-iwmp.md)
  Returns the sign of each element in a vector.
- [func simd_sign(Double) -> Double](./simd_sign%28_%29-937ee.md)
  Returns the sign of each element in a vector.
### Interpolation Functions
- [func simd_smoothstep(Double, Double, Double) -> Double](./simd_smoothstep%28_,_,_%29-5839l.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func simd_mix(Double, Double, Double) -> Double](./simd_mix%28_,_,_%29-6aqwp.md)
  Returns an element-wise linearly interpolated value between two vectors.
### Extrema Functions
- [func min(SIMD4<Double>, Double) -> SIMD4<Double>](./min%28_,_%29-7rmn.md)
  Returns the minimum value of each element in a vector.
- [func simd_min(Double, Double) -> Double](./simd_min%28_,_%29-x4en.md)
  Returns the minimum value of each element in a vector.
- [func max(SIMD2<Double>, Double) -> SIMD2<Double>](./max%28_,_%29-3puhr.md)
  Returns the maximum value of each element in a vector.
- [func simd_max(Double, Double) -> Double](./simd_max%28_,_%29-9ibgs.md)
  Returns the maximum value of each element in a vector.
### Math Functions
- [func simd_muladd(Double, Double, Double) -> Double](./simd_muladd%28_,_,_%29-9hwx1.md)
  Returns the multiply-add result for corresponding elements in three vectors.
### Reciprocal and Reciprocal Square Root Functions
- [func recip(Double) -> Double](./recip%28_%29-8b6ef.md)
  Returns the reciprocal of each element in a vector.
- [func simd_recip(Double) -> Double](./simd_recip%28_%29-7ylz3.md)
  Returns the reciprocal of each element in a vector.
- [func simd_fast_recip(Double) -> Double](./simd_fast_recip%28_%29-1h1e.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_precise_recip(Double) -> Double](./simd_precise_recip%28_%29-6qb0h.md)
  Returns the precise reciprocal of each element in a vector.
- [func rsqrt(Double) -> Double](./rsqrt%28_%29-7h0u6.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_rsqrt(Double) -> Double](./simd_rsqrt%28_%29-4ygr4.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_fast_rsqrt(Double) -> Double](./simd_fast_rsqrt%28_%29-43tvc.md)
  Returns the fast reciprocal square root of each element in a vector.
- [func simd_precise_rsqrt(Double) -> Double](./simd_precise_rsqrt%28_%29-5fl9s.md)
  Returns the precise reciprocal square root of each element in a vector.

## See Also

### Vector data types
- [typealias simd_double2](./simd_double2.md)
  A vector of two 64-bit floating-point elements.
- [typealias simd_double3](./simd_double3.md)
  A vector of three 64-bit floating-point elements.
- [typealias simd_double4](./simd_double4.md)
  A vector of four 64-bit floating-point elements.
- [typealias simd_double8](./simd_double8.md)
  A vector of eight 64-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double1)*