# simd_ushort8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 16-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ushort8 = SIMD8<UInt16>
```

```c
typedef unsigned short __attribute__((ext_vector_type(8))) simd_ushort8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_ushort8(simd_ushort2) -> simd_ushort8](./simd_make_ushort8%28_%29-1e906.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_ushort8(simd_ushort3) -> simd_ushort8](./simd_make_ushort8%28_%29-1henz.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_ushort8(simd_ushort4) -> simd_ushort8](./simd_make_ushort8%28_%29-17t38.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_ushort8(simd_ushort8) -> simd_ushort8](./simd_make_ushort8%28_%29-2e4yw.md)
  Returns a new vector from the specified vector.
- [func simd_make_ushort8(simd_ushort16) -> simd_ushort8](./simd_make_ushort8%28_%29-5yzvk.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_ushort8(simd_ushort32) -> simd_ushort8](./simd_make_ushort8%28_%29-4t9gk.md)
  Returns a new vector by truncating the specified thrity two-element vector.
- [func simd_make_ushort8(simd_ushort4, simd_ushort4) -> simd_ushort8](./simd_make_ushort8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_ushort8_undef(simd_ushort2) -> simd_ushort8](./simd_make_ushort8_undef%28_%29-49rg0.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_ushort8_undef(simd_ushort3) -> simd_ushort8](./simd_make_ushort8_undef%28_%29-46lw9.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_ushort8_undef(simd_ushort4) -> simd_ushort8](./simd_make_ushort8_undef%28_%29-416aa.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [vector8](./vector8-411sw.md)
  Returns a new vector from the specified vectors.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_ushort8(UInt16) -> simd_ushort8](./simd_make_ushort8%28_%29-66ltd.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ushort8_undef(UInt16) -> simd_ushort8](./simd_make_ushort8_undef%28_%29-wluw.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_ushort8, simd_ushort8, simd_ushort8) -> simd_ushort8](./simd_clamp%28_,_,_%29-81cik.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ushort8, simd_ushort8) -> simd_bool](./simd_equal%28_,_%29-3fkex.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ushort8) -> UInt16](./simd_reduce_min%28_%29-3oh9i.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ushort8) -> UInt16](./simd_reduce_max%28_%29-55hce.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ushort8) -> UInt16](./simd_reduce_add%28_%29-3b3cs.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_ushort8, simd_ushort8) -> simd_ushort8](./simd_min%28_,_%29-2600d.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ushort8, simd_ushort8) -> simd_ushort8](./simd_max%28_,_%29-30jsw.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ushort8) -> simd_bool](./simd_any%28_%29-6pgp3.md)
- [func simd_all(simd_ushort8) -> simd_bool](./simd_all%28_%29-1yk7d.md)
- [func simd_bitselect(simd_ushort8, simd_ushort8, simd_short8) -> simd_ushort8](./simd_bitselect%28_,_,_%29-4yay5.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ushort8](./vector_ushort8.md)
### Functions to Create Eight-Element Vectors From Vectors of Other Types
- [simd_ushort](./simd_ushort-443vh.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ushort](./simd_ushort-44dr1.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-448v1.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ushort](./simd_ushort-44iu5.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-446z9.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ushort](./simd_ushort-44gyd.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-44617.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ushort](./simd_ushort-44fwr.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-44cwv.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ushort](./simd_ushort-44dgr.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_ushort_sat](./simd_ushort_sat-8fsa4.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-8fi24.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-8fn0s.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-8fd8s.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-8fq7o.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-8fgdw.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-8foko.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-8feug.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-8fgi0.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ushort_sat](./simd_ushort_sat-8fh48.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_ushort1](./simd_ushort1.md)
  A vector of one 16-bit unsigned integer element.
- [typealias simd_ushort2](./simd_ushort2.md)
  A vector of two 16-bit unsigned integer elements.
- [typealias simd_ushort3](./simd_ushort3.md)
  A vector of three 16-bit unsigned integer elements.
- [typealias simd_ushort4](./simd_ushort4.md)
  A vector of four 16-bit unsigned integer elements.
- [typealias simd_ushort16](./simd_ushort16.md)
  A vector of sixteen 16-bit unsigned integer elements.
- [typealias simd_ushort32](./simd_ushort32.md)
  A vector of thirty-two 16-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ushort8)*