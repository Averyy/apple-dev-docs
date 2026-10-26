# simd_double3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 64-bit floating-point elements.

## Declaration

```swift
typealias simd_double3 = SIMD3<Double>
```

```c
typedef double __attribute__((ext_vector_type(3))) simd_double3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_double3(simd_double2) -> simd_double3](./simd_make_double3%28_%29-5ti92.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_double3(simd_double3) -> simd_double3](./simd_make_double3%28_%29-5qigh.md)
  Returns a new vector from the specified vector.
- [func simd_make_double3(simd_double4) -> simd_double3](./simd_make_double3%28_%29-5zuas.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_double3(simd_double8) -> simd_double3](./simd_make_double3%28_%29-4tl5k.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_double3_undef(simd_double2) -> simd_double3](./simd_make_double3_undef%28_%29-95a07.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_double3(Double) -> simd_double3](./simd_make_double3%28_%29-3qbde.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_double3(Double, Double, Double) -> simd_double3](./simd_make_double3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_double3_undef(Double) -> simd_double3](./simd_make_double3_undef%28_%29-38cg2.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector3](./vector3-kp2l.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_double3(Double, simd_double2) -> simd_double3](./simd_make_double3%28_,_%29-2va6.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_double3(simd_double2, Double) -> simd_double3](./simd_make_double3%28_,_%29-3b3z3.md)
  Returns a new vector from a vector and a scalar value.
- [vector3](./vector3-2regp.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_double3) -> simd_double3](./simd_abs%28_%29-8db3x.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD3<Double>) -> SIMD3<Double>](./abs%28_%29-8miv.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_double3, simd_double3, simd_double3) -> simd_double3](./simd_clamp%28_,_,_%29-2jao.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Double>, min: Double, max: Double) -> SIMD3<Double>](./clamp%28_,min,max%29-5otf7.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Double>, min: SIMD3<Double>, max: SIMD3<Double>) -> SIMD3<Double>](./clamp%28_,min,max%29-6m2so.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_double3, simd_double3) -> simd_bool](./simd_equal%28_,_%29-4v2cb.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_double3) -> simd_double3](./simd_fract%28_%29-47n4w.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD3<Double>) -> SIMD3<Double>](./fract%28_%29-swov.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_double3) -> simd_double3](./simd_sign%28_%29-6goju.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD3<Double>) -> SIMD3<Double>](./sign%28_%29-2qtea.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_double3, simd_double3) -> simd_double3](./simd_step%28_,_%29-2gbx7.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD3<Double>, edge: SIMD3<Double>) -> SIMD3<Double>](./step%28_,edge%29-4azct.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_add(simd_double3) -> Double](./simd_reduce_add%28_%29-2v7l1.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD3<Double>) -> Double](./reduce_add%28_%29-3112d.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_double3) -> Double](./simd_reduce_max%28_%29-4gytr.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD3<Double>) -> Double](./reduce_max%28_%29-96cb3.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_double3) -> Double](./simd_reduce_min%28_%29-46by3.md)
  Returns the miniumum value in a vector.
- [func reduce_min(SIMD3<Double>) -> Double](./reduce_min%28_%29-9g9a6.md)
  Returns the miniumum value in a vector.
### Interpolation Functions
- [func simd_mix(simd_double3, simd_double3, simd_double3) -> simd_double3](./simd_mix%28_,_,_%29-46dv1.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD3<Double>, SIMD3<Double>, t: Double) -> SIMD3<Double>](./mix%28_,_,t%29-1dp7m.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD3<Double>, SIMD3<Double>, t: SIMD3<Double>) -> SIMD3<Double>](./mix%28_,_,t%29-5ifg3.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_double3, simd_double3, simd_double3) -> simd_double3](./simd_smoothstep%28_,_,_%29-9hwr9.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD3<Double>, edge0: SIMD3<Double>, edge1: SIMD3<Double>) -> SIMD3<Double>](./smoothstep%28_,edge0,edge1%29-5ih1o.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema Functions
- [func simd_min(simd_double3, simd_double3) -> simd_double3](./simd_min%28_,_%29-5xqg7.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD3<Double>, Double) -> SIMD3<Double>](./min%28_,_%29-7hm19.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./min%28_,_%29-32b0w.md)
  Returns the minimum value of each element in a vector.
- [func fmin(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./fmin%28_,_%29-6p9y.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_double3, simd_double3) -> simd_double3](./simd_max%28_,_%29-6ykq4.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD3<Double>, Double) -> SIMD3<Double>](./max%28_,_%29-1mzkc.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./max%28_,_%29-9e6ry.md)
  Returns the maximum value of each element in a vector.
- [func fmax(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./fmax%28_,_%29-4pce8.md)
  Returns the maximum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func simd_recip(simd_double3) -> simd_double3](./simd_recip%28_%29-8jzqn.md)
  Returns the reciprocal of each element in a vector.
- [func recip(SIMD3<Double>) -> SIMD3<Double>](./recip%28_%29-6uvj7.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_double3) -> simd_double3](./simd_rsqrt%28_%29-rhpf.md)
  Returns the reciprocal square root of each element in a vector.
- [func rsqrt(SIMD3<Double>) -> SIMD3<Double>](./rsqrt%28_%29-6298y.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_double3) -> simd_double3](./simd_precise_recip%28_%29-61i77.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_double3) -> simd_double3](./simd_precise_rsqrt%28_%29-zrh9.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_double3) -> simd_double3](./simd_fast_recip%28_%29-ogui.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_double3) -> simd_double3](./simd_fast_rsqrt%28_%29-80w49.md)
  Returns the fast reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_double3) -> simd_double3](./exp%28_%29-zash.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_double3) -> simd_double3](./exp2%28_%29-26tvo.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_double3) -> simd_double3](./exp10%28_%29-88dd5.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_double3) -> simd_double3](./expm1%28_%29-2ag4r.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_double3) -> simd_double3](./log%28_%29-70ujd.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_double3) -> simd_double3](./log2%28_%29-3p8ex.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_double3) -> simd_double3](./log10%28_%29-1eshe.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_double3) -> simd_double3](./log1p%28_%29-50npd.md)
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
- [func cross(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./cross%28_,_%29-7sd7t.md)
  Returns the cross product of two vectors.
- [func dot(SIMD3<Double>, SIMD3<Double>) -> Double](./dot%28_,_%29-2sdb.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD3<Double>) -> SIMD3<Double>](./normalize%28_%29-29n8k.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD3<Double>, SIMD3<Double>) -> SIMD3<Double>](./project%28_,_%29-9jlig.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD3<Double>, n: SIMD3<Double>) -> SIMD3<Double>](./reflect%28_,n%29-1vw0n.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD3<Double>, n: SIMD3<Double>, eta: Double) -> SIMD3<Double>](./refract%28_,n,eta%29-13wsy.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
- [simd_cross](./simd_cross-27rm0.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-8l0kd.md)
  Returns the dot product of two vectors.
- [simd_insphere](./simd_insphere-88pzx.md)
  Tests if a double-precision point lies inside, on, or outside a sphere.
- [simd_normalize](./simd_normalize-9c477.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-d0e.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-4z8q1.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-4dorr.md)
  Tests the orientation of the three supplied vectors.
- [simd_orient](./simd_orient-5pahm.md)
  Tests the orientation of the four supplied vectors.
- [simd_project](./simd_project-7mlzt.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-54ecd.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-3cfbv.md)
  Returns the precise projected vector.
- [simd_reflect](./simd_reflect-26oex.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-8ogip.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
### Vector Norm Functions
- [func norm_one(SIMD3<Double>) -> Double](./norm_one%28_%29-mrh.md)
  Returns the sum of the absolute values of a vector.
- [func norm_inf(SIMD3<Double>) -> Double](./norm_inf%28_%29-7ga8i.md)
  Returns the maximum absolute value of a vector.
- [simd_norm_one](./simd_norm_one-xf5y.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-94bsb.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [func length(SIMD3<Double>) -> Double](./length%28_%29-907xq.md)
  Returns the length of a vector.
- [func length_squared(SIMD3<Double>) -> Double](./length_squared%28_%29-620zs.md)
  Returns the square of the length of a vector.
- [func distance(SIMD3<Double>, SIMD3<Double>) -> Double](./distance%28_,_%29-57zfj.md)
  Returns the distance between two vectors.
- [func distance_squared(SIMD3<Double>, SIMD3<Double>) -> Double](./distance_squared%28_,_%29-4erc0.md)
- [simd_length](./simd_length-3r7wy.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-56j8x.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-7aygj.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-3hijo.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-30257.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-9625l.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-274w4.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-89twb.md)
  Returns the square of the distance between two vectors.
### Hyperbolic Functions
- [func acosh(simd_double3) -> simd_double3](./acosh%28_%29-1e4qf.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_double3) -> simd_double3](./asinh%28_%29-8b3vg.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_double3) -> simd_double3](./atanh%28_%29-7z6qz.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_double3) -> simd_double3](./cosh%28_%29-6f3bc.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_double3) -> simd_double3](./sinh%28_%29-6glq8.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_double3) -> simd_double3](./tanh%28_%29-4b44y.md)
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
- [func simd_select(simd_double3, simd_double3, simd_long3) -> simd_double3](./simd_select%28_,_,_%29-1aiih.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_double3, simd_double3, simd_long3) -> simd_double3](./simd_bitselect%28_,_,_%29-mtv1.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_double3) -> simd_double3](./cbrt%28_%29-38h14.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD3<Double>) -> SIMD3<Double>](./ceil%28_%29-72yci.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_double3) -> simd_double3](./erf%28_%29-8eer2.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_double3) -> simd_double3](./erfc%28_%29-7ux6y.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD3<Double>) -> SIMD3<Double>](./floor%28_%29-262rp.md)
  Returns the floor of each element in a vector.
- [func fma(simd_double3, simd_double3, simd_double3) -> simd_double3](./fma%28_,_,_%29-6w3jf.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_double3, simd_double3) -> simd_double3](./fmod%28_,_%29-16oie.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_double3, simd_double3) -> simd_double3](./hypot%28_,_%29-5z7ry.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_double3) -> simd_double3](./lgamma%28_%29-4lks7.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_double3, simd_double3) -> simd_double3](./nextafter%28_,_%29-7qi1e.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_double3, simd_double3) -> simd_double3](./pow%28_,_%29-6hgod.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_double3, simd_double3) -> simd_double3](./remainder%28_,_%29-28w7v.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_double3) -> simd_double3](./round%28_%29-3e7l9.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_double3, simd_double3, simd_double3) -> simd_double3](./simd_muladd%28_,_,_%29-74qpk.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_double3) -> simd_double3](./tgamma%28_%29-98alm.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD3<Double>) -> SIMD3<Double>](./trunc%28_%29-4p8mg.md)
  Returns each element in a vector rounded toward zero to the nearest integer.
- [cbrt](./cbrt.md)
  Returns the cube root of each element in a vector.
- [copysign](./copysign.md)
  Returns each element of a vector, with the sign of the corresponding element in a second vector.
- [erf](./erf.md)
  Returns the error function for each element in a vector.
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
- [func acos(simd_double3) -> simd_double3](./acos%28_%29-76i0e.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_double3) -> simd_double3](./asin%28_%29-g6mp.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_double3) -> simd_double3](./atan%28_%29-2h77h.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_double3, simd_double3) -> simd_double3](./atan2%28_,_%29-1zx4a.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_double3) -> simd_double3](./cos%28_%29-9hw4a.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_double3) -> simd_double3](./cospi%28_%29-471sg.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_double3) -> simd_double3](./sin%28_%29-5dnnn.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_double3) -> simd_double3](./sinpi%28_%29-291vx.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_double3) -> (sin: simd_double3, cos: simd_double3)](./sincos%28_%29-6572x.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_double3) -> (sin: simd_double3, cos: simd_double3)](./sincospi%28_%29-2t5q7.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_double3) -> simd_double3](./tan%28_%29-2tvur.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_double3) -> simd_double3](./tanpi%28_%29-42odv.md)
  Returns the tangent of each element in a vector multiplied by pi.
- [acos](./acos.md)
  Returns the arccosine of each element in a vector.
- [asin](./asin.md)
  Returns the arcsine of each element in a vector.
- [atan](./atan.md)
  Returns the arctangent of each element in a vector.
- [atan2](./atan2.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
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
- [func isfinite(simd_double3) -> simd_long3](./isfinite%28_%29-1s3ji.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_double3) -> simd_long3](./isinf%28_%29-6gve5.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_double3) -> simd_long3](./isnan%28_%29-6l7v3.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_double3) -> simd_long3](./isnormal%28_%29-8k36k.md)
  Returns true for each element that is normal in a vector.
### Alternative Type Alias
- [typealias vector_double3](./vector_double3.md)
- [typealias double3](./double3.md)
### Functions to Create Three-Element Vectors From Vectors of Other Types
- [simd_double](./simd_double-50ppx.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_double](./simd_double-50fw5.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_double](./simd_double-50kxh.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_double](./simd_double-50at1.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_double](./simd_double-50rjx.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_double](./simd_double-50hml.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_double](./simd_double-50shr.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_double](./simd_double-50irj.md)
  Returns a new vector from the specified vector of 64-bit, unsigned-integer elements.
- [simd_double](./simd_double-50gn7.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_double](./simd_double-50g0v.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector data types
- [typealias simd_double1](./simd_double1.md)
  A vector of one 64-bit floating-point element.
- [typealias simd_double2](./simd_double2.md)
  A vector of two 64-bit floating-point elements.
- [typealias simd_double4](./simd_double4.md)
  A vector of four 64-bit floating-point elements.
- [typealias simd_double8](./simd_double8.md)
  A vector of eight 64-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double3)*