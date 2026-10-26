# simd_uint16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixteen 32-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uint16 = SIMD16<UInt32>
```

```c
typedef unsigned int __attribute__((ext_vector_type(16))) simd_uint16;
```

## Topics

### Functions to Create Sixteen-Element Vectors From Other Vectors
- [func simd_make_uint16(simd_uint2) -> simd_uint16](./simd_make_uint16%28_%29-99aov.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uint16(simd_uint3) -> simd_uint16](./simd_make_uint16%28_%29-9efau.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_uint16(simd_uint4) -> simd_uint16](./simd_make_uint16%28_%29-9u6t5.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_uint16(simd_uint8) -> simd_uint16](./simd_make_uint16%28_%29-9hiq.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_uint16(simd_uint16) -> simd_uint16](./simd_make_uint16%28_%29-9s9mg.md)
  Returns a new vector from the specified vector.
- [func simd_make_uint16(simd_uint8, simd_uint8) -> simd_uint16](./simd_make_uint16%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_uint16_undef(simd_uint2) -> simd_uint16](./simd_make_uint16_undef%28_%29-9w2go.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_uint16_undef(simd_uint3) -> simd_uint16](./simd_make_uint16_undef%28_%29-9slqx.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_uint16_undef(simd_uint4) -> simd_uint16](./simd_make_uint16_undef%28_%29-hcyl.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_uint16_undef(simd_uint8) -> simd_uint16](./simd_make_uint16_undef%28_%29-we1l.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
- [vector16](./vector16-8xs3z.md)
  Returns a new vector from the specified vectors.
### Functions to Create Sixteen-Element Vectors From Scalar Values
- [func simd_make_uint16(UInt32) -> simd_uint16](./simd_make_uint16%28_%29-3h7ip.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uint16_undef(UInt32) -> simd_uint16](./simd_make_uint16_undef%28_%29-6ss74.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_uint16, simd_uint16, simd_uint16) -> simd_uint16](./simd_clamp%28_,_,_%29-226tg.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uint16, simd_uint16) -> simd_bool](./simd_equal%28_,_%29-35l8d.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uint16) -> UInt32](./simd_reduce_min%28_%29-3cy7f.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_uint16) -> UInt32](./simd_reduce_max%28_%29-8iqq5.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uint16) -> UInt32](./simd_reduce_add%28_%29-7n22w.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uint16, simd_uint16) -> simd_uint16](./simd_min%28_,_%29-5plhb.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uint16, simd_uint16) -> simd_uint16](./simd_max%28_,_%29-3cz8t.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uint16) -> simd_bool](./simd_any%28_%29-931x2.md)
- [func simd_all(simd_uint16) -> simd_bool](./simd_all%28_%29-inj8.md)
- [func simd_bitselect(simd_uint16, simd_uint16, simd_int16) -> simd_uint16](./simd_bitselect%28_,_,_%29-35yra.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_uint16](./vector_uint16.md)
### Functions to Create Sixteen-Element Vectors From Vectors of Other Types
- [simd_uint](./simd_uint-19fie.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_uint](./simd_uint-19pae.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_uint](./simd_uint-19aau.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_uint](./simd_uint-19kfa.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_uint](./simd_uint-19cb6.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_uint](./simd_uint-19m36.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_uint](./simd_uint-19qym.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_uint_sat](./simd_uint_sat-548q7.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_uint_sat](./simd_uint_sat-53yzz.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_uint_sat](./simd_uint_sat-543rj.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_uint_sat](./simd_uint_sat-53tzj.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_uint_sat](./simd_uint_sat-5471v.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_uint_sat](./simd_uint_sat-53wxf.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_uint_sat](./simd_uint_sat-53x8t.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_uint1](./simd_uint1.md)
  A vector of one 32-bit unsigned integer element.
- [typealias simd_uint2](./simd_uint2.md)
  A vector of two 32-bit unsigned integer elements.
- [typealias simd_uint3](./simd_uint3.md)
  A vector of three 32-bit unsigned integer elements.
- [typealias simd_uint4](./simd_uint4.md)
  A vector of four 32-bit unsigned integer elements.
- [typealias simd_uint8](./simd_uint8.md)
  A vector of eight 32-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uint16)*