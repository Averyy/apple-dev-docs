# simd_char8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 8-bit signed integer elements.

## Declaration

```swift
typealias simd_char8 = SIMD8<CChar>
```

```c
typedef char __attribute__((ext_vector_type(8))) simd_char8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_char8(simd_char2) -> simd_char8](./simd_make_char8%28_%29-3e9h4.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_char8(simd_char3) -> simd_char8](./simd_make_char8%28_%29-39q4x.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_char8(simd_char4) -> simd_char8](./simd_make_char8%28_%29-3y2oy.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_char8(simd_char8) -> simd_char8](./simd_make_char8%28_%29-4c00u.md)
  Returns a new vector from the specified vector.
- [func simd_make_char8(simd_char16) -> simd_char8](./simd_make_char8%28_%29-497r7.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_char8(simd_char32) -> simd_char8](./simd_make_char8%28_%29-tbln.md)
  Returns a new vector by truncating the specified thrity two-element vector.
- [func simd_make_char8(simd_char64) -> simd_char8](./simd_make_char8%28_%29-4m1k5.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_char8(simd_char4, simd_char4) -> simd_char8](./simd_make_char8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_char8_undef(simd_char2) -> simd_char8](./simd_make_char8_undef%28_%29-4zw8k.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_char8_undef(simd_char3) -> simd_char8](./simd_make_char8_undef%28_%29-53bml.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_char8_undef(simd_char4) -> simd_char8](./simd_make_char8_undef%28_%29-5kqwe.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [vector8](./vector8-73z2d.md)
  Returns a new vector from the specified vectors.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_char8(CChar) -> simd_char8](./simd_make_char8%28_%29-2wraz.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char8_undef(CChar) -> simd_char8](./simd_make_char8_undef%28_%29-830qy.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_char8) -> simd_char8](./simd_abs%28_%29-7oowg.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_char8, simd_char8, simd_char8) -> simd_char8](./simd_clamp%28_,_,_%29-6t9ze.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_char8, simd_char8) -> simd_bool](./simd_equal%28_,_%29-7xed4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_char8) -> CChar](./simd_reduce_min%28_%29-3omfa.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_char8) -> CChar](./simd_reduce_max%28_%29-55mb2.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_char8) -> CChar](./simd_reduce_add%28_%29-3b8ak.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_char8, simd_char8) -> simd_char8](./simd_min%28_,_%29-66w6r.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_char8, simd_char8) -> simd_char8](./simd_max%28_,_%29-1zyht.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_char8) -> simd_bool](./simd_any%28_%29-6plnr.md)
- [func simd_all(simd_char8) -> simd_bool](./simd_all%28_%29-1yyw9.md)
- [func simd_bitselect(simd_char8, simd_char8, simd_char8) -> simd_char8](./simd_bitselect%28_,_,_%29-5bgc3.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_char8](./vector_char8.md)
### Functions to Create Eight-Element Vectors From Vectors of Other Types
- [simd_char](./simd_char-7azp6.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_char](./simd_char-7apve.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_char](./simd_char-7b4ze.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_char](./simd_char-7aure.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_char](./simd_char-7b2w6.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_char](./simd_char-7at2e.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_char](./simd_char-7b3y6.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_char](./simd_char-7au4e.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_char](./simd_char-7aqw2.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_char](./simd_char-7arha.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_char_sat](./simd_char_sat-1k3vb.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-1kdqv.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-1jyvr.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-1k8uv.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-1k1zv.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-1kbyz.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-1k125.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-1kb19.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-1kcv9.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_char_sat](./simd_char_sat-1kdj1.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

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
- [typealias simd_char16](./simd_char16.md)
  A vector of sixteen 8-bit signed integer elements.
- [typealias simd_char32](./simd_char32.md)
  A vector of thirty-two 8-bit signed integer elements.
- [typealias simd_char64](./simd_char64.md)
  A vector of sixty-four 8-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_char8)*