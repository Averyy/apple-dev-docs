# simd_float16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixteen 32-bit floating-point elements.

## Declaration

```swift
typealias simd_float16 = SIMD16<Float>
```

```c
typedef float __attribute__((ext_vector_type(16))) simd_float16;
```

## Topics

### Functions to Create 16-Element Vectors From Other Vectors
- [func simd_make_float16(simd_float2) -> simd_float16](./simd_make_float16%28_%29-73rau.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_float16(simd_float3) -> simd_float16](./simd_make_float16%28_%29-76ned.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_float16(simd_float4) -> simd_float16](./simd_make_float16%28_%29-6v3h4.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_float16(simd_float8) -> simd_float16](./simd_make_float16%28_%29-81hjg.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_float16(simd_float16) -> simd_float16](./simd_make_float16%28_%29-5j0rl.md)
  Returns a new vector from the specified vector.
- [func simd_make_float16(simd_float8, simd_float8) -> simd_float16](./simd_make_float16%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_float16_undef(simd_float2) -> simd_float16](./simd_make_float16_undef%28_%29-3f8p6.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_float16_undef(simd_float3) -> simd_float16](./simd_make_float16_undef%28_%29-3bslp.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_float16_undef(simd_float4) -> simd_float16](./simd_make_float16_undef%28_%29-38xrw.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_float16_undef(simd_float8) -> simd_float16](./simd_make_float16_undef%28_%29-4f6xc.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [vector16](./vector16-8kycm.md)
  Returns a new vector from the specified vectors.
### Functions to Create 16-Element Vectors From Scalar Values
- [func simd_make_float16(Float) -> simd_float16](./simd_make_float16%28_%29-4r3a8.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_float16_undef(Float) -> simd_float16](./simd_make_float16_undef%28_%29-71tt7.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Alternative Type Alias
- [typealias vector_float16](./vector_float16.md)
### Common Functions
- [func simd_abs(simd_float16) -> simd_float16](./simd_abs%28_%29-47h6g.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float16, simd_float16, simd_float16) -> simd_float16](./simd_clamp%28_,_,_%29-92son.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_float16, simd_float16) -> simd_bool](./simd_equal%28_,_%29-376kl.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_float16) -> simd_float16](./simd_fract%28_%29-6v1ix.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_float16) -> simd_float16](./simd_sign%28_%29-tc2v.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float16, simd_float16) -> simd_float16](./simd_step%28_,_%29-14cn0.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_min(simd_float16) -> Float](./simd_reduce_min%28_%29-3d29t.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_float16) -> Float](./simd_reduce_max%28_%29-8iok7.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_float16) -> Float](./simd_reduce_add%28_%29-7n310.md)
  Returns the sum of all elements in a vector.
### Interpolation Functions
- [func simd_smoothstep(simd_float16, simd_float16, simd_float16) -> simd_float16](./simd_smoothstep%28_,_,_%29-2q68m.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func simd_mix(simd_float16, simd_float16, simd_float16) -> simd_float16](./simd_mix%28_,_,_%29-1hgrq.md)
  Returns an element-wise linearly interpolated value between two vectors.
### Extrema Functions
- [func simd_min(simd_float16, simd_float16) -> simd_float16](./simd_min%28_,_%29-6clj9.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_float16, simd_float16) -> simd_float16](./simd_max%28_,_%29-90s23.md)
  Returns the maximum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func simd_recip(simd_float16) -> simd_float16](./simd_recip%28_%29-5bwdz.md)
  Returns the reciprocal of each element in a vector.
- [func simd_fast_recip(simd_float16) -> simd_float16](./simd_fast_recip%28_%29-mza9.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_precise_recip(simd_float16) -> simd_float16](./simd_precise_recip%28_%29-5ic8t.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_rsqrt(simd_float16) -> simd_float16](./simd_rsqrt%28_%29-76a19.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_fast_rsqrt(simd_float16) -> simd_float16](./simd_fast_rsqrt%28_%29-6862g.md)
  Returns the fast reciprocal square root of each element in a vector.
- [func simd_precise_rsqrt(simd_float16) -> simd_float16](./simd_precise_rsqrt%28_%29-6j35f.md)
  Returns the precise reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_float16) -> simd_float16](./exp%28_%29-2ru57.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_float16) -> simd_float16](./exp2%28_%29-271hg.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_float16) -> simd_float16](./exp10%28_%29-165iq.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_float16) -> simd_float16](./expm1%28_%29-90g3j.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_float16) -> simd_float16](./log%28_%29-44j3q.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_float16) -> simd_float16](./log2%28_%29-8nusk.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_float16) -> simd_float16](./log10%28_%29-7eq4p.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_float16) -> simd_float16](./log1p%28_%29-2uw4e.md)
  Returns *log(1+x)* of each element in a vector.
