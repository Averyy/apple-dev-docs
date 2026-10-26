# simd_half2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 16-bit floating-point elements.

## Declaration

```swift
typealias simd_half2 = SIMD2<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(2))) simd_half2;
```

## Topics

### Functions to create two-element vectors from other vectors
- [func simd_make_half2(simd_half2) -> simd_half2](./simd_make_half2%28_%29-1857c.md)
  Returns a new vector from the specified vector.
- [func simd_make_half2(simd_half3) -> simd_half2](./simd_make_half2%28_%29-1b2kr.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_half2(simd_half4) -> simd_half2](./simd_make_half2%28_%29-1t11m.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_half2(simd_half8) -> simd_half2](./simd_make_half2%28_%29-27x5a.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_half2(simd_half16) -> simd_half2](./simd_make_half2%28_%29-9auhj.md)
  Returns a new vector by truncating the specified 16-element vector.
- [func simd_make_half2(simd_half32) -> simd_half2](./simd_make_half2%28_%29-4bzdr.md)
  Returns a new vector by truncating the specified 32-element vector.
### Functions to create two-element vectors from scalar values
- [func simd_make_half2(Float16) -> simd_half2](./simd_make_half2%28_%29-9q31.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_half2(Float16, Float16) -> simd_half2](./simd_make_half2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_half2_undef(Float16) -> simd_half2](./simd_make_half2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common functions
- [func simd_abs(simd_half2) -> simd_half2](./simd_abs%28_%29-889zu.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_half2, simd_half2, simd_half2) -> simd_half2](./simd_clamp%28_,_,_%29-8crce.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half2, simd_half2) -> simd_bool](./simd_equal%28_,_%29-6mu96.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half2) -> simd_half2](./simd_fract%28_%29-42lx3.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half2) -> simd_half2](./simd_sign%28_%29-6jn8t.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half2, simd_half2) -> simd_half2](./simd_step%28_,_%29-4dqzp.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce functions
- [func simd_reduce_add(simd_half2) -> Float16](./simd_reduce_add%28_%29-2q3zq.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_half2) -> Float16](./simd_reduce_max%28_%29-4kf4c.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_half2) -> Float16](./simd_reduce_min%28_%29-49pb0.md)
  Returns the minimum value in a vector.
### Interpolation functions
- [func simd_mix(simd_half2, simd_half2, simd_half2) -> simd_half2](./simd_mix%28_,_,_%29-33iiq.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_half2, simd_half2, simd_half2) -> simd_half2](./simd_smoothstep%28_,_,_%29-9x0u5.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema functions
- [func simd_max(simd_half2, simd_half2) -> simd_half2](./simd_max%28_,_%29-3wsb8.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_half2, simd_half2) -> simd_half2](./simd_min%28_,_%29-6mo5o.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and reciprocal square root functions
- [func simd_recip(simd_half2) -> simd_half2](./simd_recip%28_%29-8ni98.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_half2) -> simd_half2](./simd_rsqrt%28_%29-oj14.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_half2) -> simd_half2](./simd_precise_recip%28_%29-66ohg.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_half2) -> simd_half2](./simd_precise_rsqrt%28_%29-wvby.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_half2) -> simd_half2](./simd_fast_recip%28_%29-ln7x.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_half2) -> simd_half2](./simd_fast_rsqrt%28_%29-84ema.md)
  Returns the fast reciprocal square root of each element in a vector.
### Logic functions
- [func simd_select(simd_half2, simd_half2, simd_short2) -> simd_half2](./simd_select%28_,_,_%29-472ze.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_half2, simd_half2, simd_short2) -> simd_half2](./simd_bitselect%28_,_,_%29-3g1i8.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math functions
- [func simd_muladd(simd_half2, simd_half2, simd_half2) -> simd_half2](./simd_muladd%28_,_,_%29-30k16.md)
  Returns the multiply-add result for corresponding elements in three vectors.

## See Also

### Vector data types
- [typealias simd_half1](./simd_half1.md)
  A vector of one 16-bit floating-point element.
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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half2)*