# simd_half1

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of one 16-bit floating-point element.

## Declaration

```swift
typealias simd_half1 = Float16
```

```c
typedef _Float16 simd_half1;
```

## Topics

### Common functions
- [func simd_clamp(Float16, Float16, Float16) -> Float16](./simd_clamp%28_,_,_%29-c4d6.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_fract(Float16) -> Float16](./simd_fract%28_%29-1wwew.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(Float16) -> Float16](./simd_sign%28_%29-9365i.md)
  Returns the sign of each element in a vector.
- [func simd_step(Float16, Float16) -> Float16](./simd_step%28_,_%29-u24h.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Interpolation functions
- [func simd_mix(Float16, Float16, Float16) -> Float16](./simd_mix%28_,_,_%29-3mcrj.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(Float16, Float16, Float16) -> Float16](./simd_smoothstep%28_,_,_%29-6zp30.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema functions
- [func simd_max(Float16, Float16) -> Float16](./simd_max%28_,_%29-3f8z7.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(Float16, Float16) -> Float16](./simd_min%28_,_%29-57wqc.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and reciprocal square root functions
- [func simd_recip(Float16) -> Float16](./simd_recip%28_%29-7yi5r.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(Float16) -> Float16](./simd_rsqrt%28_%29-4yfi0.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(Float16) -> Float16](./simd_precise_recip%28_%29-6q9sp.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(Float16) -> Float16](./simd_precise_rsqrt%28_%29-5fjxk.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(Float16) -> Float16](./simd_fast_recip%28_%29-1ibu.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(Float16) -> Float16](./simd_fast_rsqrt%28_%29-43sls.md)
  Returns the fast reciprocal square root of each element in a vector.
### Math functions
- [func simd_muladd(Float16, Float16, Float16) -> Float16](./simd_muladd%28_,_,_%29-41x8n.md)
  Returns the multiply-add result for corresponding elements in three vectors.

## See Also

### Vector data types
- [typealias simd_half2](./simd_half2.md)
  A vector of two 16-bit floating-point elements.
- [typealias simd_half3](./simd_half3.md)
  A vector of three 16-bit floating-point elements.
- [typealias simd_half4](./simd_half4.md)
  A vector of four 16-bit floating-point elements.
- [typealias simd_half8](./simd_half8.md)
  A vector of eight 16-bit floating-point elements.
- [typealias simd_half16](./simd_half16.md)
  A vector of sixteen 16-bit floating-point elements.
- [typealias simd_half32](./simd_half32.md)
  A vector of thirty-two 16-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half1)*