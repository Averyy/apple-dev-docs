# simd_ushort4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 16-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ushort4 = SIMD4<UInt16>
```

```c
typedef unsigned short __attribute__((ext_vector_type(4))) simd_ushort4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_ushort4(simd_ushort2) -> simd_ushort4](./simd_make_ushort4%28_%29-35tv2.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_ushort4(simd_ushort3) -> simd_ushort4](./simd_make_ushort4%28_%29-38zbb.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_ushort4(simd_ushort4) -> simd_ushort4](./simd_make_ushort4%28_%29-3qyfo.md)
  Returns a new vector from the specified vector.
- [func simd_make_ushort4(simd_ushort8) -> simd_ushort4](./simd_make_ushort4%28_%29-45zew.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_ushort4(simd_ushort16) -> simd_ushort4](./simd_make_ushort4%28_%29-2aylo.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_ushort4(simd_ushort32) -> simd_ushort4](./simd_make_ushort4%28_%29-7bisx.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_ushort4(simd_ushort2, simd_ushort2) -> simd_ushort4](./simd_make_ushort4%28_,_%29-33b7a.md)
  Returns a new vector from the specified vectors.
- [func simd_make_ushort4_undef(simd_ushort2) -> simd_ushort4](./simd_make_ushort4_undef%28_%29-263ji.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_ushort4_undef(simd_ushort3) -> simd_ushort4](./simd_make_ushort4_undef%28_%29-22y87.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [vector4](./vector4-stby.md)
  Returns a new vector from the specified vectors.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_ushort4(UInt16) -> simd_ushort4](./simd_make_ushort4%28_%29-85y03.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ushort4(UInt16, UInt16, UInt16, UInt16) -> simd_ushort4](./simd_make_ushort4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_ushort4_undef(UInt16) -> simd_ushort4](./simd_make_ushort4_undef%28_%29-9xmiv.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector4](./vector4-vklr.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_ushort4(simd_ushort2, UInt16, UInt16) -> simd_ushort4](./simd_make_ushort4%28_,_,_%29-5tiuy.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_ushort4(simd_ushort3, UInt16) -> simd_ushort4](./simd_make_ushort4%28_,_%29-44sd1.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_ushort4(UInt16, UInt16, simd_ushort2) -> simd_ushort4](./simd_make_ushort4%28_,_,_%29-3yjly.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_ushort4(UInt16, simd_ushort2, UInt16) -> simd_ushort4](./simd_make_ushort4%28_,_,_%29-53g72.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_ushort4(UInt16, simd_ushort3) -> simd_ushort4](./simd_make_ushort4%28_,_%29-4t4aq.md)
  Returns a new vector from a scalar value and a vector.
- [vector4](./vector4-34nn6.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_clamp(simd_ushort4, simd_ushort4, simd_ushort4) -> simd_ushort4](./simd_clamp%28_,_,_%29-72wjb.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ushort4, simd_ushort4) -> simd_bool](./simd_equal%28_,_%29-9613j.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ushort4) -> UInt16](./simd_reduce_min%28_%29-4usy2.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ushort4) -> UInt16](./simd_reduce_max%28_%29-4qq8a.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ushort4) -> UInt16](./simd_reduce_add%28_%29-2yjso.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_ushort4, simd_ushort4) -> simd_ushort4](./simd_min%28_,_%29-9tvdl.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ushort4, simd_ushort4) -> simd_ushort4](./simd_max%28_,_%29-64jwl.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ushort4) -> simd_bool](./simd_any%28_%29-6cx6b.md)
- [func simd_all(simd_ushort4) -> simd_bool](./simd_all%28_%29-1jswd.md)
- [func simd_bitselect(simd_ushort4, simd_ushort4, simd_short4) -> simd_ushort4](./simd_bitselect%28_,_,_%29-ryof.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ushort4](./vector_ushort4.md)
### Functions to Create Four-Element Vectors From Vectors of Other Types
- [simd_ushort](./simd_ushort-2yc4p.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ushort](./simd_ushort-2y23t.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-2ygzt.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ushort](./simd_ushort-2y70p.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-2yf49.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ushort](./simd_ushort-2y555.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-2ygrr.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ushort](./simd_ushort-2y6qv.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-2y3qr.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ushort](./simd_ushort-2y4af.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_ushort_sat](./simd_ushort_sat-82yk0.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-82omo.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-82tkg.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-82ju8.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-831o8.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-82ry0.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-832ro.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-82slg.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-82pos.md)
  Returns a new vector from the specified vector of 32-bit, floating point elements.
- [simd_ushort_sat](./simd_ushort_sat-82qc4.md)
  Returns a new vector from the specified vector of 64-bit, floating point elements.

## See Also

### Vector Data Types
- [typealias simd_ushort1](./simd_ushort1.md)
  A vector of one 16-bit unsigned integer element.
- [typealias simd_ushort2](./simd_ushort2.md)
  A vector of two 16-bit unsigned integer elements.
- [typealias simd_ushort3](./simd_ushort3.md)
  A vector of three 16-bit unsigned integer elements.
- [typealias simd_ushort8](./simd_ushort8.md)
  A vector of eight 16-bit unsigned integer elements.
- [typealias simd_ushort16](./simd_ushort16.md)
  A vector of sixteen 16-bit unsigned integer elements.
- [typealias simd_ushort32](./simd_ushort32.md)
  A vector of thirty-two 16-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ushort4)*