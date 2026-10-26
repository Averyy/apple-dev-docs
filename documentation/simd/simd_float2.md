# simd_float2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 32-bit floating-point elements.

## Declaration

```swift
typealias simd_float2 = SIMD2<Float>
```

```c
typedef float __attribute__((ext_vector_type(2))) simd_float2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_float2(simd_float2) -> simd_float2](./simd_make_float2%28_%29-3nphb.md)
  Returns a new vector from the specified vector.
- [func simd_make_float2(simd_float3) -> simd_float2](./simd_make_float2%28_%29-3kta4.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_float2(simd_float4) -> simd_float2](./simd_make_float2%28_%29-32usp.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_float2(simd_float8) -> simd_float2](./simd_make_float2%28_%29-493yd.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_float2(simd_float16) -> simd_float2](./simd_make_float2%28_%29-4e6k3.md)
  Returns a new vector by truncating the specified 16-element vector.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_float2(Float) -> simd_float2](./simd_make_float2%28_%29-70ndk.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_float2(Float, Float) -> simd_float2](./simd_make_float2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_float2_undef(Float) -> simd_float2](./simd_make_float2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector2](./vector2-25p9a.md)
  Returns a new vector from the specified scalar values.
### Common Functions
- [func simd_abs(simd_float2) -> simd_float2](./simd_abs%28_%29-886vq.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD2<Float>) -> SIMD2<Float>](./abs%28_%29-6ckob.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float2, simd_float2, simd_float2) -> simd_float2](./simd_clamp%28_,_,_%29-9b6uf.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Float>, min: Float, max: Float) -> SIMD2<Float>](./clamp%28_,min,max%29-5rthg.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Float>, min: SIMD2<Float>, max: SIMD2<Float>) -> SIMD2<Float>](./clamp%28_,min,max%29-3oo0f.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_float2, simd_float2) -> simd_bool](./simd_equal%28_,_%29-9z8e8.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_float2) -> simd_float2](./simd_fract%28_%29-42ipv.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD2<Float>) -> SIMD2<Float>](./fract%28_%29-7rplw.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_float2) -> simd_float2](./simd_sign%28_%29-6jld1.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD2<Float>) -> SIMD2<Float>](./sign%28_%29-2e6do.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float2, simd_float2) -> simd_float2](./simd_step%28_,_%29-9xjdc.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD2<Float>, edge: SIMD2<Float>) -> SIMD2<Float>](./step%28_,edge%29-1pthr.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_add(simd_float2) -> Float](./simd_reduce_add%28_%29-2pzn6.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD2<Float>) -> Float](./reduce_add%28_%29-39n2m.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_float2) -> Float](./simd_reduce_max%28_%29-4kjh0.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD2<Float>) -> Float](./reduce_max%28_%29-4zzwq.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_float2) -> Float](./simd_reduce_min%28_%29-49sh0.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD2<Float>) -> Float](./reduce_min%28_%29-76co5.md)
  Returns the minimum value in a vector.
### Interpolation Functions
- [func simd_mix(simd_float2, simd_float2, simd_float2) -> simd_float2](./simd_mix%28_,_,_%29-bvhh.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Float>, SIMD2<Float>, t: Float) -> SIMD2<Float>](./mix%28_,_,t%29-2z3yo.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Float>, SIMD2<Float>, t: SIMD2<Float>) -> SIMD2<Float>](./mix%28_,_,t%29-14tli.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_float2, simd_float2, simd_float2) -> simd_float2](./simd_smoothstep%28_,_,_%29-7iziv.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD2<Float>, edge0: SIMD2<Float>, edge1: SIMD2<Float>) -> SIMD2<Float>](./smoothstep%28_,edge0,edge1%29-43udr.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema Functions
- [func simd_max(simd_float2, simd_float2) -> simd_float2](./simd_max%28_,_%29-6uws6.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD2<Float>, Float) -> SIMD2<Float>](./max%28_,_%29-35pzn.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD2<Float>, SIMD2<Float>) -> SIMD2<Float>](./max%28_,_%29-9ye2a.md)
  Returns the maximum value of each element in a vector.
- [func fmax(SIMD2<Float>, SIMD2<Float>) -> SIMD2<Float>](./fmax%28_,_%29-3cz61.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_float2, simd_float2) -> simd_float2](./simd_min%28_,_%29-9xyee.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD2<Float>, Float) -> SIMD2<Float>](./min%28_,_%29-3eaa2.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD2<Float>, SIMD2<Float>) -> SIMD2<Float>](./min%28_,_%29-6cnnq.md)
  Returns the minimum value of each element in a vector.
- [func fmin(SIMD2<Float>, SIMD2<Float>) -> SIMD2<Float>](./fmin%28_,_%29-7jupb.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func simd_recip(simd_float2) -> simd_float2](./simd_recip%28_%29-8nf6c.md)
  Returns the reciprocal of each element in a vector.
- [func recip(SIMD2<Float>) -> SIMD2<Float>](./recip%28_%29-2opi.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_float2) -> simd_float2](./simd_rsqrt%28_%29-okw0.md)
  Returns the reciprocal square root of each element in a vector.
- [func rsqrt(SIMD2<Float>) -> SIMD2<Float>](./rsqrt%28_%29-1er1q.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_float2) -> simd_float2](./simd_precise_recip%28_%29-66mt8.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_float2) -> simd_float2](./simd_precise_rsqrt%28_%29-wqzu.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_float2) -> simd_float2](./simd_fast_recip%28_%29-ll5x.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_float2) -> simd_float2](./simd_fast_rsqrt%28_%29-84cs6.md)
  Returns the fast reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_float2) -> simd_float2](./exp%28_%29-3pa97.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_float2) -> simd_float2](./exp2%28_%29-6sez2.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_float2) -> simd_float2](./exp10%28_%29-6ga3o.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_float2) -> simd_float2](./expm1%28_%29-3bqf9.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_float2) -> simd_float2](./log%28_%29-1zfuo.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_float2) -> simd_float2](./log2%28_%29-8x5g.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_float2) -> simd_float2](./log10%28_%29-4yb6z.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_float2) -> simd_float2](./log1p%28_%29-15zc7.md)
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
- [func cross(SIMD2<Float>, SIMD2<Float>) -> SIMD3<Float>](./cross%28_,_%29-53xk2.md)
  Returns the cross product of two vectors.
- [func dot(SIMD2<Float>, SIMD2<Float>) -> Float](./dot%28_,_%29-1vb5g.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD2<Float>) -> SIMD2<Float>](./normalize%28_%29-100kb.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD2<Float>, SIMD2<Float>) -> SIMD2<Float>](./project%28_,_%29-9wt83.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD2<Float>, n: SIMD2<Float>) -> SIMD2<Float>](./reflect%28_,n%29-6w80i.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD2<Float>, n: SIMD2<Float>, eta: Float) -> SIMD2<Float>](./refract%28_,n,eta%29-5bv79.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
- [simd_cross](./simd_cross-3ukic.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-3pmfs.md)
  Returns the dot product of two vectors.
- [simd_incircle](./simd_incircle-1bi0y.md)
  Tests if a single-precision point lies inside, on, or outside a circle.
- [simd_normalize](./simd_normalize-9fok8.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-9wxm2.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-54d5a.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-8wej6.md)
  Tests the orientation of the two supplied vectors.
- [simd_orient](./simd_orient-6wf24.md)
  Tests the orientation of the three supplied vectors.
- [simd_project](./simd_project-39liq.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-4ei25.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-4chm1.md)
  Returns the fast projected vector.
- [simd_reflect](./simd_reflect-7dnri.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-4vcf3.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
### Vector Norm Functions
- [func norm_one(SIMD2<Float>) -> Float](./norm_one%28_%29-2y0m.md)
  Returns the sum of the absolute values of a vector.
- [func norm_inf(SIMD2<Float>) -> Float](./norm_inf%28_%29-9lj66.md)
  Returns the maximum absolute value of a vector.
- [simd_norm_one](./simd_norm_one-10vvt.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-91b24.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [func length(SIMD2<Float>) -> Float](./length%28_%29-6g7q5.md)
  Returns the length of a vector.
- [func length_squared(SIMD2<Float>) -> Float](./length_squared%28_%29-6tcxv.md)
  Returns the square of the length of a vector.
- [func distance(SIMD2<Float>, SIMD2<Float>) -> Float](./distance%28_,_%29-1p8ae.md)
  Returns the distance between two vectors.
- [func distance_squared(SIMD2<Float>, SIMD2<Float>) -> Float](./distance_squared%28_,_%29-9nmpe.md)
  Returns the square of the distance between two vectors.
- [simd_length](./simd_length-3ob5d.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-59ep6.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-77xwk.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-3e32j.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-598wa.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-2jlix.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-8hrn8.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-7zevh.md)
  Returns the square of the distance between two vectors.
### Hyperbolic Functions
- [func acosh(simd_float2) -> simd_float2](./acosh%28_%29-16wup.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_float2) -> simd_float2](./asinh%28_%29-14lj8.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_float2) -> simd_float2](./atanh%28_%29-3o0hv.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_float2) -> simd_float2](./cosh%28_%29-4n03p.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_float2) -> simd_float2](./sinh%28_%29-2ft5c.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_float2) -> simd_float2](./tanh%28_%29-8avnx.md)
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
- [func simd_select(simd_float2, simd_float2, simd_int2) -> simd_float2](./simd_select%28_,_,_%29-9jdc0.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_float2, simd_float2, simd_int2) -> simd_float2](./simd_bitselect%28_,_,_%29-5g70k.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_float2) -> simd_float2](./cbrt%28_%29-1t3k.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD2<Float>) -> SIMD2<Float>](./ceil%28_%29-8j6zo.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_float2) -> simd_float2](./erf%28_%29-1unjp.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_float2) -> simd_float2](./erfc%28_%29-1hisg.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD2<Float>) -> SIMD2<Float>](./floor%28_%29-1e9me.md)
  Returns the floor of each element in a vector.
- [func fma(simd_float2, simd_float2, simd_float2) -> simd_float2](./fma%28_,_,_%29-69k8u.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_float2, simd_float2) -> simd_float2](./fmod%28_,_%29-566aw.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_float2, simd_float2) -> simd_float2](./hypot%28_,_%29-1zs4i.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_float2) -> simd_float2](./lgamma%28_%29-1ksbv.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_float2, simd_float2) -> simd_float2](./nextafter%28_,_%29-8mat0.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_float2, simd_float2) -> simd_float2](./pow%28_,_%29-15e0y.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_float2, simd_float2) -> simd_float2](./remainder%28_,_%29-37wwd.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_float2) -> simd_float2](./round%28_%29-608of.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_float2, simd_float2, simd_float2) -> simd_float2](./simd_muladd%28_,_,_%29-45h2k.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_float2) -> simd_float2](./tgamma%28_%29-2aqvi.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD2<Float>) -> SIMD2<Float>](./trunc%28_%29-6neoe.md)
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
- [func acos(simd_float2) -> simd_float2](./acos%28_%29-1ya4v.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_float2) -> simd_float2](./asin%28_%29-4tbvj.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_float2) -> simd_float2](./atan%28_%29-5v3x.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_float2, simd_float2) -> simd_float2](./atan2%28_,_%29-4dpoz.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_float2) -> simd_float2](./cos%28_%29-59waa.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_float2) -> simd_float2](./cospi%28_%29-2cd9u.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_float2) -> simd_float2](./sin%28_%29-5k8vo.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_float2) -> simd_float2](./sinpi%28_%29-524r6.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_float2) -> (sin: simd_float2, cos: simd_float2)](./sincos%28_%29-4uhuq.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_float2) -> (sin: simd_float2, cos: simd_float2)](./sincospi%28_%29-11sii.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_float2) -> simd_float2](./tan%28_%29-4rx9f.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_float2) -> simd_float2](./tanpi%28_%29-3a1w1.md)
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
- [func isfinite(simd_float2) -> simd_int2](./isfinite%28_%29-zthr.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_float2) -> simd_int2](./isinf%28_%29-9bb5h.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_float2) -> simd_int2](./isnan%28_%29-7diw7.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_float2) -> simd_int2](./isnormal%28_%29-3n6dc.md)
  Returns true for each element that is normal in a vector.
### Alternative Type Alias
- [typealias vector_float2](./vector_float2.md)
- [typealias float2](./float2.md)
### Functions to Create Two-Element Vectors From Vectors of Other Types
- [simd_float](./simd_float-14iup.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_float](./simd_float-148tt.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_float](./simd_float-14nqp.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_float](./simd_float-14dwx.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_float](./simd_float-14lvd.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_float](./simd_float-14c1l.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_float](./simd_float-14mw7.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_float](./simd_float-14cvb.md)
  Returns a new vector from the specified vector of 64-bit, unsigned-integer elements.
- [simd_float](./simd_float-149uz.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_float](./simd_float-14afr.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector data types
- [typealias simd_float1](./simd_float1.md)
  A vector of one 32-bit floating-point element.
- [typealias simd_float3](./simd_float3.md)
  A vector of three 32-bit floating-point elements.
- [typealias simd_float4](./simd_float4.md)
  A vector of four 32-bit floating-point elements.
- [typealias simd_float8](./simd_float8.md)
  A vector of eight 32-bit floating-point elements.
- [typealias simd_float16](./simd_float16.md)
  A vector of sixteen 32-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float2)*