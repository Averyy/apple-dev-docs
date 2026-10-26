# simd_float3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 32-bit floating-point elements.

## Declaration

```swift
typealias simd_float3 = SIMD3<Float>
```

```c
typedef float __attribute__((ext_vector_type(3))) simd_float3;
```

## Mentions

- [Working with Matrices](../Accelerate/working-with-matrices.md)

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_float3(simd_float2) -> simd_float3](./simd_make_float3%28_%29-6jup1.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_float3(simd_float3) -> simd_float3](./simd_make_float3%28_%29-6nare.md)
  Returns a new vector from the specified vector.
- [func simd_make_float3(simd_float4) -> simd_float3](./simd_make_float3%28_%29-759bf.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_float3(simd_float8) -> simd_float3](./simd_make_float3%28_%29-7i06n.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_float3(simd_float16) -> simd_float3](./simd_make_float3%28_%29-8p6oi.md)
  Returns a new vector by truncating the specified 16-element vector.
- [func simd_make_float3_undef(simd_float2) -> simd_float3](./simd_make_float3_undef%28_%29-9aafs.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_float3(Float) -> simd_float3](./simd_make_float3%28_%29-1lvzk.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_float3(Float, Float, Float) -> simd_float3](./simd_make_float3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_float3_undef(Float) -> simd_float3](./simd_make_float3_undef%28_%29-4yqj8.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_float3(Float, simd_float2) -> simd_float3](./simd_make_float3%28_,_%29-2ke7j.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_float3(simd_float2, Float) -> simd_float3](./simd_make_float3%28_,_%29-57oga.md)
  Returns a new vector from a scalar value and a vector.
### Common Functions
- [func simd_abs(simd_float3) -> simd_float3](./simd_abs%28_%29-8dafp.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD3<Float>) -> SIMD3<Float>](./abs%28_%29-6lc19.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float3, simd_float3, simd_float3) -> simd_float3](./simd_clamp%28_,_,_%29-5szev.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Float>, min: Float, max: Float) -> SIMD3<Float>](./clamp%28_,min,max%29-3esdw.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Float>, min: SIMD3<Float>, max: SIMD3<Float>) -> SIMD3<Float>](./clamp%28_,min,max%29-9eeiz.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_float3, simd_float3) -> simd_bool](./simd_equal%28_,_%29-6i7q4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func fract(SIMD3<Float>) -> SIMD3<Float>](./fract%28_%29-3rsxo.md)
  Returns the fractional part of each element in a vector.
- [func simd_fract(simd_float3) -> simd_float3](./simd_fract%28_%29-47mh4.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_float3) -> simd_float3](./simd_sign%28_%29-6gp3q.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD3<Float>) -> SIMD3<Float>](./sign%28_%29-9p5uo.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float3, simd_float3) -> simd_float3](./simd_step%28_,_%29-9ygnw.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD3<Float>, edge: SIMD3<Float>) -> SIMD3<Float>](./step%28_,edge%29-48vbr.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_add(simd_float3) -> Float](./simd_reduce_add%28_%29-2v85p.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD3<Float>) -> Float](./reduce_add%28_%29-3xuqf.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_float3) -> Float](./simd_reduce_max%28_%29-4gy97.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD3<Float>) -> Float](./reduce_max%28_%29-1u3hn.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_float3) -> Float](./simd_reduce_min%28_%29-46cif.md)
  Returns the miniumum value in a vector.
- [func reduce_min(SIMD3<Float>) -> Float](./reduce_min%28_%29-3myvw.md)
  Returns the miniumum value in a vector.
### Interpolation Functions
- [func simd_mix(simd_float3, simd_float3, simd_float3) -> simd_float3](./simd_mix%28_,_,_%29-6l1x8.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD3<Float>, SIMD3<Float>, t: Float) -> SIMD3<Float>](./mix%28_,_,t%29-9o58r.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD3<Float>, SIMD3<Float>, t: SIMD3<Float>) -> SIMD3<Float>](./mix%28_,_,t%29-6c4d3.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_float3, simd_float3, simd_float3) -> simd_float3](./simd_smoothstep%28_,_,_%29-mz0x.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD3<Float>, edge0: SIMD3<Float>, edge1: SIMD3<Float>) -> SIMD3<Float>](./smoothstep%28_,edge0,edge1%29-6m76x.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema Functions
- [func simd_min(simd_float3, simd_float3) -> simd_float3](./simd_min%28_,_%29-9ccbp.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD3<Float>, Float) -> SIMD3<Float>](./min%28_,_%29-2xilk.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./min%28_,_%29-7cjgj.md)
  Returns the minimum value of each element in a vector.
