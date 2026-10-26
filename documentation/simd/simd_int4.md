# simd_int4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 32-bit signed integer elements.

## Declaration

```swift
typealias simd_int4 = SIMD4<Int32>
```

```c
typedef int __attribute__((ext_vector_type(4))) simd_int4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_int4(simd_int2) -> simd_int4](./simd_make_int4%28_%29-1suou.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_int4(simd_int3) -> simd_int4](./simd_make_int4%28_%29-1wbev.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_int4(simd_int4) -> simd_int4](./simd_make_int4%28_%29-1kx2w.md)
  Returns a new vector from the specified vector.
- [func simd_make_int4(simd_int8) -> simd_int4](./simd_make_int4%28_%29-2qk04.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_int4(simd_int16) -> simd_int4](./simd_make_int4%28_%29-2rtb0.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_int4(simd_int2, simd_int2) -> simd_int4](./simd_make_int4%28_,_%29-4phxy.md)
  Returns a new vector from the specified vectors.
- [func simd_make_int4_undef(simd_int2) -> simd_int4](./simd_make_int4_undef%28_%29-5g92f.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_int4_undef(simd_int3) -> simd_int4](./simd_make_int4_undef%28_%29-5dw9q.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [vector4](./vector4-6k3t7.md)
  Returns a new vector from the specified vectors.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_int4(Int32) -> simd_int4](./simd_make_int4%28_%29-7vwve.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_int4(Int32, Int32, Int32, Int32) -> simd_int4](./simd_make_int4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_int4_undef(Int32) -> simd_int4](./simd_make_int4_undef%28_%29-2wt72.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector4](./vector4-7j5gn.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_int4(simd_int2, Int32, Int32) -> simd_int4](./simd_make_int4%28_,_,_%29-7cjm7.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_int4(simd_int3, Int32) -> simd_int4](./simd_make_int4%28_,_%29-7rrqd.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_int4(Int32, Int32, simd_int2) -> simd_int4](./simd_make_int4%28_,_,_%29-9tjlm.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_int4(Int32, simd_int2, Int32) -> simd_int4](./simd_make_int4%28_,_,_%29-8of8y.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_int4(Int32, simd_int3) -> simd_int4](./simd_make_int4%28_,_%29-6p0ui.md)
  Returns a new vector from a scalar value and a vector.
- [vector4](./vector4-6wxif.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_int4) -> simd_int4](./simd_abs%28_%29-81glw.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD4<Int32>) -> SIMD4<Int32>](./abs%28_%29-1b3qo.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_int4, simd_int4, simd_int4) -> simd_int4](./simd_clamp%28_,_,_%29-50obl.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<Int32>, min: Int32, max: Int32) -> SIMD4<Int32>](./clamp%28_,min,max%29-5if3n.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<Int32>, min: SIMD4<Int32>, max: SIMD4<Int32>) -> SIMD4<Int32>](./clamp%28_,min,max%29-5f538.md)
  Returns each element in a vector clamped to a specified scalar range.
- [func simd_equal(simd_int4, simd_int4) -> simd_bool](./simd_equal%28_,_%29-2rypj.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_int4) -> Int32](./simd_reduce_min%28_%29-4uaza.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD4<Int32>) -> Int32](./reduce_min%28_%29-6npco.md)
  Returns the minimum value in a vector.
- [func simd_reduce_max(simd_int4) -> Int32](./simd_reduce_max%28_%29-4qjkm.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD4<Int32>) -> Int32](./reduce_max%28_%29-5afy1.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_int4) -> Int32](./simd_reduce_add%28_%29-2ybq8.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD4<Int32>) -> Int32](./reduce_add%28_%29-89ptt.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_max(simd_int4, simd_int4) -> simd_int4](./simd_max%28_,_%29-51txy.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD4<Int32>, Int32) -> SIMD4<Int32>](./max%28_,_%29-696e3.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD4<Int32>, SIMD4<Int32>) -> SIMD4<Int32>](./max%28_,_%29-6cb9k.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_int4, simd_int4) -> simd_int4](./simd_min%28_,_%29-1m8ma.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD4<Int32>, Int32) -> SIMD4<Int32>](./min%28_,_%29-5uuf6.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD4<Int32>, SIMD4<Int32>) -> SIMD4<Int32>](./min%28_,_%29-5y1sd.md)
  Returns the minimum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_int4) -> simd_bool](./simd_any%28_%29-6cp1b.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_int4) -> simd_bool](./simd_all%28_%29-1jw6t.md)
  Returns true if the high-order bit of every element is set; false otherwise.
- [func simd_bitselect(simd_int4, simd_int4, simd_int4) -> simd_int4](./simd_bitselect%28_,_,_%29-27mh1.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias int4](./int4.md)
- [typealias vector_int4](./vector_int4.md)
### Functions to Create Four-Element Vectors From Vectors of Other Types
- [simd_int](./simd_int-9gib6.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_int](./simd_int-9gsc2.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_int](./simd_int-9gnaq.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_int](./simd_int-9gx82.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_int](./simd_int-9gf7q.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_int](./simd_int-9gp3a.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_int](./simd_int-9ggra.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_int](./simd_int-9gqqe.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_int](./simd_int-9gtqi.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_int](./simd_int-9gt5y.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_int_sat](./simd_int_sat-6820l.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_int_sat](./simd_int_sat-67sad.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_int_sat](./simd_int_sat-67x4l.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_int_sat](./simd_int_sat-67nat.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_int_sat](./simd_int_sat-68459.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_int_sat](./simd_int_sat-67tx9.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_int_sat](./simd_int_sat-684sf.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_int_sat](./simd_int_sat-67uyn.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_int_sat](./simd_int_sat-67t8j.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_int_sat](./simd_int_sat-67sbj.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Round-Half-to-Even Conversion From Single-Precision Vectors
- [simd_int_rte](./simd_int_rte-8emhi.md)
  Returns a new vector from the specified four-element vector.

## See Also

### Vector Data Types
- [typealias simd_int1](./simd_int1.md)
  A vector of one 32-bit signed integer element.
- [typealias simd_int2](./simd_int2.md)
  A vector of two 32-bit signed integer elements.
- [typealias simd_int3](./simd_int3.md)
  A vector of three 32-bit signed integer elements.
- [typealias simd_int8](./simd_int8.md)
  A vector of eight 32-bit signed integer elements.
- [typealias simd_int16](./simd_int16.md)
  A vector of sixteen 32-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_int4)*