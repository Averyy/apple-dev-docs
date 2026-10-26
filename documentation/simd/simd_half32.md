# simd_half32

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of thirty-two 16-bit floating-point elements.

## Declaration

```swift
typealias simd_half32 = SIMD32<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(32))) simd_half32;
```

## Topics

### Functions to create 32-element vectors from other vectors
- [func simd_make_half32(simd_half2) -> simd_half32](./simd_make_half32%28_%29-8obpe.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_half32(simd_half3) -> simd_half32](./simd_make_half32%28_%29-8kum5.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_half32(simd_half4) -> simd_half32](./simd_make_half32%28_%29-82w1c.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_half32(simd_half8) -> simd_half32](./simd_make_half32%28_%29-997h0.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_half32(simd_half16) -> simd_half32](./simd_make_half32%28_%29-6xe53.md)
  Returns a new vector from the specified 16-element vector, and other elements set to zero.
- [func simd_make_half32(simd_half32) -> simd_half32](./simd_make_half32%28_%29-80qof.md)
  Returns a new vector from the specified vector.
- [func simd_make_half32_undef(simd_half2) -> simd_half32](./simd_make_half32_undef%28_%29-3w7jb.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_half32_undef(simd_half3) -> simd_half32](./simd_make_half32_undef%28_%29-3yzwk.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_half32_undef(simd_half4) -> simd_half32](./simd_make_half32_undef%28_%29-42h8l.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_half32_undef(simd_half8) -> simd_half32](./simd_make_half32_undef%28_%29-4gyi9.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
- [func simd_make_half32_undef(simd_half16) -> simd_half32](./simd_make_half32_undef%28_%29-9hc0w.md)
  Returns a new vector from the specified 16-element vector, and other elements undefined.
- [func simd_make_half32(simd_half16, simd_half16) -> simd_half32](./simd_make_half32%28_,_%29.md)
  Returns a new vector from the specified vectors.
### Functions to create 32-element vectors from scalar values
- [func simd_make_half32(Float16) -> simd_half32](./simd_make_half32%28_%29-4hl1s.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_half32_undef(Float16) -> simd_half32](./simd_make_half32_undef%28_%29-65xeg.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common functions
- [func simd_abs(simd_half32) -> simd_half32](./simd_abs%28_%29-2byol.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_half32, simd_half32, simd_half32) -> simd_half32](./simd_clamp%28_,_,_%29-868pk.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half32, simd_half32) -> simd_bool](./simd_equal%28_,_%29-5620v.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half32) -> simd_half32](./simd_fract%28_%29-4zj0y.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half32) -> simd_half32](./simd_sign%28_%29-9r24j.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half32, simd_half32) -> simd_half32](./simd_step%28_,_%29-2kbac.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce functions
- [func simd_reduce_add(simd_half32) -> Float16](./simd_reduce_add%28_%29-1urk1.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_half32) -> Float16](./simd_reduce_max%28_%29-9itok.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_half32) -> Float16](./simd_reduce_min%28_%29-2b1zw.md)
  Returns the minimum value in a vector.
### Interpolation functions
- [func simd_mix(simd_half32, simd_half32, simd_half32) -> simd_half32](./simd_mix%28_,_,_%29-4qwly.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_half32, simd_half32, simd_half32) -> simd_half32](./simd_smoothstep%28_,_,_%29-6nnf0.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema functions
- [func simd_max(simd_half32, simd_half32) -> simd_half32](./simd_max%28_,_%29-2y7nk.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_half32, simd_half32) -> simd_half32](./simd_min%28_,_%29-10jj2.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and reciprocal square root functions
- [func simd_recip(simd_half32) -> simd_half32](./simd_recip%28_%29-6hfwj.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_half32) -> simd_half32](./simd_rsqrt%28_%29-60bll.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_half32) -> simd_half32](./simd_precise_recip%28_%29-22hxl.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_half32) -> simd_half32](./simd_precise_rsqrt%28_%29-8ce7i.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_half32) -> simd_half32](./simd_fast_recip%28_%29-2i3al.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_half32) -> simd_half32](./simd_fast_rsqrt%28_%29-2sbqs.md)
  Returns the fast reciprocal square root of each element in a vector.
### Logic functions
- [func simd_select(simd_half32, simd_half32, simd_short32) -> simd_half32](./simd_select%28_,_,_%29-63scw.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_half32, simd_half32, simd_short32) -> simd_half32](./simd_bitselect%28_,_,_%29-81xk8.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math functions
- [func simd_muladd(simd_half32, simd_half32, simd_half32) -> simd_half32](./simd_muladd%28_,_,_%29-bf1p.md)
  Returns the multiply-add result for corresponding elements in three vectors.
### Geometry functions
- [simd_dot](./simd_dot-14m5i.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-4thje.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-1kyde.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-3zlx2.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-40ksg.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-8q7gz.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-56rgk.md)
  Returns the fast projected vector.
### Vector norm functions
- [simd_norm_one](./simd_norm_one-jtbh.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-74hug.md)
  Returns the maximum absolute value of a vector.
### Length and distance functions
- [simd_length](./simd_length-zvvu.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-4jwws.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-916dp.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-9h8sy.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-5389o.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-5ufke.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-3ed89.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-6xb9g.md)
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
- [typealias simd_half16](./simd_half16.md)
  A vector of sixteen 16-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half32)*