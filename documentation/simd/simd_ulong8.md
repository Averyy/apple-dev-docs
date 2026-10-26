# simd_ulong8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 64-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ulong8 = SIMD8<simd_ulong1>
```

```c
typedef unsigned long __attribute__((ext_vector_type(8))) simd_ulong8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_ulong8(simd_ulong2) -> simd_ulong8](./simd_make_ulong8%28_%29-5w0n4.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_ulong8(simd_ulong3) -> simd_ulong8](./simd_make_ulong8%28_%29-5zhz7.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_ulong8(simd_ulong4) -> simd_ulong8](./simd_make_ulong8%28_%29-6hggi.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_ulong8(simd_ulong8) -> simd_ulong8](./simd_make_ulong8%28_%29-6wa2m.md)
  Returns a new vector from the specified vector.
- [func simd_make_ulong8(simd_ulong4, simd_ulong4) -> simd_ulong8](./simd_make_ulong8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_ulong8_undef(simd_ulong2) -> simd_ulong8](./simd_make_ulong8_undef%28_%29-9rdt9.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_ulong8_undef(simd_ulong3) -> simd_ulong8](./simd_make_ulong8_undef%28_%29-9oge2.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_ulong8_undef(simd_ulong4) -> simd_ulong8](./simd_make_ulong8_undef%28_%29-d5pk.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [vector8](./vector8-5kkur.md)
  Returns a new vector from the specified vectors.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_ulong8(simd_ulong1) -> simd_ulong8](./simd_make_ulong8%28_%29-w5ee.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ulong8_undef(simd_ulong1) -> simd_ulong8](./simd_make_ulong8_undef%28_%29-73woc.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_ulong8, simd_ulong8, simd_ulong8) -> simd_ulong8](./simd_clamp%28_,_,_%29-6mt76.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ulong8, simd_ulong8) -> simd_bool](./simd_equal%28_,_%29-4dws0.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ulong8) -> simd_ulong1](./simd_reduce_min%28_%29-3oaqy.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ulong8) -> simd_ulong1](./simd_reduce_max%28_%29-55c36.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ulong8) -> simd_ulong1](./simd_reduce_add%28_%29-3avzc.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_ulong8, simd_ulong8) -> simd_ulong8](./simd_min%28_,_%29-1ynv5.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ulong8, simd_ulong8) -> simd_ulong8](./simd_max%28_,_%29-9mj3u.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ulong8) -> simd_bool](./simd_any%28_%29-6p9gh.md)
- [func simd_all(simd_ulong8) -> simd_bool](./simd_all%28_%29-1yolz.md)
- [func simd_bitselect(simd_ulong8, simd_ulong8, simd_long8) -> simd_ulong8](./simd_bitselect%28_,_,_%29-3xirg.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ulong8](./vector_ulong8.md)
### Functions to Create Eight-Element Vectors From Vectors of Other Types
- [simd_ulong](./simd_ulong-16dyy.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ulong](./simd_ulong-16o3e.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ulong](./simd_ulong-1692y.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ulong](./simd_ulong-16j3u.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ulong](./simd_ulong-16fzq.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ulong](./simd_ulong-16px2.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ulong](./simd_ulong-16eyu.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ulong](./simd_ulong-16oxy.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ulong](./simd_ulong-16n5e.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ulong](./simd_ulong-16mhi.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_ulong_sat](./simd_ulong_sat-nyps.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ulong_sat](./simd_ulong_sat-o8sg.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ulong_sat](./simd_ulong_sat-o3vk.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ulong_sat](./simd_ulong_sat-odsw.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ulong_sat](./simd_ulong_sat-nvpk.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ulong_sat](./simd_ulong_sat-o5oo.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ulong_sat](./simd_ulong_sat-nu30.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ulong_sat](./simd_ulong_sat-o3yk.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ulong_sat](./simd_ulong_sat-o7ac.md)
  Returns a new vector from the specified vector of 32-bit, floating point elements.
- [simd_ulong_sat](./simd_ulong_sat-o6mk.md)
  Returns a new vector from the specified vector of 64-bit, floating point elements.

## See Also

### Vector Data Types
- [typealias simd_ulong1](./simd_ulong1.md)
  A vector of one 64-bit unsigned integer element.
- [typealias simd_ulong2](./simd_ulong2.md)
  A vector of two 64-bit unsigned integer elements.
- [typealias simd_ulong3](./simd_ulong3.md)
  A vector of three 64-bit unsigned integer elements.
- [typealias simd_ulong4](./simd_ulong4.md)
  A vector of four 64-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ulong8)*