### Hyperbolic Functions
- [func acosh(simd_float16) -> simd_float16](./acosh%28_%29-4w84k.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_float16) -> simd_float16](./asinh%28_%29-6v4m.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_float16) -> simd_float16](./atanh%28_%29-70pvm.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_float16) -> simd_float16](./cosh%28_%29-9kvzr.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_float16) -> simd_float16](./sinh%28_%29-1d6si.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_float16) -> simd_float16](./tanh%28_%29-7sto5.md)
  Returns the hyperbolic tangent of each element in a vector.
### Logic Functions
- [func simd_select(simd_float16, simd_float16, simd_int16) -> simd_float16](./simd_select%28_,_,_%29-41fgt.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_float16, simd_float16, simd_int16) -> simd_float16](./simd_bitselect%28_,_,_%29-wjqf.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_float16) -> simd_float16](./cbrt%28_%29-3cnri.md)
  Returns the cube root of each element in a vector.
- [func erf(simd_float16) -> simd_float16](./erf%28_%29-7wkg3.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_float16) -> simd_float16](./erfc%28_%29-20vsh.md)
  Returns the complementary error function for each element in a vector.
- [func fma(simd_float16, simd_float16, simd_float16) -> simd_float16](./fma%28_,_,_%29-503dp.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_float16, simd_float16) -> simd_float16](./fmod%28_,_%29-2bys0.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_float16, simd_float16) -> simd_float16](./hypot%28_,_%29-265pt.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_float16) -> simd_float16](./lgamma%28_%29-1onkc.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_float16, simd_float16) -> simd_float16](./nextafter%28_,_%29-9kvo8.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_float16, simd_float16) -> simd_float16](./pow%28_,_%29-7mpyc.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_float16, simd_float16) -> simd_float16](./remainder%28_,_%29-5dxqm.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_float16) -> simd_float16](./round%28_%29-74w3c.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_float16, simd_float16, simd_float16) -> simd_float16](./simd_muladd%28_,_,_%29-8imv2.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_float16) -> simd_float16](./tgamma%28_%29-9r61k.md)
  Returns the gamma function for each element in a vector.
### Trigonometric Functions
- [func acos(simd_float16) -> simd_float16](./acos%28_%29-9k95t.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_float16) -> simd_float16](./asin%28_%29-52bly.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_float16) -> simd_float16](./atan%28_%29-7y100.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_float16, simd_float16) -> simd_float16](./atan2%28_,_%29-5dweo.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_float16) -> simd_float16](./cos%28_%29-40gvn.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_float16) -> simd_float16](./cospi%28_%29-7kfdh.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_float16) -> simd_float16](./sin%28_%29-7e17y.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_float16) -> simd_float16](./sinpi%28_%29-6d2hq.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_float16) -> (sin: simd_float16, cos: simd_float16)](./sincos%28_%29-go67.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_float16) -> (sin: simd_float16, cos: simd_float16)](./sincospi%28_%29-h3av.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_float16) -> simd_float16](./tan%28_%29-5q9ad.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_float16) -> simd_float16](./tanpi%28_%29-2vht8.md)
  Returns the tangent of each element in a vector multiplied by pi.
### Classification Functions
- [func isfinite(simd_float16) -> simd_int16](./isfinite%28_%29-8bt9t.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_float16) -> simd_int16](./isinf%28_%29-77t4f.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_float16) -> simd_int16](./isnan%28_%29-3ek5k.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_float16) -> simd_int16](./isnormal%28_%29-86aj9.md)
  Returns true for each element that is normal in a vector.
### Functions to Create 16-Element Vectors From Vectors of Other Types
- [simd_float](./simd_float-33quw.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_float](./simd_float-33h14.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_float](./simd_float-33lyw.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_float](./simd_float-33bqw.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_float](./simd_float-33os8.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_float](./simd_float-33eyg.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_float](./simd_float-33i8s.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
### Geometry Functions
- [simd_dot](./simd_dot-z7ab.md)
  Returns the dot product of two vectors.
- [simd_project](./simd_project-4ofki.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-4kt3u.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-39090.md)
  Returns the precise projected vector.
- [simd_normalize](./simd_normalize-3r4t9.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-fjva.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-53f8a.md)
  Returns the precise normalized vector.
### Vector Norm Functions
- [simd_norm_one](./simd_norm_one-2dgnq.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-2x7vw.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [simd_length](./simd_length-575we.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-3edeo.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-bswz.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-7moqe.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-7xk9e.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-56een.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-5ci0y.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-57ui2.md)
  Returns the square of the distance between two vectors.

## See Also

### Vector data types
- [typealias simd_float1](./simd_float1.md)
  A vector of one 32-bit floating-point element.
- [typealias simd_float2](./simd_float2.md)
  A vector of two 32-bit floating-point elements.
- [typealias simd_float3](./simd_float3.md)
  A vector of three 32-bit floating-point elements.
- [typealias simd_float4](./simd_float4.md)
  A vector of four 32-bit floating-point elements.
- [typealias simd_float8](./simd_float8.md)
  A vector of eight 32-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float16)*