- [func fmin(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./fmin%28_,_%29-6jyy2.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_float3, simd_float3) -> simd_float3](./simd_max%28_,_%29-6x53b.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD3<Float>, Float) -> SIMD3<Float>](./max%28_,_%29-27ore.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./max%28_,_%29-7plm.md)
  Returns the maximum value of each element in a vector.
- [func fmax(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./fmax%28_,_%29-1yseu.md)
  Returns the maximum value of each element in a vector.
### Reciprocal and Reciprocal Square Root Functions
- [func simd_recip(simd_float3) -> simd_float3](./simd_recip%28_%29-8jz2r.md)
  Returns the reciprocal of each element in a vector.
- [func recip(SIMD3<Float>) -> SIMD3<Float>](./recip%28_%29-8p7rb.md)
  Returns the reciprocal of each element in a vector.
- [func simd_fast_recip(simd_float3) -> simd_float3](./simd_fast_recip%28_%29-ohgm.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_precise_recip(simd_float3) -> simd_float3](./simd_precise_recip%28_%29-61j27.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_rsqrt(simd_float3) -> simd_float3](./simd_rsqrt%28_%29-rh1j.md)
  Returns the reciprocal square root of each element in a vector.
- [func rsqrt(SIMD3<Float>) -> SIMD3<Float>](./rsqrt%28_%29-6peaq.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_fast_rsqrt(simd_float3) -> simd_float3](./simd_fast_rsqrt%28_%29-80wq1.md)
  Returns the fast reciprocal square root of each element in a vector.
- [func simd_precise_rsqrt(simd_float3) -> simd_float3](./simd_precise_rsqrt%28_%29-zs51.md)
  Returns the precise reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_float3) -> simd_float3](./exp%28_%29-5nqcd.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_float3) -> simd_float3](./exp2%28_%29-85hb2.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_float3) -> simd_float3](./exp10%28_%29-6da66.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_float3) -> simd_float3](./expm1%28_%29-2r6sd.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_float3) -> simd_float3](./log%28_%29-3290g.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_float3) -> simd_float3](./log2%28_%29-5mgme.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_float3) -> simd_float3](./log10%28_%29-39t0j.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_float3) -> simd_float3](./log1p%28_%29-25ya0.md)
  Returns *log(1+x)* of each element in a vector.
### Geometry Functions
- [func cross(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./cross%28_,_%29-8xu8k.md)
  Returns the cross product of two vectors.
- [func dot(SIMD3<Float>, SIMD3<Float>) -> Float](./dot%28_,_%29-4gb9g.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD3<Float>) -> SIMD3<Float>](./normalize%28_%29-ac7.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD3<Float>, SIMD3<Float>) -> SIMD3<Float>](./project%28_,_%29-9ggyv.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD3<Float>, n: SIMD3<Float>) -> SIMD3<Float>](./reflect%28_,n%29-64cgz.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD3<Float>, n: SIMD3<Float>, eta: Float) -> SIMD3<Float>](./refract%28_,n,eta%29-7jv66.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
### Vector Norm Functions
- [func norm_one(SIMD3<Float>) -> Float](./norm_one%28_%29-7w7u6.md)
  Returns the sum of the absolute values of a vector.
- [func norm_inf(SIMD3<Float>) -> Float](./norm_inf%28_%29-6o26q.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [func length(SIMD3<Float>) -> Float](./length%28_%29-6t47g.md)
  Returns the length of a vector.
- [func length_squared(SIMD3<Float>) -> Float](./length_squared%28_%29-8odp0.md)
  Returns the square of the length of a vector.
- [func distance(SIMD3<Float>, SIMD3<Float>) -> Float](./distance%28_,_%29-8t6ut.md)
  Returns the distance between two vectors.
- [func distance_squared(SIMD3<Float>, SIMD3<Float>) -> Float](./distance_squared%28_,_%29-87jjy.md)
  Returns the square of the distance between two vectors.
### Hyperbolic Functions
- [func acosh(simd_float3) -> simd_float3](./acosh%28_%29-48wtu.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_float3) -> simd_float3](./asinh%28_%29-5c50h.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_float3) -> simd_float3](./atanh%28_%29-1y6z5.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_float3) -> simd_float3](./cosh%28_%29-4k02l.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_float3) -> simd_float3](./sinh%28_%29-15g8v.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_float3) -> simd_float3](./tanh%28_%29-4rx8s.md)
  Returns the hyperbolic tangent of each element in a vector.
