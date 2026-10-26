# simd_uchar8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 8-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uchar8 = SIMD8<UInt8>
```

```c
typedef unsigned char __attribute__((ext_vector_type(8))) simd_uchar8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_uchar8(simd_uchar2) -> simd_uchar8](./simd_make_uchar8%28_%29-5zumf.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uchar8(simd_uchar3) -> simd_uchar8](./simd_make_uchar8%28_%29-62sn2.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_uchar8(simd_uchar4) -> simd_uchar8](./simd_make_uchar8%28_%29-65qph.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_uchar8(simd_uchar8) -> simd_uchar8](./simd_make_uchar8%28_%29-51mi9.md)
  Returns a new vector from the specified vector.
- [func simd_make_uchar8(simd_uchar16) -> simd_uchar8](./simd_make_uchar8%28_%29-5p2su.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_uchar8(simd_uchar32) -> simd_uchar8](./simd_make_uchar8%28_%29-6svfy.md)
  Returns a new vector by truncating the specified thrity two-element vector.
- [func simd_make_uchar8(simd_uchar64) -> simd_uchar8](./simd_make_uchar8%28_%29-75pea.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_uchar8(simd_uchar4, simd_uchar4) -> simd_uchar8](./simd_make_uchar8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_uchar8_undef(simd_uchar2) -> simd_uchar8](./simd_make_uchar8_undef%28_%29-19t4r.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_uchar8_undef(simd_uchar3) -> simd_uchar8](./simd_make_uchar8_undef%28_%29-14ngi.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_uchar8_undef(simd_uchar4) -> simd_uchar8](./simd_make_uchar8_undef%28_%29-ovyp.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [vector8](./vector8-5xlzy.md)
  Returns a new vector from the specified vectors.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_uchar8(UInt8) -> simd_uchar8](./simd_make_uchar8%28_%29-9e791.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uchar8_undef(UInt8) -> simd_uchar8](./simd_make_uchar8_undef%28_%29-3cvtm.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_uchar8, simd_uchar8, simd_uchar8) -> simd_uchar8](./simd_clamp%28_,_,_%29-1uiyw.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uchar8, simd_uchar8) -> simd_bool](./simd_equal%28_,_%29-5o6ip.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uchar8) -> UInt8](./simd_reduce_min%28_%29-3oc92.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_uchar8) -> UInt8](./simd_reduce_max%28_%29-55cku.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uchar8) -> UInt8](./simd_reduce_add%28_%29-3ay64.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uchar8, simd_uchar8) -> simd_uchar8](./simd_min%28_,_%29-8ibca.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uchar8, simd_uchar8) -> simd_uchar8](./simd_max%28_,_%29-7b9mk.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uchar8) -> simd_bool](./simd_any%28_%29-6pbmv.md)
- [func simd_all(simd_uchar8) -> simd_bool](./simd_all%28_%29-1yp2h.md)
- [func simd_bitselect(simd_uchar8, simd_uchar8, simd_char8) -> simd_uchar8](./simd_bitselect%28_,_,_%29-9gyx6.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_uchar8](./vector_uchar8.md)
### Functions to Create Eight-Element Vectors From Vectors of Other Types
- [simd_uchar](./simd_uchar-83fp8.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_uchar](./simd_uchar-83px8.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_uchar](./simd_uchar-83arg.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_uchar](./simd_uchar-83kzg.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_uchar](./simd_uchar-83dz8.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_uchar](./simd_uchar-83nr8.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_uchar](./simd_uchar-83cy0.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_uchar](./simd_uchar-83n48.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_uchar](./simd_uchar-83ovk.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_uchar](./simd_uchar-83pew.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_uchar_sat](./simd_uchar_sat-18rfe.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_uchar_sat](./simd_uchar_sat-1917e.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_uchar_sat](./simd_uchar_sat-18wbe.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_uchar_sat](./simd_uchar_sat-196e2.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_uchar_sat](./simd_uchar_sat-18ufi.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_uchar_sat](./simd_uchar_sat-194b2.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_uchar_sat](./simd_uchar_sat-18svq.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_uchar_sat](./simd_uchar_sat-192t2.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_uchar_sat](./simd_uchar_sat-18zuq.md)
  Returns a new vector from the specified vector of 32-bit, floating point elements.
- [simd_uchar_sat](./simd_uchar_sat-190iu.md)
  Returns a new vector from the specified vector of 64-bit, floating point elements.

## See Also

### Vector Data Types
- [typealias simd_uchar1](./simd_uchar1.md)
  A vector of one 8-bit unsigned integer element.
- [typealias simd_uchar2](./simd_uchar2.md)
  A vector of two 8-bit unsigned integer elements.
- [typealias simd_uchar3](./simd_uchar3.md)
  A vector of three 8-bit unsigned integer elements.
- [typealias simd_uchar4](./simd_uchar4.md)
  A vector of four 8-bit unsigned integer elements.
- [typealias simd_uchar16](./simd_uchar16.md)
  A vector of sixteen 8-bit unsigned integer elements.
- [typealias simd_uchar32](./simd_uchar32.md)
  A vector of thirty-two 8-bit unsigned integer elements.
- [typealias simd_uchar64](./simd_uchar64.md)
  A vector of sixty-four 8-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uchar8)*