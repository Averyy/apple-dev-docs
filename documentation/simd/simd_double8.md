# simd_double8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 64-bit floating-point elements.

## Declaration

```swift
typealias simd_double8 = SIMD8<Double>
```

```c
typedef double __attribute__((ext_vector_type(8))) simd_double8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_double8(simd_double2) -> simd_double8](./simd_make_double8%28_%29-3wn9q.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_double8(simd_double3) -> simd_double8](./simd_make_double8%28_%29-40259.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_double8(simd_double4) -> simd_double8](./simd_make_double8%28_%29-3br50.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_double8(simd_double8) -> simd_double8](./simd_make_double8%28_%29-4i0aw.md)
  Returns a new vector from the specified vector.
- [func simd_make_double8(simd_double4, simd_double4) -> simd_double8](./simd_make_double8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_double8_undef(simd_double2) -> simd_double8](./simd_make_double8_undef%28_%29-7g0z0.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_double8_undef(simd_double3) -> simd_double8](./simd_make_double8_undef%28_%29-7d127.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_double8_undef(simd_double4) -> simd_double8](./simd_make_double8_undef%28_%29-7md0u.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_double8(Double) -> simd_double8](./simd_make_double8%28_%29-56g8y.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_double8_undef(Double) -> simd_double8](./simd_make_double8_undef%28_%29-5rmk5.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_double8) -> simd_double8](./simd_abs%28_%29-7p0dw.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_double8, simd_double8, simd_double8) -> simd_double8](./simd_clamp%28_,_,_%29-q88m.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_double8, simd_double8) -> simd_bool](./simd_equal%28_,_%29-8pk1m.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_double8) -> simd_double8](./simd_fract%28_%29-3jcfd.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_double8) -> simd_double8](./simd_sign%28_%29-7hb8r.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_double8, simd_double8) -> simd_double8](./simd_step%28_,_%29-1vckv.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_min(simd_double8) -> Double](./simd_reduce_min%28_%29-3ode2.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_double8) -> Double](./simd_reduce_max%28_%29-55eqq.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_double8) -> Double](./simd_reduce_add%28_%29-3aymg.md)
  Returns the sum of all elements in a vector.
### Interpolation Functions
- [func simd_smoothstep(simd_double8, simd_double8, simd_double8) -> simd_double8](./simd_smoothstep%28_,_,_%29-99l4q.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func simd_mix(simd_double8, simd_double8, simd_double8) -> simd_double8](./simd_mix%28_,_,_%29-5afwd.md)
  Returns an element-wise linearly interpolated value between two vectors.
### Extrema Functions
- [func simd_min(simd_double8, simd_double8) -> simd_double8](./simd_min%28_,_%29-6beor.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_double8, simd_double8) -> simd_double8](./simd_max%28_,_%29-65po6.md)
  Returns the maximum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func simd_recip(simd_double8) -> simd_double8](./simd_recip%28_%29-98afu.md)
  Returns the reciprocal of each element in a vector.
- [func simd_fast_recip(simd_double8) -> simd_double8](./simd_fast_recip%28_%29-16f97.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_precise_recip(simd_double8) -> simd_double8](./simd_precise_recip%28_%29-74cqq.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_rsqrt(simd_double8) -> simd_double8](./simd_rsqrt%28_%29-1ojpy.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_fast_rsqrt(simd_double8) -> simd_double8](./simd_fast_rsqrt%28_%29-922us.md)
  Returns the fast reciprocal square root of each element in a vector.
- [func simd_precise_rsqrt(simd_double8) -> simd_double8](./simd_precise_rsqrt%28_%29-1hq00.md)
  Returns the precise reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_double8) -> simd_double8](./exp%28_%29-69tin.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_double8) -> simd_double8](./exp2%28_%29-4m3mb.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_double8) -> simd_double8](./exp10%28_%29-39f7r.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_double8) -> simd_double8](./expm1%28_%29-8nn5x.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_double8) -> simd_double8](./log%28_%29-7649l.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_double8) -> simd_double8](./log2%28_%29-8k8nf.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_double8) -> simd_double8](./log10%28_%29-24ung.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_double8) -> simd_double8](./log1p%28_%29-3fdfb.md)
  Returns *log(1+x)* of each element in a vector.
### Hyperbolic Functions
- [func acosh(simd_double8) -> simd_double8](./acosh%28_%29-2zf9d.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_double8) -> simd_double8](./asinh%28_%29-5vu4r.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_double8) -> simd_double8](./atanh%28_%29-d3b3.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_double8) -> simd_double8](./cosh%28_%29-1g57o.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_double8) -> simd_double8](./sinh%28_%29-ip9w.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_double8) -> simd_double8](./tanh%28_%29-1ag6z.md)
  Returns the hyperbolic tangent of each element in a vector.
### Logic Functions
- [func simd_select(simd_double8, simd_double8, simd_long8) -> simd_double8](./simd_select%28_,_,_%29-8wti7.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_double8, simd_double8, simd_long8) -> simd_double8](./simd_bitselect%28_,_,_%29-1yj5q.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_double8) -> simd_double8](./cbrt%28_%29-9dsjc.md)
  Returns the cube root of each element in a vector.
- [func erf(simd_double8) -> simd_double8](./erf%28_%29-293ey.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_double8) -> simd_double8](./erfc%28_%29-vzkw.md)
  Returns the complementary error function for each element in a vector.
- [func fma(simd_double8, simd_double8, simd_double8) -> simd_double8](./fma%28_,_,_%29-95vfo.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_double8, simd_double8) -> simd_double8](./fmod%28_,_%29-7g7m.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_double8, simd_double8) -> simd_double8](./hypot%28_,_%29-8vke8.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_double8) -> simd_double8](./lgamma%28_%29-7t6g8.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_double8, simd_double8) -> simd_double8](./nextafter%28_,_%29-2xerr.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_double8, simd_double8) -> simd_double8](./pow%28_,_%29-9xmzf.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_double8, simd_double8) -> simd_double8](./remainder%28_,_%29-326ci.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_double8) -> simd_double8](./round%28_%29-7t6q.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_double8, simd_double8, simd_double8) -> simd_double8](./simd_muladd%28_,_,_%29-2vs0c.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_double8) -> simd_double8](./tgamma%28_%29-8qiri.md)
  Returns the gamma function for each element in a vector.
### Trigonometric Functions
- [func acos(simd_double8) -> simd_double8](./acos%28_%29-2141m.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_double8) -> simd_double8](./asin%28_%29-78d03.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_double8) -> simd_double8](./atan%28_%29-7b52p.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_double8, simd_double8) -> simd_double8](./atan2%28_,_%29-8pfg9.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_double8) -> simd_double8](./cos%28_%29-7bqey.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_double8) -> simd_double8](./cospi%28_%29-8d55q.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_double8) -> simd_double8](./sin%28_%29-1joh9.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_double8) -> simd_double8](./sinpi%28_%29-9tdix.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_double8) -> (sin: simd_double8, cos: simd_double8)](./sincos%28_%29-3iwed.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_double8) -> (sin: simd_double8, cos: simd_double8)](./sincospi%28_%29-5yfry.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_double8) -> simd_double8](./tan%28_%29-7a2xj.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_double8) -> simd_double8](./tanpi%28_%29-3lobh.md)
  Returns the tangent of each element in a vector multiplied by pi.
### Classification Functions
- [func isfinite(simd_double8) -> simd_long8](./isfinite%28_%29-9iwij.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_double8) -> simd_long8](./isinf%28_%29-5i1uj.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_double8) -> simd_long8](./isnan%28_%29-90lcg.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_double8) -> simd_long8](./isnormal%28_%29-7lk2x.md)
  Returns true for each element that is normal in a vector.
### Alternative Type Alias
- [typealias vector_double8](./vector_double8.md)
### Functions to Create Eight-Element Vectors From Vectors of Other Types
- [simd_double](./simd_double-62zne.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_double](./simd_double-639kq.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_double](./simd_double-634oq.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_double](./simd_double-63eii.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_double](./simd_double-631ha.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_double](./simd_double-63bi6.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_double](./simd_double-63332.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_double](./simd_double-63d26.md)
  Returns a new vector from the specified vector of 64-bit, unsigned-integer elements.
- [simd_double](./simd_double-63b6q.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_double](./simd_double-63agu.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Geometry Functions
- [simd_dot](./simd_dot-5vlda.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-yjr.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-8x3pc.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-6237w.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-8o56y.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-61mm1.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-2x3bb.md)
  Returns the precise projected vector.
### Vector Norm Functions
- [simd_norm_one](./simd_norm_one-fgqf.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-9maca.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [simd_length](./simd_length-32x7b.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-5utvc.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-67k0i.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-3x9ip.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-8f8o.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-9mi5e.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-82p17.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-4kl6l.md)
  Returns the square of the distance between two vectors.

## See Also

### Vector data types
- [typealias simd_double1](./simd_double1.md)
  A vector of one 64-bit floating-point element.
- [typealias simd_double2](./simd_double2.md)
  A vector of two 64-bit floating-point elements.
- [typealias simd_double3](./simd_double3.md)
  A vector of three 64-bit floating-point elements.
- [typealias simd_double4](./simd_double4.md)
  A vector of four 64-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double8)*