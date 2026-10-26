# simd_short3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 16-bit signed integer elements.

## Declaration

```swift
typealias simd_short3 = SIMD3<Int16>
```

```c
typedef short __attribute__((ext_vector_type(3))) simd_short3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_short3(simd_short2) -> simd_short3](./simd_make_short3%28_%29-c59z.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_short3(simd_short3) -> simd_short3](./simd_make_short3%28_%29-gyam.md)
  eturns a new vector from the specified vector.
- [func simd_make_short3(simd_short4) -> simd_short3](./simd_make_short3%28_%29-x9n1.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_short3(simd_short8) -> simd_short3](./simd_make_short3%28_%29-1capt.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_short3(simd_short16) -> simd_short3](./simd_make_short3%28_%29-9l6v8.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_short3(simd_short32) -> simd_short3](./simd_make_short3%28_%29-70om7.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_short3_undef(simd_short2) -> simd_short3](./simd_make_short3_undef%28_%29-87ju7.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_short3(Int16) -> simd_short3](./simd_make_short3%28_%29-2ux4i.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_short3(Int16, Int16, Int16) -> simd_short3](./simd_make_short3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_short3_undef(Int16) -> simd_short3](./simd_make_short3_undef%28_%29-5n83n.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector3](./vector3-3x8j.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_short3(simd_short2, Int16) -> simd_short3](./simd_make_short3%28_,_%29-7dmp4.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_short3(Int16, simd_short2) -> simd_short3](./simd_make_short3%28_,_%29-9bk9v.md)
  Returns a new vector from a scalar value and a vector.
- [vector3](./vector3-3833i.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_short3) -> simd_short3](./simd_abs%28_%29-8d6jr.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_short3, simd_short3, simd_short3) -> simd_short3](./simd_clamp%28_,_,_%29-7wmh7.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_short3, simd_short3) -> simd_bool](./simd_equal%28_,_%29-40ux3.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_short3) -> Int16](./simd_reduce_min%28_%29-466g9.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_short3) -> Int16](./simd_reduce_max%28_%29-4hewh.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_short3) -> Int16](./simd_reduce_add%28_%29-2v1tf.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_short3, simd_short3) -> simd_short3](./simd_min%28_,_%29-9vz62.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_short3, simd_short3) -> simd_short3](./simd_max%28_,_%29-8id6w.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_short3) -> simd_bool](./simd_any%28_%29-69f7s.md)
- [func simd_all(simd_short3) -> simd_bool](./simd_all%28_%29-1ahau.md)
- [func simd_bitselect(simd_short3, simd_short3, simd_short3) -> simd_short3](./simd_bitselect%28_,_,_%29-8m8ti.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_short3](./vector_short3.md)
### Functions to Create Three-Element Vectors From Vectors of Other Types
- [simd_short](./simd_short-6hhh3.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_short](./simd_short-6hrav.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_short](./simd_short-6hmgn.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_short](./simd_short-6hw6v.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements
- [simd_short](./simd_short-6he6b.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_short](./simd_short-6ho1v.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_short](./simd_short-6hfx5.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_short](./simd_short-6hpp5.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_short](./simd_short-6hswh.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_short](./simd_short-6hsc9.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_short_sat](./simd_short_sat-3ixry.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-3j7lq.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-3j2pq.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-3jcji.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements
- [simd_short_sat](./simd_short_sat-3izgq.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-3j9fu.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-3iy1u.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-3j7vm.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-3j652.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_short_sat](./simd_short_sat-3j5f6.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_short1](./simd_short1.md)
  A vector of one 16-bit signed integer element.
- [typealias simd_short2](./simd_short2.md)
  A vector of two 16-bit signed integer elements.
- [typealias simd_short4](./simd_short4.md)
  A vector of four 16-bit signed integer elements.
- [typealias simd_short8](./simd_short8.md)
  A vector of eight 16-bit signed integer elements.
- [typealias simd_short16](./simd_short16.md)
  A vector of sixteen 16-bit signed integer elements.
- [typealias simd_short32](./simd_short32.md)
  A vector of thirty-two 16-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_short3)*