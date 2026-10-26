# simd_char16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixteen 8-bit signed integer elements.

## Declaration

```swift
typealias simd_char16 = SIMD16<CChar>
```

```c
typedef char __attribute__((ext_vector_type(16))) simd_char16;
```

## Topics

### Functions to Create Sixteen-Element Vectors From Other Vectors
- [func simd_make_char16(simd_char2) -> simd_char16](./simd_make_char16%28_%29-5aqmo.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_char16(simd_char3) -> simd_char16](./simd_make_char16%28_%29-5e63t.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_char16(simd_char4) -> simd_char16](./simd_make_char16%28_%29-54urm.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_char16(simd_char8) -> simd_char16](./simd_make_char16%28_%29-4pte6.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_char16(simd_char16) -> simd_char16](./simd_make_char16%28_%29-516bc.md)
  Returns a new vector from the specified vector.
- [func simd_make_char16(simd_char32) -> simd_char16](./simd_make_char16%28_%29-tfq4.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_char16(simd_char64) -> simd_char16](./simd_make_char16%28_%29-2j94t.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_char16(simd_char8, simd_char8) -> simd_char16](./simd_make_char16%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_char16_undef(simd_char2) -> simd_char16](./simd_make_char16_undef%28_%29-5kb1b.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_char16_undef(simd_char3) -> simd_char16](./simd_make_char16_undef%28_%29-5gvk6.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_char16_undef(simd_char4) -> simd_char16](./simd_make_char16_undef%28_%29-5ddf1.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_char16_undef(simd_char8) -> simd_char16](./simd_make_char16_undef%28_%29-4yci9.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
- [vector16](./vector16-gwvj.md)
  Returns a new vector from the specified vectors.
### Functions to Create Sixteen-Element Vectors From Scalar Values
- [func simd_make_char16(CChar) -> simd_char16](./simd_make_char16%28_%29-9skzf.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char16_undef(CChar) -> simd_char16](./simd_make_char16_undef%28_%29-9uhre.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_char16) -> simd_char16](./simd_abs%28_%29-475ng.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_char16, simd_char16, simd_char16) -> simd_char16](./simd_clamp%28_,_,_%29-509lj.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_char16, simd_char16) -> simd_bool](./simd_equal%28_,_%29-19z1a.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_char16) -> CChar](./simd_reduce_min%28_%29-3crdj.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_char16) -> CChar](./simd_reduce_max%28_%29-8idj9.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_char16) -> CChar](./simd_reduce_add%28_%29-7mtzs.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_char16, simd_char16) -> simd_char16](./simd_min%28_,_%29-3t06b.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_char16, simd_char16) -> simd_char16](./simd_max%28_,_%29-2pboz.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_char16) -> simd_bool](./simd_any%28_%29-92tuy.md)
- [func simd_all(simd_char16) -> simd_bool](./simd_all%28_%29-iajg.md)
- [func simd_bitselect(simd_char16, simd_char16, simd_char16) -> simd_char16](./simd_bitselect%28_,_,_%29-5uq86.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_char16](./vector_char16.md)
### Functions to Create Sixteen-Element Vectors From Vectors of Other Types
- [simd_char](./simd_char-98lzg.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_char](./simd_char-98c7g.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_char](./simd_char-98qy4.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_char](./simd_char-98h4c.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_char](./simd_char-98nqs.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_char](./simd_char-98dx0.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_char](./simd_char-98dt4.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_char_sat](./simd_char_sat-6mtcs.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-6n38c.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-6mogs.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-6myfw.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-6mwk4.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-6n6j8.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-6n1q0.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_char1](./simd_char1.md)
  A vector of one 8-bit signed integer element.
- [typealias simd_char2](./simd_char2.md)
  A vector of two 8-bit signed integer elements.
- [typealias simd_char3](./simd_char3.md)
  A vector of three 8-bit signed integer elements.
- [typealias simd_char4](./simd_char4.md)
  A vector of four 8-bit signed integer elements.
- [typealias simd_char8](./simd_char8.md)
  A vector of eight 8-bit signed integer elements.
- [typealias simd_char32](./simd_char32.md)
  A vector of thirty-two 8-bit signed integer elements.
- [typealias simd_char64](./simd_char64.md)
  A vector of sixty-four 8-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_char16)*