# simd_double4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 64-bit floating-point elements.

## Declaration

```swift
typealias simd_double4 = SIMD4<Double>
```

```c
typedef double __attribute__((ext_vector_type(4))) simd_double4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_double4(simd_double2) -> simd_double4](./simd_make_double4%28_%29-3ft6m.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_double4(simd_double3) -> simd_double4](./simd_make_double4%28_%29-3jd0t.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_double4(simd_double4) -> simd_double4](./simd_make_double4%28_%29-3ofj0.md)
  Returns a new vector from the specified vector.
- [func simd_make_double4(simd_double8) -> simd_double4](./simd_make_double4%28_%29-41bao.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_double4(simd_double2, simd_double2) -> simd_double4](./simd_make_double4%28_,_%29-68v0e.md)
  Returns a new vector from the specified vectors.
- [func simd_make_double4_undef(simd_double2) -> simd_double4](./simd_make_double4_undef%28_%29-6brs0.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_double4_undef(simd_double3) -> simd_double4](./simd_make_double4_undef%28_%29-68wqb.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [vector4](./vector4-15myv.md)
  Returns a new vector from the specified vectors.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_double4(Double) -> simd_double4](./simd_make_double4%28_%29-2zeiq.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_double4(Double, Double, Double, Double) -> simd_double4](./simd_make_double4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_double4_undef(Double) -> simd_double4](./simd_make_double4_undef%28_%29-22old.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector4](./vector4-4b8da.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_double4(Double, Double, simd_double2) -> simd_double4](./simd_make_double4%28_,_,_%29-51v00.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_double4(Double, simd_double2, Double) -> simd_double4](./simd_make_double4%28_,_,_%29-8f2vh.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_double4(Double, simd_double3) -> simd_double4](./simd_make_double4%28_,_%29-1ifzl.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_double4(simd_double2, Double, Double) -> simd_double4](./simd_make_double4%28_,_,_%29-8b5fy.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_double4(simd_double3, Double) -> simd_double4](./simd_make_double4%28_,_%29-767qm.md)
  Returns a new vector from a vector and a scalar value.
- [vector4](./vector4-23zx8.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_double4) -> simd_double4](./simd_abs%28_%29-81rjc.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD4<Double>) -> SIMD4<Double>](./abs%28_%29-63bb7.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_double4, simd_double4, simd_double4) -> simd_double4](./simd_clamp%28_,_,_%29-8skia.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<Double>, min: Double, max: Double) -> SIMD4<Double>](./clamp%28_,min,max%29-3iua3.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<Double>, min: SIMD4<Double>, max: SIMD4<Double>) -> SIMD4<Double>](./clamp%28_,min,max%29-51jkt.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_fract(simd_double4) -> simd_double4](./simd_fract%28_%29-3w3dh.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD4<Double>) -> SIMD4<Double>](./fract%28_%29-8mowg.md)
  Returns the fractional part of each element in a vector.
- [func simd_equal(simd_double4, simd_double4) -> simd_bool](./simd_equal%28_,_%29-6lpka.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_sign(simd_double4) -> simd_double4](./simd_sign%28_%29-74z7b.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD4<Double>) -> SIMD4<Double>](./sign%28_%29-86tur.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_double4, simd_double4) -> simd_double4](./simd_step%28_,_%29-6nrf4.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD4<Double>, edge: SIMD4<Double>) -> SIMD4<Double>](./step%28_,edge%29-641e1.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_add(simd_double4) -> Double](./simd_reduce_add%28_%29-2ymlg.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD4<Double>) -> Double](./reduce_add%28_%29-7psay.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_double4) -> Double](./simd_reduce_max%28_%29-4qv3y.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD4<Double>) -> Double](./reduce_max%28_%29-66smw.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_double4) -> Double](./simd_reduce_min%28_%29-4umgm.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD4<Double>) -> Double](./reduce_min%28_%29-4bbr.md)
  Returns the minimum value in a vector.
### Interpolation Functions
- [func simd_smoothstep(simd_double4, simd_double4, simd_double4) -> simd_double4](./simd_smoothstep%28_,_,_%29-6idlb.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD4<Double>, edge0: SIMD4<Double>, edge1: SIMD4<Double>) -> SIMD4<Double>](./smoothstep%28_,edge0,edge1%29-3gmrv.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func simd_mix(simd_double4, simd_double4, simd_double4) -> simd_double4](./simd_mix%28_,_,_%29-49aeg.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Double>, SIMD4<Double>, t: Double) -> SIMD4<Double>](./mix%28_,_,t%29-9jxxl.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Double>, SIMD4<Double>, t: SIMD4<Double>) -> SIMD4<Double>](./mix%28_,_,t%29-92fbo.md)
  Returns an element-wise linearly interpolated value between two vectors.
### Extrema Functions
- [func simd_max(simd_double4, simd_double4) -> simd_double4](./simd_max%28_,_%29-72b4.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD4<Double>, Double) -> SIMD4<Double>](./max%28_,_%29-82ig0.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD4<Double>, SIMD4<Double>) -> SIMD4<Double>](./max%28_,_%29-4pgdo.md)
  Returns the maximum value of each element in a vector.
- [func fmax(SIMD4<Double>, SIMD4<Double>) -> SIMD4<Double>](./fmax%28_,_%29-60f6g.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_double4, simd_double4) -> simd_double4](./simd_min%28_,_%29-78g6s.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD4<Double>, Double) -> SIMD4<Double>](./min%28_,_%29-7rmn.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD4<Double>, SIMD4<Double>) -> SIMD4<Double>](./min%28_,_%29-8m4sw.md)
  Returns the minimum value of each element in a vector.
- [func fmin(SIMD4<Double>, SIMD4<Double>) -> SIMD4<Double>](./fmin%28_,_%29-4joph.md)
  Returns the minimum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func simd_recip(simd_double4) -> simd_double4](./simd_recip%28_%29-8218m.md)
  Returns the reciprocal of each element in a vector.
- [func recip(SIMD4<Double>) -> SIMD4<Double>](./recip%28_%29-2zcya.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_double4) -> simd_double4](./simd_rsqrt%28_%29-i5ka.md)
  Returns the reciprocal square root of each element in a vector.
- [func rsqrt(SIMD4<Double>) -> SIMD4<Double>](./rsqrt%28_%29-8rb58.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_double4) -> simd_double4](./simd_precise_recip%28_%29-6pt5q.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_double4) -> simd_double4](./simd_precise_rsqrt%28_%29-136bw.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_double4) -> simd_double4](./simd_fast_recip%28_%29-61j.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_double4) -> simd_double4](./simd_fast_rsqrt%28_%29-8p6tk.md)
  Returns the fast reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_double4) -> simd_double4](./exp%28_%29-92zj.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_double4) -> simd_double4](./exp2%28_%29-6nz50.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_double4) -> simd_double4](./exp10%28_%29-apfo.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_double4) -> simd_double4](./expm1%28_%29-4osfq.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_double4) -> simd_double4](./log%28_%29-54908.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_double4) -> simd_double4](./log2%28_%29-2m5uu.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_double4) -> simd_double4](./log10%28_%29-80x29.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_double4) -> simd_double4](./log1p%28_%29-t4r0.md)
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
- [func dot(SIMD4<Double>, SIMD4<Double>) -> Double](./dot%28_,_%29-5ifd.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD4<Double>) -> SIMD4<Double>](./normalize%28_%29-3lhrd.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD4<Double>, SIMD4<Double>) -> SIMD4<Double>](./project%28_,_%29-1uuxo.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD4<Double>, n: SIMD4<Double>) -> SIMD4<Double>](./reflect%28_,n%29-1nabs.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD4<Double>, n: SIMD4<Double>, eta: Double) -> SIMD4<Double>](./refract%28_,n,eta%29-2macj.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
- [simd_dot](./simd_dot-85nay.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9o7wa.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-3rv7.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-4vtps.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-6cfku.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-6urv1.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-1f1gc.md)
  Returns the precise projected vector.
- [simd_reflect](./simd_reflect-91ah5.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-7dskm.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
### Vector Norm Functions
- [func norm_one(SIMD4<Double>) -> Double](./norm_one%28_%29-1cwpd.md)
  Returns the sum of the absolute values of a vector.
- [func norm_inf(SIMD4<Double>) -> Double](./norm_inf%28_%29-8zws7.md)
  Returns the maximum absolute value of a vector.
- [simd_norm_one](./simd_norm_one-scnf.md)
  Returns the sum of the absolute values of a vector.
- [simd_norm_inf](./simd_norm_inf-97qpi.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [func length(SIMD4<Double>) -> Double](./length%28_%29-79i68.md)
  Returns the length of a vector.
- [func length_squared(SIMD4<Double>) -> Double](./length_squared%28_%29-856uz.md)
  Returns the square of the length of a vector.
- [func distance(SIMD4<Double>, SIMD4<Double>) -> Double](./distance%28_,_%29-559m9.md)
  Returns the distance between two vectors.
- [func distance_squared(SIMD4<Double>, SIMD4<Double>) -> Double](./distance_squared%28_,_%29-73nv3.md)
  Returns the square of the distance between two vectors.
- [simd_length](./simd_length-3fo5n.md)
  Returns the length of a vector.
- [simd_fast_length](./simd_fast_length-4okp0.md)
  Returns the fast length of a vector.
- [simd_precise_length](./simd_precise_length-7dt8e.md)
  Returns the precise length of a vector.
- [simd_length_squared](./simd_length_squared-2t7x9.md)
  Returns the square of the length of a vector.
- [simd_distance](./simd_distance-9rhec.md)
  Returns the distance between two vectors.
- [simd_fast_distance](./simd_fast_distance-13ukv.md)
  Returns the fast distance between two vectors.
- [simd_precise_distance](./simd_precise_distance-5ywfl.md)
  Returns the precise distance between two vectors.
- [simd_distance_squared](./simd_distance_squared-42eds.md)
  Returns the square of the distance between two vectors.
### Hyperbolic Functions
- [func acosh(simd_double4) -> simd_double4](./acosh%28_%29-2a3a.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_double4) -> simd_double4](./asinh%28_%29-847y.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_double4) -> simd_double4](./atanh%28_%29-17pza.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_double4) -> simd_double4](./cosh%28_%29-8h0te.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_double4) -> simd_double4](./sinh%28_%29-3rjw6.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_double4) -> simd_double4](./tanh%28_%29-x8vt.md)
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
- [func simd_select(simd_double4, simd_double4, simd_long4) -> simd_double4](./simd_select%28_,_,_%29-tq6k.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_double4, simd_double4, simd_long4) -> simd_double4](./simd_bitselect%28_,_,_%29-1mn6g.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_double4) -> simd_double4](./cbrt%28_%29-7pm3s.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD4<Double>) -> SIMD4<Double>](./ceil%28_%29-9s503.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_double4) -> simd_double4](./erf%28_%29-1yjjk.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_double4) -> simd_double4](./erfc%28_%29-6rgzx.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD4<Double>) -> SIMD4<Double>](./floor%28_%29-3956i.md)
  Returns the floor of each element in a vector.
- [func fma(simd_double4, simd_double4, simd_double4) -> simd_double4](./fma%28_,_,_%29-6mqpv.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_double4, simd_double4) -> simd_double4](./fmod%28_,_%29-92tjw.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_double4, simd_double4) -> simd_double4](./hypot%28_,_%29-2exik.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_double4) -> simd_double4](./lgamma%28_%29-2frmv.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_double4, simd_double4) -> simd_double4](./nextafter%28_,_%29-oxq7.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_double4, simd_double4) -> simd_double4](./pow%28_,_%29-3jh7o.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_double4, simd_double4) -> simd_double4](./remainder%28_,_%29-jw8b.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_double4) -> simd_double4](./round%28_%29-5ytc6.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_double4, simd_double4, simd_double4) -> simd_double4](./simd_muladd%28_,_,_%29-6kpyx.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_double4) -> simd_double4](./tgamma%28_%29-2o8vo.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD4<Double>) -> SIMD4<Double>](./trunc%28_%29-9n2h5.md)
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
- [func acos(simd_double4) -> simd_double4](./acos%28_%29-9cb48.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_double4) -> simd_double4](./asin%28_%29-70soc.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_double4) -> simd_double4](./atan%28_%29-5w6c7.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_double4, simd_double4) -> simd_double4](./atan2%28_,_%29-19fnn.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_double4) -> simd_double4](./cos%28_%29-1leci.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_double4) -> simd_double4](./cospi%28_%29-8cke2.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_double4) -> simd_double4](./sin%28_%29-67ulu.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_double4) -> simd_double4](./sinpi%28_%29-45nf0.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_double4) -> (sin: simd_double4, cos: simd_double4)](./sincos%28_%29-9olep.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_double4) -> (sin: simd_double4, cos: simd_double4)](./sincospi%28_%29-40ymv.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_double4) -> simd_double4](./tan%28_%29-5zsp2.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_double4) -> simd_double4](./tanpi%28_%29-54qo6.md)
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
- [func isfinite(simd_double4) -> simd_long4](./isfinite%28_%29-1870d.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_double4) -> simd_long4](./isinf%28_%29-4gutc.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_double4) -> simd_long4](./isnan%28_%29-94v5c.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_double4) -> simd_long4](./isnormal%28_%29-35fxl.md)
  Returns true for each element that is normal in a vector.
### Alternative Type Alias
- [typealias vector_double4](./vector_double4.md)
- [typealias double4](./double4.md)
### Functions to Create Four-Element Vectors From Vectors of Other Types
- [simd_double](./simd_double-5p2h2.md)
  Returns a new vector from the specified vector of 8-bit, signed-integer elements.
- [simd_double](./simd_double-5osau.md)
  Returns a new vector from the specified vector of 8-bit, unsigned-integer elements.
- [simd_double](./simd_double-5oxie.md)
  Returns a new vector from the specified vector of 16-bit, signed-integer elements.
- [simd_double](./simd_double-5onhi.md)
  Returns a new vector from the specified vector of 16-bit, unsigned-integer elements.
- [simd_double](./simd_double-5p456.md)
  Returns a new vector from the specified vector of 32-bit, signed-integer elements.
- [simd_double](./simd_double-5ouey.md)
  Returns a new vector from the specified vector of 32-bit, unsigned-integer elements.
- [simd_double](./simd_double-5p376.md)
  Returns a new vector from the specified vector of 64-bit, signed-integer elements.
- [simd_double](./simd_double-5ot9u.md)
  Returns a new vector from the specified vector of 64-bit, unsigned-integer elements.
- [simd_double](./simd_double-5orke.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_double](./simd_double-5oqzm.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector data types
- [typealias simd_double1](./simd_double1.md)
  A vector of one 64-bit floating-point element.
- [typealias simd_double2](./simd_double2.md)
  A vector of two 64-bit floating-point elements.
- [typealias simd_double3](./simd_double3.md)
  A vector of three 64-bit floating-point elements.
- [typealias simd_double8](./simd_double8.md)
  A vector of eight 64-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_double4)*