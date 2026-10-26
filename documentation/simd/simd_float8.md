# simd_float8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 32-bit floating-point elements.

## Declaration

```swift
typealias simd_float8 = SIMD8<Float>
```

```c
typedef float __attribute__((ext_vector_type(8))) simd_float8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_float8(simd_float2) -> simd_float8](./simd_make_float8%28_%29-9l23p.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_float8(simd_float3) -> simd_float8](./simd_make_float8%28_%29-9i5x2.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_float8(simd_float4) -> simd_float8](./simd_make_float8%28_%29-6v9s.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_float8(simd_float8) -> simd_float8](./simd_make_float8%28_%29-907gf.md)
  Returns a new vector from the specified vector.
- [func simd_make_float8(simd_float16) -> simd_float8](./simd_make_float8%28_%29-9z6aw.md)
  Returns a new vector by truncating the specified 16-element vector.
- [func simd_make_float8(simd_float4, simd_float4) -> simd_float8](./simd_make_float8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_float8_undef(simd_float2) -> simd_float8](./simd_make_float8_undef%28_%29-9njgo.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_float8_undef(simd_float3) -> simd_float8](./simd_make_float8_undef%28_%29-9qfif.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_float8_undef(simd_float4) -> simd_float8](./simd_make_float8_undef%28_%29-8sol.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [vector8](./vector8-9dpo5.md)
  Returns a new vector from the specified vectors.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_float8(Float) -> simd_float8](./simd_make_float8%28_%29-6hx2j.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_float8_undef(Float) -> simd_float8](./simd_make_float8_undef%28_%29-8cuk5.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_float8) -> simd_float8](./simd_abs%28_%29-7ozws.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float8, simd_float8, simd_float8) -> simd_float8](./simd_clamp%28_,_,_%29-14mzm.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_float8, simd_float8) -> simd_bool](./simd_equal%28_,_%29-7of37.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_float8) -> simd_float8](./simd_fract%28_%29-3jbrt.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_float8) -> simd_float8](./simd_sign%28_%29-7hbzz.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float8, simd_float8) -> simd_float8](./simd_step%28_,_%29-96e50.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_min(simd_float8) -> Float](./simd_reduce_min%28_%29-3odum.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_float8) -> Float](./simd_reduce_max%28_%29-55e32.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_float8) -> Float](./simd_reduce_add%28_%29-3az3s.md)
  Returns the sum of all elements in a vector.
### Interpolation Functions
- [func simd_smoothstep(simd_float8, simd_float8, simd_float8) -> simd_float8](./simd_smoothstep%28_,_,_%29-845yk.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func simd_mix(simd_float8, simd_float8, simd_float8) -> simd_float8](./simd_mix%28_,_,_%29-4c4kn.md)
  Returns an element-wise linearly interpolated value between two vectors.
### Extrema Functions
- [func simd_min(simd_float8, simd_float8) -> simd_float8](./simd_min%28_,_%29-7n539.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_float8, simd_float8) -> simd_float8](./simd_max%28_,_%29-6m7z0.md)
  Returns the maximum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func simd_recip(simd_float8) -> simd_float8](./simd_recip%28_%29-989se.md)
  Returns the reciprocal of each element in a vector.
- [func simd_fast_recip(simd_float8) -> simd_float8](./simd_fast_recip%28_%29-16fz3.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_precise_recip(simd_float8) -> simd_float8](./simd_precise_recip%28_%29-74deu.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_rsqrt(simd_float8) -> simd_float8](./simd_rsqrt%28_%29-1oj3u.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_fast_rsqrt(simd_float8) -> simd_float8](./simd_fast_rsqrt%28_%29-923f0.md)
  Returns the fast reciprocal square root of each element in a vector.
- [func simd_precise_rsqrt(simd_float8) -> simd_float8](./simd_precise_rsqrt%28_%29-1hqkg.md)
  Returns the precise reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_float8) -> simd_float8](./exp%28_%29-1pg0i.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_float8) -> simd_float8](./exp2%28_%29-1n4s0.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_float8) -> simd_float8](./exp10%28_%29-8kkzs.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_float8) -> simd_float8](./expm1%28_%29-70odp.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_float8) -> simd_float8](./log%28_%29-5bs8h.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_float8) -> simd_float8](./log2%28_%29-939d1.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_float8) -> simd_float8](./log10%28_%29-94fwu.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_float8) -> simd_float8](./log1p%28_%29-7f7d8.md)
  Returns *log(1+x)* of each element in a vector.
### Hyperbolic Functions
- [func acosh(simd_float8) -> simd_float8](./acosh%28_%29-5ye64.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_float8) -> simd_float8](./asinh%28_%29-1uw5q.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_float8) -> simd_float8](./atanh%28_%29-95265.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_float8) -> simd_float8](./cosh%28_%29-6rb1l.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_float8) -> simd_float8](./sinh%28_%29-43ijd.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_float8) -> simd_float8](./tanh%28_%29-tpg5.md)
  Returns the hyperbolic tangent of each element in a vector.
### Logic Functions
- [func simd_select(simd_float8, simd_float8, simd_int8) -> simd_float8](./simd_select%28_,_,_%29-5h243.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_float8, simd_float8, simd_int8) -> simd_float8](./simd_bitselect%28_,_,_%29-66uzh.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_float8) -> simd_float8](./cbrt%28_%29-3f2k2.md)
  Returns the cube root of each element in a vector.
- [func erf(simd_float8) -> simd_float8](./erf%28_%29-5vzab.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_float8) -> simd_float8](./erfc%28_%29-1csse.md)
  Returns the complementary error function for each element in a vector.
- [func fma(simd_float8, simd_float8, simd_float8) -> simd_float8](./fma%28_,_,_%29-49crk.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_float8, simd_float8) -> simd_float8](./fmod%28_,_%29-8fmuq.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_float8, simd_float8) -> simd_float8](./hypot%28_,_%29-47t8e.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_float8) -> simd_float8](./lgamma%28_%29-9g2rk.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_float8, simd_float8) -> simd_float8](./nextafter%28_,_%29-sc7d.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_float8, simd_float8) -> simd_float8](./pow%28_,_%29-nk2t.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_float8, simd_float8) -> simd_float8](./remainder%28_,_%29-7l2wd.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_float8) -> simd_float8](./round%28_%29-1ffcx.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_float8, simd_float8, simd_float8) -> simd_float8](./simd_muladd%28_,_,_%29-3v5t5.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_float8) -> simd_float8](./tgamma%28_%29-6tafl.md)
  Returns the gamma function for each element in a vector.
### Trigonometric Functions
- [func acos(simd_float8) -> simd_float8](./acos%28_%29-7zw9c.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_float8) -> simd_float8](./asin%28_%29-476k0.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_float8) -> simd_float8](./atan%28_%29-al43.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_float8, simd_float8) -> simd_float8](./atan2%28_,_%29-52zvp.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_float8) -> simd_float8](./cos%28_%29-6spt8.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_float8) -> simd_float8](./cospi%28_%29-mwoe.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_float8) -> simd_float8](./sin%28_%29-8n720.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_float8) -> simd_float8](./sinpi%28_%29-5sfds.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_float8) -> (sin: simd_float8, cos: simd_float8)](./sincos%28_%29-26uzx.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_float8) -> (sin: simd_float8, cos: simd_float8)](./sincospi%28_%29-3cme4.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_float8) -> simd_float8](./tan%28_%29-6t9p5.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_float8) -> simd_float8](./tanpi%28_%29-5w53i.md)
  Returns the tangent of each element in a vector multiplied by pi.
### Classification Functions
- [func isfinite(simd_float8) -> simd_int8](./isfinite%28_%29-285ek.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_float8) -> simd_int8](./isinf%28_%29-9ud2k.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_float8) -> simd_int8](./isnan%28_%29-8blhp.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_float8) -> simd_int8](./isnormal%28_%29-36pn2.md)
  Returns true for each element that is normal in a vector.
### Alternative Type Alias
- [typealias vector_float8](./vector_float8.md)
### Functions to Create Eight-Element Vectors From Vectors of Other Types
- [simd_float](./simd_float-1pfvj.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_float](./simd_float-1ppun.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_float](./simd_float-1pazj.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_float](./simd_float-1pkyn.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_float](./simd_float-1phqj.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_float](./simd_float-1prpn.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_float](./simd_float-1pgbl.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_float](./simd_float-1pq5d.md)
  Returns a new vector from the specified vector of 64-bit, unsigned-integer elements.
- [simd_float](./simd_float-1poa9.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_float](./simd_float-1pno1.md)
  Returns a new vector from the specified vector of 64 -bit, floating-point elements.
### Geometry Functions
- [simd_dot](./simd_dot-7390g.md)
  Returns the dot product of two vectors.
- [simd_project](./simd_project-8htqe.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-98hyq.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-33evf.md)
  Returns the precise projected vector.
- [simd_normalize](./simd_normalize-xs3.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-8x4o0.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-623uc.md)
  Returns the precise normalized vector.
### Vector Norm Functions
- [simd_norm_one](./simd_norm_one-fhar.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-9mawm.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [simd_length](./simd_length-32wmj.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-5utao.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-67kmm.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-3xa1d.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-8i534.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-1ml9e.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-9w7rx.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-7gp4v.md)
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
- [typealias simd_float16](./simd_float16.md)
  A vector of sixteen 32-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float8)*