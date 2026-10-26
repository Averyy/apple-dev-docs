# simd_float4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 32-bit floating-point elements.

## Declaration

```swift
typealias simd_float4 = SIMD4<Float>
```

```c
typedef float __attribute__((ext_vector_type(4))) simd_float4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_float4(simd_float2) -> simd_float4](./simd_make_float4%28_%29-iuxp.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_float4(simd_float3) -> simd_float4](./simd_make_float4%28_%29-fyse.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_float4(simd_float4) -> simd_float4](./simd_make_float4%28_%29-cjxn.md)
  Returns a new vector from the specified vector.
- [func simd_make_float4(simd_float8) -> simd_float4](./simd_make_float4%28_%29-9xll2.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_float4(simd_float16) -> simd_float4](./simd_make_float4%28_%29-5sesp.md)
  Returns a new vector by truncating the specified 16-element vector.
- [func simd_make_float4(simd_float2, simd_float2) -> simd_float4](./simd_make_float4%28_,_%29-51w3j.md)
  Returns a new vector from the specified vectors.
- [func simd_make_float4_undef(simd_float2) -> simd_float4](./simd_make_float4_undef%28_%29-3brs5.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_float4_undef(simd_float3) -> simd_float4](./simd_make_float4_undef%28_%29-3f7tu.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_float4(Float) -> simd_float4](./simd_make_float4%28_%29-2ja7v.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_float4(Float, Float, Float, Float) -> simd_float4](./simd_make_float4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_float4_undef(Float) -> simd_float4](./simd_make_float4_undef%28_%29-24y7o.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_float4(Float, simd_float2, Float) -> simd_float4](./simd_make_float4%28_,_,_%29-5qr1r.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_float4(Float, Float, simd_float2) -> simd_float4](./simd_make_float4%28_,_,_%29-2rgt8.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_float4(Float, simd_float3) -> simd_float4](./simd_make_float4%28_,_%29-9ngva.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_float4(simd_float2, Float, Float) -> simd_float4](./simd_make_float4%28_,_,_%29-2bmi8.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_float4(simd_float3, Float) -> simd_float4](./simd_make_float4%28_,_%29-4911p.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_float4) -> simd_float4](./simd_abs%28_%29-81qo8.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD4<Float>) -> SIMD4<Float>](./abs%28_%29-1fzhv.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_float4, simd_float4, simd_float4) -> simd_float4](./simd_clamp%28_,_,_%29-6vmhh.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<Float>, min: Float, max: Float) -> SIMD4<Float>](./clamp%28_,min,max%29-46ay6.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<Float>, min: SIMD4<Float>, max: SIMD4<Float>) -> SIMD4<Float>](./clamp%28_,min,max%29-19q7w.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_float4, simd_float4) -> simd_bool](./simd_equal%28_,_%29-6sa26.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
- [func simd_fract(simd_float4) -> simd_float4](./simd_fract%28_%29-3w2rh.md)
  Returns the fractional part of each element in a vector.
- [func fract(SIMD4<Float>) -> SIMD4<Float>](./fract%28_%29-9s3df.md)
  Returns the fractional part of each element in a vector.
- [func simd_sign(simd_float4) -> simd_float4](./simd_sign%28_%29-74zwz.md)
  Returns the sign of each element in a vector.
- [func sign(SIMD4<Float>) -> SIMD4<Float>](./sign%28_%29-167c1.md)
  Returns the sign of each element in a vector.
- [func simd_step(simd_float4, simd_float4) -> simd_float4](./simd_step%28_,_%29-1fxwh.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
- [func step(SIMD4<Float>, edge: SIMD4<Float>) -> SIMD4<Float>](./step%28_,edge%29-8we4c.md)
  Returns zero for each element in a vector less than a specified edge, and otherwise returns one.
### Reduce Functions
- [func simd_reduce_add(simd_float4) -> Float](./simd_reduce_add%28_%29-2yn18.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD4<Float>) -> Float](./reduce_add%28_%29-8m4ir.md)
  Returns the sum of all elements in a vector.
- [func simd_reduce_max(simd_float4) -> Float](./simd_reduce_max%28_%29-4qug2.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD4<Float>) -> Float](./reduce_max%28_%29-263wv.md)
  Returns the maximum value in a vector.
- [func simd_reduce_min(simd_float4) -> Float](./simd_reduce_min%28_%29-4un1u.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD4<Float>) -> Float](./reduce_min%28_%29-1xt53.md)
  Returns the minimum value in a vector.
### Interpolation Functions
- [func simd_mix(simd_float4, simd_float4, simd_float4) -> simd_float4](./simd_mix%28_,_,_%29-5fpv1.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Float>, SIMD4<Float>, t: Float) -> SIMD4<Float>](./mix%28_,_,t%29-2uufx.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Float>, SIMD4<Float>, t: SIMD4<Float>) -> SIMD4<Float>](./mix%28_,_,t%29-8qz2g.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_float4, simd_float4, simd_float4) -> simd_float4](./simd_smoothstep%28_,_,_%29-33ugy.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD4<Float>, edge0: SIMD4<Float>, edge1: SIMD4<Float>) -> SIMD4<Float>](./smoothstep%28_,edge0,edge1%29-3gx0q.md)
  Returns an element-wise smoothly interpolated value between two vectors.
### Extrema Functions
- [func simd_max(simd_float4, simd_float4) -> simd_float4](./simd_max%28_,_%29-3mrbf.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD4<Float>, Float) -> SIMD4<Float>](./max%28_,_%29-8mn3g.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD4<Float>, SIMD4<Float>) -> SIMD4<Float>](./max%28_,_%29-317vz.md)
  Returns the maximum value of each element in a vector.
- [func fmax(SIMD4<Float>, SIMD4<Float>) -> SIMD4<Float>](./fmax%28_,_%29-7f29b.md)
- [func simd_min(simd_float4, simd_float4) -> simd_float4](./simd_min%28_,_%29-6upge.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD4<Float>, Float) -> SIMD4<Float>](./min%28_,_%29-2jw3s.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD4<Float>, SIMD4<Float>) -> SIMD4<Float>](./min%28_,_%29-7wmdr.md)
  Returns the minimum value of each element in a vector.
- [func fmin(SIMD4<Float>, SIMD4<Float>) -> SIMD4<Float>](./fmin%28_,_%29-47ii0.md)
### Reciprocal and Reciprocal Square Root Functions
- [func simd_recip(simd_float4) -> simd_float4](./simd_recip%28_%29-820ma.md)
  Returns the reciprocal of each element in a vector.
- [func recip(SIMD4<Float>) -> SIMD4<Float>](./recip%28_%29-3idnw.md)
  Returns the reciprocal of each element in a vector.
- [func simd_rsqrt(simd_float4) -> simd_float4](./simd_rsqrt%28_%29-i4we.md)
  Returns the reciprocal square root of each element in a vector.
- [func rsqrt(SIMD4<Float>) -> SIMD4<Float>](./rsqrt%28_%29-3g5ej.md)
  Returns the reciprocal square root of each element in a vector.
- [func simd_precise_recip(simd_float4) -> simd_float4](./simd_precise_recip%28_%29-6ptoq.md)
  Returns the precise reciprocal of each element in a vector.
- [func simd_precise_rsqrt(simd_float4) -> simd_float4](./simd_precise_rsqrt%28_%29-136xw.md)
  Returns the precise reciprocal square root of each element in a vector.
- [func simd_fast_recip(simd_float4) -> simd_float4](./simd_fast_recip%28_%29-6nf.md)
  Returns the fast reciprocal of each element in a vector.
- [func simd_fast_rsqrt(simd_float4) -> simd_float4](./simd_fast_rsqrt%28_%29-8p7fk.md)
  Returns the fast reciprocal square root of each element in a vector.
### Exponential and Logarithmic Functions
- [func exp(simd_float4) -> simd_float4](./exp%28_%29-8lp9u.md)
  Returns *e* raised to the power of each element in a vector.
- [func exp2(simd_float4) -> simd_float4](./exp2%28_%29-4tmv0.md)
  Returns 2 raised to the power of each element in a vector.
- [func exp10(simd_float4) -> simd_float4](./exp10%28_%29-7ddho.md)
  Returns 10 raised to the power of each element in a vector.
- [func expm1(simd_float4) -> simd_float4](./expm1%28_%29-4f45.md)
  Returns *eˣ-1* for each element in a vector.
- [func log(simd_float4) -> simd_float4](./log%28_%29-259z1.md)
  Returns the natural logarithm of each element in a vector.
- [func log2(simd_float4) -> simd_float4](./log2%28_%29-5gt2x.md)
  Returns the base 2 logarithm of each element in a vector.
- [func log10(simd_float4) -> simd_float4](./log10%28_%29-2lowj.md)
  Returns the base 10 logarithm of each element in a vector.
- [func log1p(simd_float4) -> simd_float4](./log1p%28_%29-77wue.md)
  Returns *log(1+x)* of each element in a vector.
### Geometry Functions
- [func dot(SIMD4<Float>, SIMD4<Float>) -> Float](./dot%28_,_%29-47df.md)
  Returns the dot product of two vectors.
- [func normalize(SIMD4<Float>) -> SIMD4<Float>](./normalize%28_%29-6g9xc.md)
  Returns a vector pointing in the same direction of the supplied vector with a length of 1.
- [func project(SIMD4<Float>, SIMD4<Float>) -> SIMD4<Float>](./project%28_,_%29-pdsh.md)
  Returns the first vector projected onto the second vector.
- [func reflect(SIMD4<Float>, n: SIMD4<Float>) -> SIMD4<Float>](./reflect%28_,n%29-8i5cc.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [func refract(SIMD4<Float>, n: SIMD4<Float>, eta: Float) -> SIMD4<Float>](./refract%28_,n,eta%29-8qo9c.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.
### Vector Norm Functions
- [func norm_one(SIMD4<Float>) -> Float](./norm_one%28_%29-jo3r.md)
  Returns the sum of the absolute values of a vector.
- [func norm_inf(SIMD4<Float>) -> Float](./norm_inf%28_%29-8tppa.md)
  Returns the maximum absolute value of a vector.
### Length and Distance Functions
- [func length(SIMD4<Float>) -> Float](./length%28_%29-9i1zg.md)
  Returns the length of a vector.
- [func length_squared(SIMD4<Float>) -> Float](./length_squared%28_%29-80gxf.md)
  Returns the square of the length of a vector.
- [func distance(SIMD4<Float>, SIMD4<Float>) -> Float](./distance%28_,_%29-39uat.md)
  Returns the distance between two vectors.
- [func distance_squared(SIMD4<Float>, SIMD4<Float>) -> Float](./distance_squared%28_,_%29-32wfg.md)
  Returns the square of the distance between two vectors.
### Hyperbolic Functions
- [func acosh(simd_float4) -> simd_float4](./acosh%28_%29-7sio6.md)
  Returns the inverse hyperbolic cosine of each element in a vector.
- [func asinh(simd_float4) -> simd_float4](./asinh%28_%29-693z8.md)
  Returns the inverse hyperbolic sine of each element in a vector.
- [func atanh(simd_float4) -> simd_float4](./atanh%28_%29-48wed.md)
  Returns the inverse hyperbolic tangent of each element in a vector.
- [func cosh(simd_float4) -> simd_float4](./cosh%28_%29-5k3hp.md)
  Returns the hyperbolic cosine of each element in a vector.
- [func sinh(simd_float4) -> simd_float4](./sinh%28_%29-4eoxy.md)
  Returns the hyperbolic sine of each element in a vector.
- [func tanh(simd_float4) -> simd_float4](./tanh%28_%29-9p88r.md)
  Returns the hyperbolic tangent of each element in a vector.
### Logic Functions
- [func simd_select(simd_float4, simd_float4, simd_int4) -> simd_float4](./simd_select%28_,_,_%29-7vjx6.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element’s high-order bit in the mask.
- [func simd_bitselect(simd_float4, simd_float4, simd_int4) -> simd_float4](./simd_bitselect%28_,_,_%29-7g1os.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Math Functions
- [func cbrt(simd_float4) -> simd_float4](./cbrt%28_%29-5wdps.md)
  Returns the cube root of each element in a vector.
- [func ceil(SIMD4<Float>) -> SIMD4<Float>](./ceil%28_%29-2omh0.md)
  Returns the ceiling of each element in a vector.
- [func erf(simd_float4) -> simd_float4](./erf%28_%29-4zsot.md)
  Returns the error function for each element in a vector.
- [func erfc(simd_float4) -> simd_float4](./erfc%28_%29-7acqr.md)
  Returns the complementary error function for each element in a vector.
- [func floor(SIMD4<Float>) -> SIMD4<Float>](./floor%28_%29-56de3.md)
  Returns the floor of each element in a vector.
- [func fma(simd_float4, simd_float4, simd_float4) -> simd_float4](./fma%28_,_,_%29-1zefy.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func fmod(simd_float4, simd_float4) -> simd_float4](./fmod%28_,_%29-px8m.md)
  Returns the modulus after dividing each element in a vector by the corresponding element in a second vector.
- [func hypot(simd_float4, simd_float4) -> simd_float4](./hypot%28_,_%29-96sjx.md)
  Returns the hypotenuse of a right-angled triangle with the sides that are adjacent to the right angle that two vectors define.
- [func lgamma(simd_float4) -> simd_float4](./lgamma%28_%29-3l63e.md)
  Returns the natural logarithm of the absolute value of the gamma function of each element in a vector.
- [func nextafter(simd_float4, simd_float4) -> simd_float4](./nextafter%28_,_%29-6sc0p.md)
  Returns the next representable value of each element in a vector in the direction of the corresponding element in a second vector.
- [func pow(simd_float4, simd_float4) -> simd_float4](./pow%28_,_%29-skyu.md)
  Returns each element in a vector raised to the power of the corresponding element in a second vector.
- [func remainder(simd_float4, simd_float4) -> simd_float4](./remainder%28_,_%29-7o61f.md)
  Returns the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func round(simd_float4) -> simd_float4](./round%28_%29-8vqnv.md)
  Returns each element in a vector rounded to the nearest integer.
- [func simd_muladd(simd_float4, simd_float4, simd_float4) -> simd_float4](./simd_muladd%28_,_,_%29-3e79w.md)
  Returns the multiply-add result for corresponding elements in three vectors.
- [func tgamma(simd_float4) -> simd_float4](./tgamma%28_%29-twdo.md)
  Returns the gamma function for each element in a vector.
- [func trunc(SIMD4<Float>) -> SIMD4<Float>](./trunc%28_%29-4xiyl.md)
  Returns each element in a vector rounded toward zero to the nearest integer.
### Trigonometric Functions
- [func acos(simd_float4) -> simd_float4](./acos%28_%29-2blze.md)
  Returns the arccosine of each element in a vector.
- [func asin(simd_float4) -> simd_float4](./asin%28_%29-87ban.md)
  Returns the arcsine of each element in a vector.
- [func atan(simd_float4) -> simd_float4](./atan%28_%29-8xa90.md)
  Returns the arctangent of each element in a vector.
- [func atan2(simd_float4, simd_float4) -> simd_float4](./atan2%28_,_%29-63ije.md)
  Returns the arctangent of each pair of corresponding elements in two vectors.
- [func cos(simd_float4) -> simd_float4](./cos%28_%29-8qcj2.md)
  Returns the cosine of each element in a vector.
- [func cospi(simd_float4) -> simd_float4](./cospi%28_%29-5chnf.md)
  Returns the cosine of each element in a vector multiplied by pi.
- [func sin(simd_float4) -> simd_float4](./sin%28_%29-80x4.md)
  Returns the sine of each element in a vector.
- [func sinpi(simd_float4) -> simd_float4](./sinpi%28_%29-71xz.md)
  Returns the sine of each element in a vector multiplied by pi.
- [func sincos(simd_float4) -> (sin: simd_float4, cos: simd_float4)](./sincos%28_%29-8bfn1.md)
  Returns the sine and cosine of each element in a vector.
- [func sincospi(simd_float4) -> (sin: simd_float4, cos: simd_float4)](./sincospi%28_%29-84wzt.md)
  Returns the sine and cosine of each element in a vector multiplied by pi.
- [func tan(simd_float4) -> simd_float4](./tan%28_%29-7uvy9.md)
  Returns the tangent of each element in a vector.
- [func tanpi(simd_float4) -> simd_float4](./tanpi%28_%29-93eul.md)
  Returns the tangent of each element in a vector multiplied by pi.
### Classification Functions
- [func isfinite(simd_float4) -> simd_int4](./isfinite%28_%29-96ccc.md)
  Returns true for each element that is finite in a vector.
- [func isinf(simd_float4) -> simd_int4](./isinf%28_%29-4hqza.md)
  Returns true for each element that is infinite in a vector.
- [func isnan(simd_float4) -> simd_int4](./isnan%28_%29-9epap.md)
  Returns true for each element that is not a number (NaN) in a vector.
- [func isnormal(simd_float4) -> simd_int4](./isnormal%28_%29-7428z.md)
  Returns true for each element that is normal in a vector.
### Alternative Type Alias
- [typealias vector_float4](./vector_float4.md)
- [typealias float4](./float4.md)

## See Also

### Vector data types
- [typealias simd_float1](./simd_float1.md)
  A vector of one 32-bit floating-point element.
- [typealias simd_float2](./simd_float2.md)
  A vector of two 32-bit floating-point elements.
- [typealias simd_float3](./simd_float3.md)
  A vector of three 32-bit floating-point elements.
- [typealias simd_float8](./simd_float8.md)
  A vector of eight 32-bit floating-point elements.
- [typealias simd_float16](./simd_float16.md)
  A vector of sixteen 32-bit floating-point elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_float4)*