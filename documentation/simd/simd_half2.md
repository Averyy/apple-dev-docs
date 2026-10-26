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
### Functions to create two-element vectors from vectors of other types
- [simd_half](./simd_half-2u7u3.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_half](./simd_half-2uhrf.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_half](./simd_half-2ucqz.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_half](./simd_half-2umx7.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_half](./simd_half-2ub2n.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_half](./simd_half-2ukun.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_half](./simd_half-2uco9.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_half](./simd_half-2umll.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_half](./simd_half-2ulcx.md)
  Returns a new vector from the specified vector of 16-bit, floating-point elements.
- [simd_half](./simd_half-2ujap.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_half](./simd_half-2ujxl.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Geometry functions
- [simd_cross](./simd_cross-9a0v4.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-8841h.md)
  Returns the dot product of two vectors.
- [simd_incircle](./simd_incircle-4k0k0.md)
  Tests whether a single-precision point lies inside, on, or outside a circle.
- [simd_normalize](./simd_normalize-9fk7c.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-9wx26.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-54cma.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-9db7k.md)
  Tests the orientation of the two supplied vectors.
- [simd_orient](./simd_orient-4pzf2.md)
  Tests the orientation of the two supplied vectors.
- [simd_orient](./simd_orient-hid7.md)
  Tests the orientation of the two supplied vectors.
- [simd_project](./simd_project-6bme3.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-6uimg.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-8f9wk.md)
  Returns the fast projected vector.
- [simd_reflect](./simd_reflect-1ot4h.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-31085.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
### Vector norm functions
- [simd_norm_one](./simd_norm_one-1108p.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-91fdw.md)
  Returns the maximum absolute value of a vector.
### Length and distance functions
- [simd_length](./simd_length-3oe9l.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-59hta.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-77xak.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-3e4zb.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-9tyar.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-7xeat.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-3fsw6.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-v9b5.md)
  Returns the square of the distance between two vectors.

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