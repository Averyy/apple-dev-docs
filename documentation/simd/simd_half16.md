# simd_half16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixteen 16-bit floating-point elements.

## Declaration

```swift
typealias simd_half16 = SIMD16<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(16))) simd_half16;
```

## Topics

### Functions to create 16-element vectors from other vectors
- [func simd_make_half16(simd_half2) -> simd_half16](./simd_make_half16%28_%29-7jegv.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_half16(simd_half3) -> simd_half16](./simd_make_half16%28_%29-7fwvg.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_half16(simd_half4) -> simd_half16](./simd_make_half16%28_%29-7czq5.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_half16(simd_half8) -> simd_half16](./simd_make_half16%28_%29-8jb49.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_half16(simd_half16) -> simd_half16](./simd_make_half16%28_%29-2eeq3.md)
  Returns a new vector from the specified vector.
- [func simd_make_half16(simd_half32) -> simd_half16](./simd_make_half16%28_%29-18zo3.md)
  Returns a new vector by truncating the specified 32-element vector.
- [func simd_make_half16_undef(simd_half2) -> simd_half16](./simd_make_half16_undef%28_%29-nn1z.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_half16_undef(simd_half3) -> simd_half16](./simd_make_half16_undef%28_%29-qkco.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_half16_undef(simd_half4) -> simd_half16](./simd_make_half16_undef%28_%29-hd79.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_half16_undef(simd_half8) -> simd_half16](./simd_make_half16_undef%28_%29-1lcb5.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
- [func simd_make_half16(simd_half8, simd_half8) -> simd_half16](./simd_make_half16%28_,_%29.md)
  Returns a new vector from the specified vectors.
### Functions to create 16-element vectors from scalar values
- [func simd_make_half16(Float16) -> simd_half16](./simd_make_half16%28_%29-923w5.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_half16_undef(Float16) -> simd_half16](./simd_make_half16_undef%28_%29-5x8m.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common functions
- [func simd_abs(simd_half16) -> simd_half16](./simd_abs%28_%29-47hrc.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_int16, simd_int16, simd_int16) -> simd_int16](./simd_clamp%28_,_,_%29-5xcny.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half16, simd_half16) -> simd_bool](./simd_equal%28_,_%29-9ijsx.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half16) -> simd_half16](./simd_fract%28_%29-6v27d.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half16) -> simd_half16](./simd_sign%28_%29-tcn7.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half16, simd_half16) -> simd_half16](./simd_step%28_,_%29-7ryeb.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce functions
- [func simd_reduce_add(simd_half16) -> Float16](./simd_reduce_add%28_%29-7n2m4.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_half16) -> Float16](./simd_reduce_max%28_%29-8iq8z.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_half16) -> Float16](./simd_reduce_min%28_%29-3cxx5.md)
  Returns the minimum value in a vector.
### Interpolation functions
- [func simd_mix(simd_half16, simd_half16, simd_half16) -> simd_half16](./simd_mix%28_,_,_%29-7hbla.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_half16, simd_half16, simd_half16) -> simd_half16](./simd_smoothstep%28_,_,_%29-4twuq.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema functions
- [func simd_max(simd_half16, simd_half16) -> simd_half16](./simd_max%28_,_%29-9p9g1.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_half16, simd_half16) -> simd_half16](./simd_min%28_,_%29-4gxfx.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and reciprocal square root functions
- [func simd_recip(simd_half16) -> simd_half16](./simd_recip%28_%29-5bvrv.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_half16) -> simd_half16](./simd_rsqrt%28_%29-765rp.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_half16) -> simd_half16](./simd_precise_recip%28_%29-5icut.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_half16) -> simd_half16](./simd_precise_rsqrt%28_%29-6j2jj.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_half16) -> simd_half16](./simd_fast_recip%28_%29-mw6p.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_half16) -> simd_half16](./simd_fast_rsqrt%28_%29-686mo.md)
  Returns the fast reciprocal square root of each element in a vector.
### Logic functions
- [func simd_select(simd_half16, simd_half16, simd_short16) -> simd_half16](./simd_select%28_,_,_%29-7d7xj.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_half16, simd_half16, simd_short16) -> simd_half16](./simd_bitselect%28_,_,_%29-92kfc.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math functions
- [func simd_muladd(simd_half16, simd_half16, simd_half16) -> simd_half16](./simd_muladd%28_,_,_%29-8bkab.md)
  Returns the multiply-add result for corresponding elements in three vectors.
### Functions to create 16-element vectors from vectors of other types
- [simd_half](./simd_half-227sx.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_half](./simd_half-21y0x.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_half](./simd_half-22cyp.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_half](./simd_half-222xt.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_half](./simd_half-229ux.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_half](./simd_half-21zqh.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_half](./simd_half-21zmj.md)
  Returns a new vector from the specified vector of 16-bit, floating-point elements.
- [simd_half](./simd_half-21z2n.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
### Geometry functions
- [simd_dot](./simd_dot-8gymo.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-3r6p1.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-fo8a.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-53d5a.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-4n2u6.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-7slej.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-95iib.md)
  Returns the fast projected vector.
### Vector norm functions
- [simd_norm_one](./simd_norm_one-2djve.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-2x7b8.md)
  Returns the maximum absolute value of a vector.
### Length and distance functions
- [simd_length](./simd_length-576ia.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-3ecug.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-bxb3.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-7mlpe.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-2dror.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-1pqse.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-wp3e.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-m1wr.md)
  Returns the square of the distance between two vectors.

## See Also

### Vector data types
- [typealias simd_half1](./simd_half1.md)
  A vector of one 16-bit floating-point element.
- [typealias simd_half2](./simd_half2.md)
  A vector of two 16-bit floating-point elements.
- [typealias simd_half3](./simd_half3.md)
  A vector of three 16-bit floating-point elements.
- [typealias simd_half4](./simd_half4.md)
  A vector of four 16-bit floating-point elements.
- [typealias simd_half8](./simd_half8.md)
  A vector of eight 16-bit floating-point elements.
- [typealias simd_half32](./simd_half32.md)
  A vector of thirty-two 16-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half16)*