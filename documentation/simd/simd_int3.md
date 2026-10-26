# simd_int3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 32-bit signed integer elements.

## Declaration

```swift
typealias simd_int3 = SIMD3<Int32>
```

```c
typedef int __attribute__((ext_vector_type(3))) simd_int3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_int3(simd_int2) -> simd_int3](./simd_make_int3%28_%29-2tix4.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_int3(simd_int3) -> simd_int3](./simd_make_int3%28_%29-2r609.md)
  Returns a new vector from the specified vector.
- [func simd_make_int3(simd_int4) -> simd_int3](./simd_make_int3%28_%29-3fioe.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_int3(simd_int8) -> simd_int3](./simd_make_int3%28_%29-28n96.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_int3(simd_int16) -> simd_int3](./simd_make_int3%28_%29-4wbrt.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_int3_undef(simd_int2) -> simd_int3](./simd_make_int3_undef%28_%29-5kpok.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_int3(Int32) -> simd_int3](./simd_make_int3%28_%29-4pdxm.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_int3(Int32, Int32, Int32) -> simd_int3](./simd_make_int3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_int3_undef(Int32) -> simd_int3](./simd_make_int3_undef%28_%29-5q1nf.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector3](./vector3-8jq14.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_int3(simd_int2, Int32) -> simd_int3](./simd_make_int3%28_,_%29-7nox5.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_int3(Int32, simd_int2) -> simd_int3](./simd_make_int3%28_,_%29-48lb0.md)
  Returns a new vector from a scalar value and a vector.
- [vector3](./vector3-7wv2r.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_int3) -> simd_int3](./simd_abs%28_%29-8d4m3.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD3<Int32>) -> SIMD3<Int32>](./abs%28_%29-2m9bi.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_int3, simd_int3, simd_int3) -> simd_int3](./simd_clamp%28_,_,_%29-68p0z.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Int32>, min: Int32, max: Int32) -> SIMD3<Int32>](./clamp%28_,min,max%29-7b2i.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Int32>, min: SIMD3<Int32>, max: SIMD3<Int32>) -> SIMD3<Int32>](./clamp%28_,min,max%29-cim1.md)
  Returns each element in a vector clamped to a specified scalar range.
- [func simd_equal(simd_float3, simd_float3) -> simd_bool](./simd_equal%28_,_%29-6i7q4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_int3) -> Int32](./simd_reduce_min%28_%29-45ygx.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD3<Int32>) -> Int32](./reduce_min%28_%29-3l43s.md)
  Returns the minimum value in a vector.
- [func simd_reduce_max(simd_float3) -> Float](./simd_reduce_max%28_%29-4gy97.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD3<Int32>) -> Int32](./reduce_max%28_%29-5wvu6.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_int3) -> Int32](./simd_reduce_add%28_%29-2utmv.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD3<Int32>) -> Int32](./reduce_add%28_%29-9pjza.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_max(simd_int3, simd_int3) -> simd_int3](./simd_max%28_,_%29-93k3o.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD3<Int32>, Int32) -> SIMD3<Int32>](./max%28_,_%29-1zb5g.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD3<Int32>, SIMD3<Int32>) -> SIMD3<Int32>](./max%28_,_%29-1w3tf.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_int3, simd_int3) -> simd_int3](./simd_min%28_,_%29-2t446.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD3<Int32>, Int32) -> SIMD3<Int32>](./min%28_,_%29-8safl.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD3<Int32>, SIMD3<Int32>) -> SIMD3<Int32>](./min%28_,_%29-8p0ea.md)
  Returns the minimum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_int3) -> simd_bool](./simd_any%28_%29-69748.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_int3) -> simd_bool](./simd_all%28_%29-1apey.md)
  Returns true if the high-order bit of every element is set; false otherwise.
- [func simd_bitselect(simd_int3, simd_int3, simd_int3) -> simd_int3](./simd_bitselect%28_,_,_%29-78l7a.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias int3](./int3.md)
- [typealias vector_int3](./vector_int3.md)
### Functions to Create Three-Element Vectors From Vectors of Other Types
- [simd_int](./simd_int-9k08p.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_int](./simd_int-9ka9l.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_int](./simd_int-9jvcp.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_int](./simd_int-9k56h.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_int](./simd_int-9jx7l.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_int](./simd_int-9k71d.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_int](./simd_int-9jvmj.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_int](./simd_int-9k5ln.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_int](./simd_int-9k8m7.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_int](./simd_int-9k83f.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_int_sat](./simd_int_sat-6weo6.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_int_sat](./simd_int_sat-6w4w6.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_int_sat](./simd_int_sat-6w9t2.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_int_sat](./simd_int_sat-6vzom.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_int_sat](./simd_int_sat-6wgfu.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_int_sat](./simd_int_sat-6w6m2.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_int_sat](./simd_int_sat-6wfsi.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_int_sat](./simd_int_sat-6w5ki.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_int_sat](./simd_int_sat-6w3v2.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_int_sat](./simd_int_sat-6w3aa.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Round-Half-to-Even Conversion From Single-Precision Vectors
- [simd_int_rte](./simd_int_rte-8wkxz.md)
  Returns a new vector from the specified three-element vector.

## See Also

### Vector Data Types
- [typealias simd_int1](./simd_int1.md)
  A vector of one 32-bit signed integer element.
- [typealias simd_int2](./simd_int2.md)
  A vector of two 32-bit signed integer elements.
- [typealias simd_int4](./simd_int4.md)
  A vector of four 32-bit signed integer elements.
- [typealias simd_int8](./simd_int8.md)
  A vector of eight 32-bit signed integer elements.
- [typealias simd_int16](./simd_int16.md)
  A vector of sixteen 32-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_int3)*