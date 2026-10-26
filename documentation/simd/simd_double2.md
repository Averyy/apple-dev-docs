# simd_double2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 64-bit floating-point elements.

## Declaration

```swift
typealias simd_double2 = SIMD2<Double>
```

```c
typedef double __attribute__((ext_vector_type(2))) simd_double2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_double2(simd_double2) -> simd_double2](./simd_make_double2%28_%29-3qby3.md)
  Returns a new vector from the specified vector.
- [func simd_make_double2(simd_double3) -> simd_double2](./simd_make_double2%28_%29-3tt38.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_double2(simd_double4) -> simd_double2](./simd_make_double2%28_%29-3hpld.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_double2(simd_double8) -> simd_double2](./simd_make_double2%28_%29-4o3ot.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_double2(Double, Double) -> simd_double2](./simd_make_double2%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [vector2](./vector2-8cpbh.md)
  Returns a new vector from the specified vectors.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_double2(Double) -> simd_double2](./simd_make_double2%28_%29-r6xz.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_double2_undef(Double) -> simd_double2](./simd_make_double2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_double2) -> simd_double2](./simd_abs%28_%29-8869e.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD2<Double>) -> SIMD2<Double>](./abs%28_%29-1p8t7.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_double2, simd_double2, simd_double2) -> simd_double2](./simd_clamp%28_,_,_%29-6puwa.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Double>, min: Double, max: Double) -> SIMD2<Double>](./clamp%28_,min,max%29-7n2jv.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Double>, min: SIMD2<Double>, max: SIMD2<Double>) -> SIMD2<Double>](./clamp%28_,min,max%29-6d1s7.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_double2, simd_double2) -> simd_bool](./simd_equal%28_,_%29-vmn4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_double2) -> simd_double2](./simd_fract%28_%29-42i3r.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD2<Double>) -> SIMD2<Double>](./fract%28_%29-2gjrn.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_double2) -> simd_double2](./simd_sign%28_%29-6jlx9.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD2<Double>) -> SIMD2<Double>](./sign%28_%29-5fczz.md)
  Returns the sign of each element in a vector.
- [func step(SIMD2<Double>, edge: SIMD2<Double>) -> SIMD2<Double>](./step%28_,edge%29-2qauk.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func simd_step(simd_double2, simd_double2) -> simd_double2](./simd_step%28_,_%29-8jlf2.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_add(simd_double2) -> Double](./simd_reduce_add%28_%29-2q09i.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD2<Double>) -> Double](./reduce_add%28_%29-8iwo6.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_double2) -> Double](./simd_reduce_max%28_%29-4kinw.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD2<Double>) -> Double](./reduce_max%28_%29-3rmpx.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_double2) -> Double](./simd_reduce_min%28_%29-49t1o.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD2<Double>) -> Double](./reduce_min%28_%29-6mev7.md)
  Returns the minimum value in a vector.
### Interpolation Functions
- [func simd_smoothstep(simd_double2, simd_double2, simd_double2) -> simd_double2](./simd_smoothstep%28_,_,_%29-e0ov.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD2<Double>, edge0: SIMD2<Double>, edge1: SIMD2<Double>) -> SIMD2<Double>](./smoothstep%28_,edge0,edge1%29-2wqo9.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func simd_mix(simd_double2, simd_double2, simd_double2) -> simd_double2](./simd_mix%28_,_,_%29-v083.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Double>, SIMD2<Double>, t: Double) -> SIMD2<Double>](./mix%28_,_,t%29-7bjg5.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Double>, SIMD2<Double>, t: SIMD2<Double>) -> SIMD2<Double>](./mix%28_,_,t%29-3hfwb.md)
  Returns an element-wise linearly interpolated value between two vectors.
### Extrema Functions
- [func simd_max(simd_double2, simd_double2) -> simd_double2](./simd_max%28_,_%29-1sy2n.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD2<Double>, Double) -> SIMD2<Double>](./max%28_,_%29-3puhr.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD2<Double>, SIMD2<Double>) -> SIMD2<Double>](./max%28_,_%29-8a5p5.md)
  Returns the maximum value of each element in a vector.
- [func fmax(SIMD2<Double>, SIMD2<Double>) -> SIMD2<Double>](./fmax%28_,_%29-15te9.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_double2, simd_double2) -> simd_double2](./simd_min%28_,_%29-9mraz.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD2<Double>, Double) -> SIMD2<Double>](./min%28_,_%29-4sdw0.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD2<Double>, SIMD2<Double>) -> SIMD2<Double>](./min%28_,_%29-9yz9x.md)
  Returns the minimum value of each element in a vector.
- [func fmin(SIMD2<Double>, SIMD2<Double>) -> SIMD2<Double>](./fmin%28_,_%29-39mes.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func recip(SIMD2<Double>) -> SIMD2<Double>](./recip%28_%29-43mv7.md)
  Returns the reciprocal of each element in a vector.
- [func simd_recip(simd_double2) -> simd_double2](./simd_recip%28_%29-8nekc.md)
  Returns the reciprocal of each element in a vector.
- [func simd_fast_recip(simd_double2) -> simd_double2](./simd_fast_recip%28_%29-lm0t.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_precise_recip(simd_double2) -> simd_double2](./simd_precise_recip%28_%29-66n8k.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_rsqrt(simd_double2) -> simd_double2](./simd_rsqrt%28_%29-ok9s.md)
  Returns the reciprocal square root of each element in a vector.
- [func rsqrt(SIMD2<Double>) -> SIMD2<Double>](./rsqrt%28_%29-2k5rh.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_fast_rsqrt(simd_double2) -> simd_double2](./simd_fast_rsqrt%28_%29-84dca.md)
  Returns the fast reciprocal square root of each element in a vector.
- [func simd_precise_rsqrt(simd_double2) -> simd_double2](./simd_precise_rsqrt%28_%29-wrke.md)
  Returns the precise reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_double2) -> simd_double2](./exp%28_%29-9nxip.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_double2) -> simd_double2](./exp2%28_%29-4y2ne.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_double2) -> simd_double2](./exp10%28_%29-4tdos.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_double2) -> simd_double2](./expm1%28_%29-9aitr.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_double2) -> simd_double2](./log%28_%29-2ieba.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_double2) -> simd_double2](./log2%28_%29-779eu.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_double2) -> simd_double2](./log10%28_%29-337zw.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_double2) -> simd_double2](./log1p%28_%29-40mka.md)
  Returns *log(1+x)* of each element in a vector.
- [exp](./exp.md)
  Returns *e* raised to the power of each element in a vector.
- [exp2](./exp2.md)
  Returns 2 raised to the power of each element in a vector.
- [exp10](./exp10.md)
  Returns 10 raised to the power of each element in a vector.
- [expm1](./expm1.md)
  Returns *eˣ-1* for each element in a vector.
- [log](./log.md)
  Returns the natural logarithm of each element in a vector.
- [log2](./log2.md)
  Returns the base 2 logarithm of each element in a vector.
- [log10](./log10.md)
  Returns the base 10 logarithm of each element in a vector.
- [log1p](./log1p.md)
  Returns *log(1+x)* for each element in a vector.
### Geometry Functions
- [func cross(SIMD2<Double>, SIMD2<Double>) -> SIMD3<Double>](./cross%28_,_%29-916aw.md)
  Returns the cross product of two vectors.
- [func dot(SIMD2<Double>, SIMD2<Double>) -> Double](./dot%28_,_%29-6ayky.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD2<Double>) -> SIMD2<Double>](./normalize%28_%29-5mqhk.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD2<Double>, SIMD2<Double>) -> SIMD2<Double>](./project%28_,_%29-kai1.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD2<Double>, n: SIMD2<Double>) -> SIMD2<Double>](./reflect%28_,n%29-3rhgb.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD2<Double>, n: SIMD2<Double>, eta: Double) -> SIMD2<Double>](./refract%28_,n,eta%29-1ghae.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
- [simd_cross](./simd_cross-1dixl.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-3r1vl.md)
  Returns the dot product of two vectors.
- [simd_incircle](./simd_incircle-8iogb.md)
  Tests if a double-precision point lies inside, on, or outside a circle.
- [simd_normalize](./simd_normalize-9fo1c.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-9wy6m.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-54dru.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-9fgki.md)
  Tests the orientation of the two supplied vectors.
- [simd_orient](./simd_orient-9b2wf.md)
  Tests the orientation of the three supplied vectors.
- [simd_project](./simd_project-1mg5p.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-6c68k.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-7t3qn.md)
  Returns the precise projected vector.
- [simd_reflect](./simd_reflect-7c8f9.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-4ani9.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
### Vector Norm Functions
- [func norm_one(SIMD2<Double>) -> Double](./norm_one%28_%29-2uh74.md)
  Returns the sum of the absolute values of a vector.
- [func norm_inf(SIMD2<Double>) -> Double](./norm_inf%28_%29-s3p1.md)
  Returns the maximum absolute value of a vector.
- [simd_norm_one](./simd_norm_one-10wox.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-91byc.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [func length(SIMD2<Double>) -> Double](./length%28_%29-4gxdk.md)
  Returns the length of a vector.
- [func length_squared(SIMD2<Double>) -> Double](./length_squared%28_%29-8gxz9.md)
  Returns the square of the length of a vector.
- [func distance(SIMD2<Double>, SIMD2<Double>) -> Double](./distance%28_,_%29-1mnxv.md)
  Returns the distance between two vectors.
- [func distance_squared(SIMD2<Double>, SIMD2<Double>) -> Double](./distance_squared%28_,_%29-56tah.md)
  Returns the square of the distance between two vectors.
- [simd_length](./simd_length-3oaj5.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-59e3i.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-77yjg.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-3e3uf.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-2d51k.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-3vbs7.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-3dnn0.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-7xzck.md)
  Returns the square of the distance between two vectors.
### Hyperbolic Functions
- [func acosh(simd_double2) -> simd_double2](./acosh%28_%29-edu.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_double2) -> simd_double2](./asinh%28_%29-nxaa.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_double2) -> simd_double2](./atanh%28_%29-5l8ss.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_double2) -> simd_double2](./cosh%28_%29-303ot.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_double2) -> simd_double2](./sinh%28_%29-5gx9h.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_double2) -> simd_double2](./tanh%28_%29-739hq.md)
  Returns the hyperbolic tangent of each element in a vector.
- [acosh](./acosh.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [asinh](./asinh.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [atanh](./atanh.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [cosh](./cosh.md)
  Returns the hyperbolic cosine of each element in a vector.
- [sinh](./sinh.md)
  Returns the hyperbolic sine of each element in a vector.
- [tanh](./tanh.md)
  Returns the hyperbolic tangent of each element in a vector.
### Logic Functions
- [func simd_select(simd_double2, simd_double2, simd_long2) -> simd_double2](./simd_select%28_,_,_%29-7sz6k.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_double2, simd_double2, simd_long2) -> simd_double2](./simd_bitselect%28_,_,_%29-3ys1a.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_double2) -> simd_double2](./cbrt%28_%29-75bqn.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD2<Double>) -> SIMD2<Double>](./ceil%28_%29-cu6z.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_double2) -> simd_double2](./erf%28_%29-7tfrz.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_double2) -> simd_double2](./erfc%28_%29-8i2r6.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD2<Double>) -> SIMD2<Double>](./floor%28_%29-21h1y.md)
- [func fma(simd_double2, simd_double2, simd_double2) -> simd_double2](./fma%28_,_,_%29-4fxau.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_double2, simd_double2) -> simd_double2](./fmod%28_,_%29-81hr1.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_double2, simd_double2) -> simd_double2](./hypot%28_,_%29-9ecpz.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_double2) -> simd_double2](./lgamma%28_%29-697vf.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_double2, simd_double2) -> simd_double2](./nextafter%28_,_%29-6qeuz.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_double2, simd_double2) -> simd_double2](./pow%28_,_%29-2ov0n.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_double2, simd_double2) -> simd_double2](./remainder%28_,_%29-1l80m.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_double2) -> simd_double2](./round%28_%29-1ith.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_double2, simd_double2, simd_double2) -> simd_double2](./simd_muladd%28_,_,_%29-o9lv.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_double2) -> simd_double2](./tgamma%28_%29-3id8t.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD2<Double>) -> SIMD2<Double>](./trunc%28_%29-1xvcu.md)
  Returns each element in a vector rounded toward zero to the nearest integer.
- [cbrt](./cbrt.md)
  Returns the cube root of each element in a vector.
- [copysign](./copysign.md)
  Returns each element of a vector, with the sign of the corresponding element in a second vector.
- [erf](./erf.md)
  Returns the error function for each element in a vector.
- [erfc](./erfc.md)
  Returns the complementary error function for each element in a vector.
- [fabs](./fabs.md)
  Returns the absolute value of each element in a vector.
- [fdim](./fdim.md)
  Returns the positive difference between corresponding elements in two vectors.
- [fma](./fma.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [fmod](./fmod.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [hypot](./hypot.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [nextafter](./nextafter.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [pow](./pow.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [remainder](./remainder.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [rint](./rint.md)
  Returns each element in a vector rounded to the nearest integer in the specified direction.
- [round](./round.md)
  Returns each element in a vector rounded to the nearest integer.
- [sqrt](./sqrt.md)
  Returns the square root of each element in a vector.
- [tgamma](./tgamma.md)
  Returns the gamma function for each element in a vector.
### Trigonometric Functions
- [func acos(simd_double2) -> simd_double2](./acos%28_%29-1hgv5.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_double2) -> simd_double2](./asin%28_%29-72orw.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_double2) -> simd_double2](./atan%28_%29-9onaa.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_double2, simd_double2) -> simd_double2](./atan2%28_,_%29-6ogu4.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_double2) -> simd_double2](./cos%28_%29-3p9ym.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_double2) -> simd_double2](./cospi%28_%29-57353.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_double2) -> simd_double2](./sin%28_%29-3p88b.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_double2) -> simd_double2](./sinpi%28_%29-4lgpo.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_double2) -> (sin: simd_double2, cos: simd_double2)](./sincos%28_%29-9pa2l.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_double2) -> (sin: simd_double2, cos: simd_double2)](./sincospi%28_%29-3fwbj.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_double2) -> simd_double2](./tan%28_%29-5czlf.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_double2) -> simd_double2](./tanpi%28_%29-9z76.md)
  Returns the tangent of each element in a vector multiplied by pi.
- [acos](./acos.md)
  Returns the arccosine of each element in a vector.
- [asin](./asin.md)
  Returns the arcsine of each element in a vector.
- [atan](./atan.md)
  Returns the arctangent of each element in a vector.
- [atan2](./atan2.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [cos](./cos.md)
  Returns the cosine of each element in a vector.
- [cospi](./cospi.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [sin](./sin.md)
  Returns the sine of each element in a vector.
- [sinpi](./sinpi.md)
  Returns the sine of each element in a vector multiplied by pi.
- [tan](./tan.md)
  Returns the tangent of each element in a vector.
- [tanpi](./tanpi.md)
  Returns the tangent of each element in a vector multiplied by pi.
### Classification Functions
- [func isfinite(simd_double2) -> simd_long2](./isfinite%28_%29-7d8q7.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_double2) -> simd_long2](./isinf%28_%29-4wflm.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_double2) -> simd_long2](./isnan%28_%29-9irpc.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_double2) -> simd_long2](./isnormal%28_%29-61nr1.md)
  Returns true for each element that is normal in a vector.
### Alternative Type Alias
- [typealias vector_double2](./vector_double2.md)
- [typealias double2](./double2.md)
### Functions to Create Three-Element Vectors From Vectors of Other Types
- [simd_double](./simd_double-531gc.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_double](./simd_double-53bbw.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_double](./simd_double-536fw.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_double](./simd_double-53gf0.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_double](./simd_double-534k4.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_double](./simd_double-53ej8.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_double](./simd_double-5365s.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_double](./simd_double-53fzk.md)
  Returns a new vector from the specified vector of 64-bit, unsigned-integer elements.
- [simd_double](./simd_double-53czc.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_double](./simd_double-53di8.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector data types
- [typealias simd_double1](./simd_double1.md)
  A vector of one 64-bit floating-point element.
- [typealias simd_double3](./simd_double3.md)
  A vector of three 64-bit floating-point elements.
- [typealias simd_double4](./simd_double4.md)
  A vector of four 64-bit floating-point elements.
- [typealias simd_double8](./simd_double8.md)
  A vector of eight 64-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double2)*