### Logic Functions
- [func simd_select(simd_float3, simd_float3, simd_int3) -> simd_float3](./simd_select%28_,_,_%29-9gbqb.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_float3, simd_float3, simd_int3) -> simd_float3](./simd_bitselect%28_,_,_%29-5j5g8.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_float3) -> simd_float3](./cbrt%28_%29-6vcwl.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD3<Float>) -> SIMD3<Float>](./ceil%28_%29-580ar.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_float3) -> simd_float3](./erf%28_%29-2fow4.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_float3) -> simd_float3](./erfc%28_%29-7e6kk.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD3<Float>) -> SIMD3<Float>](./floor%28_%29-50q1o.md)
  Returns the floor of each element in a vector.
- [func fma(simd_float3, simd_float3, simd_float3) -> simd_float3](./fma%28_,_,_%29-22bjf.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_float3, simd_float3) -> simd_float3](./fmod%28_,_%29-3x8lc.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_float3, simd_float3) -> simd_float3](./hypot%28_,_%29-4xggy.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_float3) -> simd_float3](./lgamma%28_%29-7kgzo.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_float3, simd_float3) -> simd_float3](./nextafter%28_,_%29-ymwd.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_float3, simd_float3) -> simd_float3](./pow%28_,_%29-65mb9.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_float3, simd_float3) -> simd_float3](./remainder%28_,_%29-7ij10.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_float3) -> simd_float3](./round%28_%29-1tl5h.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_float3, simd_float3, simd_float3) -> simd_float3](./simd_muladd%28_,_,_%29-8a66m.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_float3) -> simd_float3](./tgamma%28_%29-6difz.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD3<Float>) -> SIMD3<Float>](./trunc%28_%29-9byjt.md)
  Returns each element in a vector rounded toward zero to the nearest integer.
### Trigonometric Functions
- [func acos(simd_float3) -> simd_float3](./acos%28_%29-8bwml.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_float3) -> simd_float3](./asin%28_%29-5t22r.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_float3) -> simd_float3](./atan%28_%29-3otbw.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_float3, simd_float3) -> simd_float3](./atan2%28_,_%29-40z9.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_float3) -> simd_float3](./cos%28_%29-2d0cu.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_float3) -> simd_float3](./cospi%28_%29-1ceix.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_float3) -> simd_float3](./sin%28_%29-78r0i.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_float3) -> simd_float3](./sinpi%28_%29-99o27.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_float3) -> (sin: simd_float3, cos: simd_float3)](./sincos%28_%29-3330.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_float3) -> (sin: simd_float3, cos: simd_float3)](./sincospi%28_%29-98kdl.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_float3) -> simd_float3](./tan%28_%29-yv9u.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_float3) -> simd_float3](./tanpi%28_%29-3lzzx.md)
  Returns the tangent of each element in a vector multiplied by pi.
### Classification Functions
- [func isfinite(simd_float3) -> simd_int3](./isfinite%28_%29-57mgu.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_float3) -> simd_int3](./isinf%28_%29-7fd4p.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_float3) -> simd_int3](./isnan%28_%29-j9kr.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_float3) -> simd_int3](./isnormal%28_%29-6f7tq.md)
  Returns true for each element that is normal in a vector.
### Alternative Type Alias
- [typealias vector_float3](./vector_float3.md)
  A floating point vector type used to perform physics calculations.
- [typealias float3](./float3.md)

## See Also

### Vector data types
- [typealias simd_float1](./simd_float1.md)
  A vector of one 32-bit floating-point element.
- [typealias simd_float2](./simd_float2.md)
  A vector of two 32-bit floating-point elements.
- [typealias simd_float4](./simd_float4.md)
  A vector of four 32-bit floating-point elements.
- [typealias simd_float8](./simd_float8.md)
  A vector of eight 32-bit floating-point elements.
- [typealias simd_float16](./simd_float16.md)
  A vector of sixteen 32-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float3)*