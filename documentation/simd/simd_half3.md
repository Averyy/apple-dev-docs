# simd_half3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 16-bit floating-point elements.

## Declaration

```swift
typealias simd_half3 = SIMD3<Float16>
```

```c
typedef _Float16 __attribute__((ext_vector_type(3))) simd_half3;
```

## Topics

### Functions to create three-element vectors from other vectors
- [func simd_make_half3(simd_half2) -> simd_half3](./simd_make_half3%28_%29-52gdy.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_half3(simd_half3) -> simd_half3](./simd_make_half3%28_%29-4yz0x.md)
  Returns a new vector from the specified vector.
- [func simd_make_half3(simd_half4) -> simd_half3](./simd_make_half3%28_%29-4h0kc.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_half3(simd_half8) -> simd_half3](./simd_make_half3%28_%29-5nca0.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_half3(simd_half16) -> simd_half3](./simd_make_half3%28_%29-9063q.md)
  Returns a new vector by truncating the specified 16-element vector.
- [func simd_make_half3(simd_half32) -> simd_half3](./simd_make_half3%28_%29-64v1.md)
  Returns a new vector by truncating the specified 32-element vector.
- [func simd_make_half3_undef(simd_half2) -> simd_half3](./simd_make_half3_undef%28_%29-1frd1.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to create three-element vectors from scalar values
- [func simd_make_half3(Float16) -> simd_half3](./simd_make_half3%28_%29-9gqvo.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_half3(Float16, Float16, Float16) -> simd_half3](./simd_make_half3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_half3(simd_half2, Float16) -> simd_half3](./simd_make_half3%28_,_%29-5wwpl.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_half3(Float16, simd_half2) -> simd_half3](./simd_make_half3%28_,_%29-4svq0.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_half3_undef(Float16) -> simd_half3](./simd_make_half3_undef%28_%29-6lcqp.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common functions
- [func simd_abs(simd_half3) -> simd_half3](./simd_abs%28_%29-8derx.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_half3, simd_half3, simd_half3) -> simd_half3](./simd_clamp%28_,_,_%29-2h8ov.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_half3, simd_half3) -> simd_bool](./simd_equal%28_,_%29-9k8m9.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_half3) -> simd_half3](./simd_fract%28_%29-47quw.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_half3) -> simd_half3](./simd_sign%28_%29-6gppu.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_half3, simd_half3) -> simd_half3](./simd_step%28_,_%29-8w7e.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce functions
- [func simd_reduce_add(simd_half3) -> Float16](./simd_reduce_add%28_%29-2v3th.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_half3) -> Float16](./simd_reduce_max%28_%29-4h2m7.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_half3) -> Float16](./simd_reduce_min%28_%29-4685v.md)
  Returns the minimum value in a vector.
### Interpolation functions
- [func simd_mix(simd_half3, simd_half3, simd_half3) -> simd_half3](./simd_mix%28_,_,_%29-4co2a.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_half3, simd_half3, simd_half3) -> simd_half3](./simd_smoothstep%28_,_,_%29-4rnii.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema functions
- [func simd_max(simd_half3, simd_half3) -> simd_half3](./simd_max%28_,_%29-1g1g7.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_half3, simd_half3) -> simd_half3](./simd_min%28_,_%29-4rmyw.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and reciprocal square root functions
- [func simd_recip(simd_half3) -> simd_half3](./simd_recip%28_%29-8k0yn.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_half3) -> simd_half3](./simd_rsqrt%28_%29-rgh7.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_half3) -> simd_half3](./simd_precise_recip%28_%29-61jmz.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_half3) -> simd_half3](./simd_precise_rsqrt%28_%29-znwt.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_half3) -> simd_half3](./simd_fast_recip%28_%29-okeq.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_half3) -> simd_half3](./simd_fast_rsqrt%28_%29-80xc1.md)
  Returns the fast reciprocal square root of each element in a vector.
### Logic functions
- [func simd_select(simd_half3, simd_half3, simd_short3) -> simd_half3](./simd_select%28_,_,_%29-2ljkl.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_half3, simd_half3, simd_short3) -> simd_half3](./simd_bitselect%28_,_,_%29-6ne9u.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math functions
- [func simd_muladd(simd_half3, simd_half3, simd_half3) -> simd_half3](./simd_muladd%28_,_,_%29-582ze.md)
  Returns the multiply-add result for corresponding elements in three vectors.

## See Also

### Vector data types
- [typealias simd_half1](./simd_half1.md)
  A vector of one 16-bit floating-point element.
- [typealias simd_half2](./simd_half2.md)
  A vector of two 16-bit floating-point elements.
- [typealias simd_half4](./simd_half4.md)
  A vector of four 16-bit floating-point elements.
- [typealias simd_half8](./simd_half8.md)
  A vector of eight 16-bit floating-point elements.
- [typealias simd_half16](./simd_half16.md)
  A vector of sixteen 16-bit floating-point elements.
- [typealias simd_half32](./simd_half32.md)
  A vector of thirty-two 16-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_half3)*