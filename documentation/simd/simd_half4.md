# simd_half4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 16-bit floating-point elements.

## Declaration

```swift
typealias simd_half4 = SIMD4<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(4))) simd_half4;
```

## Topics

### Functions to create four-element vectors from other vectors
- [func simd_make_half4(simd_half2) -> simd_half4](./simd_make_half4%28_%29-fx5r.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_half4(simd_half3) -> simd_half4](./simd_make_half4%28_%29-iuj0.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_half4(simd_half4) -> simd_half4](./simd_make_half4%28_%29-9u2ra.md)
  Returns a new vector from the specified vector.
- [func simd_make_half4(simd_half8) -> simd_half4](./simd_make_half4%28_%29-10t2p.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_half4(simd_half16) -> simd_half4](./simd_make_half4%28_%29-43737.md)
  Returns a new vector by truncating the specified 16-element vector.
- [func simd_make_half4(simd_half32) -> simd_half4](./simd_make_half4%28_%29-60ltf.md)
  Returns a new vector by truncating the specified 32-element vector.
- [func simd_make_half4(simd_half2, simd_half2) -> simd_half4](./simd_make_half4%28_,_%29-2ea2z.md)
  Returns a new vector from the specified vectors.
- [func simd_make_half4_undef(simd_half2) -> simd_half4](./simd_make_half4_undef%28_%29-16ipv.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_half4_undef(simd_half3) -> simd_half4](./simd_make_half4_undef%28_%29-136jo.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
### Functions to create four-element vectors from scalar values
- [func simd_make_half4(Float16) -> simd_half4](./simd_make_half4%28_%29-6lkh9.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_half4(Float16, Float16, Float16, Float16) -> simd_half4](./simd_make_half4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_half4_undef(Float16) -> simd_half4](./simd_make_half4_undef%28_%29-4axzi.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [func simd_make_half4(Float16, simd_half3) -> simd_half4](./simd_make_half4%28_,_%29-2n13g.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_half4(simd_half3, Float16) -> simd_half4](./simd_make_half4%28_,_%29-6uygn.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_half4(Float16, simd_half2, Float16) -> simd_half4](./simd_make_half4%28_,_,_%29-43wuv.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_half4(Float16, Float16, simd_half2) -> simd_half4](./simd_make_half4%28_,_,_%29-74ybg.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_half4(simd_half2, Float16, Float16) -> simd_half4](./simd_make_half4%28_,_,_%29-6g0kb.md)
  Returns a new vector from a vector and scalar values.
### Common functions
- [func simd_abs(simd_half4) -> simd_half4](./simd_abs%28_%29-81q3k.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_half4, simd_half4, simd_half4) -> simd_half4](./simd_clamp%28_,_,_%29-2vvpa.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half4, simd_half4) -> simd_bool](./simd_equal%28_,_%29-6nuuw.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half4) -> simd_half4](./simd_fract%28_%29-3w251.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half4) -> simd_half4](./simd_sign%28_%29-7533b.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half4, simd_half4) -> simd_half4](./simd_step%28_,_%29-4knqw.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce functions
- [func simd_reduce_add(simd_half4) -> Float16](./simd_reduce_add%28_%29-2ylck.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_half4) -> Float16](./simd_reduce_max%28_%29-4qtu6.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_half4) -> Float16](./simd_reduce_min%28_%29-4ulc6.md)
  Returns the minimum value in a vector.
### Interpolation functions
- [func simd_mix(simd_half4, simd_half4, simd_half4) -> simd_half4](./simd_mix%28_,_,_%29-4uou1.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_half4, simd_half4, simd_half4) -> simd_half4](./simd_smoothstep%28_,_,_%29-7gsfq.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema functions
- [func simd_max(simd_half4, simd_half4) -> simd_half4](./simd_max%28_,_%29-64l5l.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_half4, simd_half4) -> simd_half4](./simd_min%28_,_%29-1ep1a.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and reciprocal square root functions
- [func simd_recip(simd_half4) -> simd_half4](./simd_recip%28_%29-822hi.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_half4) -> simd_half4](./simd_rsqrt%28_%29-i99u.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_half4) -> simd_half4](./simd_precise_recip%28_%29-6pwwe.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_half4) -> simd_half4](./simd_precise_rsqrt%28_%29-13530.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_half4) -> simd_half4](./simd_fast_recip%28_%29-7d3.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_half4) -> simd_half4](./simd_fast_rsqrt%28_%29-8pakw.md)
  Returns the fast reciprocal square root of each element in a vector.
### Logic functions
- [func simd_select(simd_half4, simd_half4, simd_short4) -> simd_half4](./simd_select%28_,_,_%29-4vjt.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_half4, simd_half4, simd_short4) -> simd_half4](./simd_bitselect%28_,_,_%29-6gy8u.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math functions
- [func simd_muladd(simd_half4, simd_half4, simd_half4) -> simd_half4](./simd_muladd%28_,_,_%29-99g6r.md)
  Returns the multiply-add result for corresponding elements in three vectors.
### Functions to create four-element vectors from vectors of other types
- [simd_half](./simd_half-3g8pd.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_half](./simd_half-3fyxd.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_half](./simd_half-3g3td.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_half](./simd_half-3fu1d.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_half](./simd_half-3gau9.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_half](./simd_half-3g0m9.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_half](./simd_half-3g9t7.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_half](./simd_half-3fzzf.md)
  Returns a new vector from the specified vector of 64-bit, unsigned-integer elements.
- [simd_half](./simd_half-3g13n.md)
  Returns a new vector from the specified vector of 16-bit, floating-point elements.
- [simd_half](./simd_half-3fxvr.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_half](./simd_half-3fxbf.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Geometry functions
- [simd_dot](./simd_dot-87ssc.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9o6iq.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-3vaz.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-4vqaw.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-24ld6.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-1cw2i.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-6ymj6.md)
  Returns the fast projected vector.
- [simd_reflect](./simd_reflect-9r760.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-6q75f.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
### Vector norm functions
- [simd_norm_one](./simd_norm_one-sdw3.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-97p52.md)
  Returns the maximum absolute value of a vector.
### Length and distance functions
- [simd_length](./simd_length-3fmwz.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-4om0k.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-7dx4e.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-2t92l.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-9tmum.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-7jdgd.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-3g45n.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-1uyo7.md)
  Returns the square of the distance between two vectors.

## See Also

### Vector data types
- [typealias simd_half1](./simd_half1.md)
  A vector of one 16-bit floating-point element.
- [typealias simd_half2](./simd_half2.md)
  A vector of two 16-bit floating-point elements.
- [typealias simd_half3](./simd_half3.md)
  A vector of three 16-bit floating-point elements.
- [typealias simd_half8](./simd_half8.md)
  A vector of eight 16-bit floating-point elements.
- [typealias simd_half16](./simd_half16.md)
  A vector of sixteen 16-bit floating-point elements.
- [typealias simd_half32](./simd_half32.md)
  A vector of thirty-two 16-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half4)*