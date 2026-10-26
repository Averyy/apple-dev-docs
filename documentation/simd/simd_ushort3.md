# simd_ushort3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 16-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ushort3 = SIMD3<UInt16>
```

```c
typedef unsigned short __attribute__((ext_vector_type(3))) simd_ushort3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_ushort3(simd_ushort2) -> simd_ushort3](./simd_make_ushort3%28_%29-80g2g.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_ushort3(simd_ushort3) -> simd_ushort3](./simd_make_ushort3%28_%29-7xag1.md)
  Returns a new vector from the specified vector.
- [func simd_make_ushort3(simd_ushort4) -> simd_ushort3](./simd_make_ushort3%28_%29-7u2h6.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_ushort3(simd_ushort8) -> simd_ushort3](./simd_make_ushort3%28_%29-7fbo6.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_ushort3(simd_ushort16) -> simd_ushort3](./simd_make_ushort3%28_%29-58w42.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_ushort3(simd_ushort32) -> simd_ushort3](./simd_make_ushort3%28_%29-11fhu.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_ushort3_undef(simd_ushort2) -> simd_ushort3](./simd_make_ushort3_undef%28_%29-6m2i9.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_ushort3(UInt16) -> simd_ushort3](./simd_make_ushort3%28_%29-93msa.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ushort3(UInt16, UInt16, UInt16) -> simd_ushort3](./simd_make_ushort3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_ushort3_undef(UInt16) -> simd_ushort3](./simd_make_ushort3_undef%28_%29-6cyga.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector3](./vector3-6gujk.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_ushort3(simd_ushort2, UInt16) -> simd_ushort3](./simd_make_ushort3%28_,_%29-3ap3r.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_ushort3(UInt16, simd_ushort2) -> simd_ushort3](./simd_make_ushort3%28_,_%29-9h935.md)
  Returns a new vector from a scalar value and a vector.
- [vector3](./vector3-5er36.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_clamp(simd_ushort3, simd_ushort3, simd_ushort3) -> simd_ushort3](./simd_clamp%28_,_,_%29-4akg3.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ushort3, simd_ushort3) -> simd_bool](./simd_equal%28_,_%29-9b270.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ushort3) -> UInt16](./simd_reduce_min%28_%29-46gdl.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ushort3) -> UInt16](./simd_reduce_max%28_%29-4h4s1.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ushort3) -> UInt16](./simd_reduce_add%28_%29-2vbub.md)
  Returns the sum of all elements in a vector.
### Extrema Function
- [func simd_min(simd_ushort3, simd_ushort3) -> simd_ushort3](./simd_min%28_,_%29-4jk8l.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ushort3, simd_ushort3) -> simd_ushort3](./simd_max%28_,_%29-4fcp5.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ushort3) -> simd_bool](./simd_any%28_%29-69p6w.md)
- [func simd_all(simd_ushort3) -> simd_bool](./simd_all%28_%29-1a7fa.md)
- [func simd_bitselect(simd_ushort3, simd_ushort3, simd_short3) -> simd_ushort3](./simd_bitselect%28_,_,_%29-7yglw.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ushort3](./vector_ushort3.md)
### Functions to Create Three-Element Vectors From Vectors of Other Types
- [simd_ushort](./simd_ushort-3fra2.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ushort](./simd_ushort-3g196.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-3fw9m.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ushort](./simd_ushort-3g656.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-3fudi.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ushort](./simd_ushort-3g492.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-3fvby.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ushort](./simd_ushort-3g5b2.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer element.
- [simd_ushort](./simd_ushort-3g22q.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ushort](./simd_ushort-3g2v2.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_ushort_sat](./simd_ushort_sat-7kfoj.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7kpib.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7kapv.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7kkoz.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7kipj.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7kstz.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7kk9d.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7kuc1.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer element.
- [simd_ushort_sat](./simd_ushort_sat-7kr89.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ushort_sat](./simd_ushort_sat-7kroh.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_ushort1](./simd_ushort1.md)
  A vector of one 16-bit unsigned integer element.
- [typealias simd_ushort2](./simd_ushort2.md)
  A vector of two 16-bit unsigned integer elements.
- [typealias simd_ushort4](./simd_ushort4.md)
  A vector of four 16-bit unsigned integer elements.
- [typealias simd_ushort8](./simd_ushort8.md)
  A vector of eight 16-bit unsigned integer elements.
- [typealias simd_ushort16](./simd_ushort16.md)
  A vector of sixteen 16-bit unsigned integer elements.
- [typealias simd_ushort32](./simd_ushort32.md)
  A vector of thirty-two 16-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ushort3)*