# simd_char3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 8-bit signed integer elements.

## Declaration

```swift
typealias simd_char3 = SIMD3<CChar>
```

```c
typedef char __attribute__((ext_vector_type(3))) simd_char3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_char3(simd_char2) -> simd_char3](./simd_make_char3%28_%29-7hn14.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_char3(simd_char3) -> simd_char3](./simd_make_char3%28_%29-7l2ch.md)
  Returns a new vector from the specified vector.
- [func simd_make_char3(simd_char4) -> simd_char3](./simd_make_char3%28_%29-81dqq.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_char3(simd_char8) -> simd_char3](./simd_make_char3%28_%29-6wpri.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_char3(simd_char16) -> simd_char3](./simd_make_char3%28_%29-7kwml.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_char3(simd_char32) -> simd_char3](./simd_make_char3%28_%29-5pt8h.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_char3(simd_char64) -> simd_char3](./simd_make_char3%28_%29-2kabv.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_char3_undef(simd_char2) -> simd_char3](./simd_make_char3_undef%28_%29-3pbpb.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_char3(CChar) -> simd_char3](./simd_make_char3%28_%29-9zbpd.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char3(CChar, CChar, CChar) -> simd_char3](./simd_make_char3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_char3_undef(CChar) -> simd_char3](./simd_make_char3_undef%28_%29-866v6.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector3](./vector3-7jt7g.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_char3(CChar, simd_char2) -> simd_char3](./simd_make_char3%28_,_%29-5c5ds.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_char3(simd_char2, CChar) -> simd_char3](./simd_make_char3%28_,_%29-9qv2s.md)
  Returns a new vector from a vector and a scalar value.
- [vector3](./vector3-7dpc0.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_char3) -> simd_char3](./simd_abs%28_%29-8d1l3.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_char3, simd_char3, simd_char3) -> simd_char3](./simd_clamp%28_,_,_%29-5xm9q.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_char3, simd_char3) -> simd_bool](./simd_equal%28_,_%29-ymae.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_char3) -> CChar](./simd_reduce_min%28_%29-461hl.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_char3) -> CChar](./simd_reduce_max%28_%29-4h9pt.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_char3) -> CChar](./simd_reduce_add%28_%29-2uwqb.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_char3, simd_char3) -> simd_char3](./simd_min%28_,_%29-93d9y.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_char3, simd_char3) -> simd_char3](./simd_max%28_,_%29-5fzu7.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_char3) -> simd_bool](./simd_any%28_%29-69a7c.md)
- [func simd_all(simd_char3) -> simd_bool](./simd_all%28_%29-1aml2.md)
- [func simd_bitselect(simd_char3, simd_char3, simd_char3) -> simd_char3](./simd_bitselect%28_,_,_%29-4kbjh.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_char3](./vector_char3.md)
### Functions to Create Three-Element Vectors From Vectors of Other Types
- [simd_char](./simd_char-7zce5.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_char](./simd_char-7z2kd.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_char](./simd_char-7zhfh.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_char](./simd_char-7z7i5.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_char](./simd_char-7zflh.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_char](./simd_char-7z5rp.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_char](./simd_char-7zejv.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_char](./simd_char-7z4q3.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_char](./simd_char-7z1j3.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_char](./simd_char-7z22z.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_char_sat](./simd_char_sat-2gjzk.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-2gu40.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-2gp4g.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-2gz1s.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-2giaw.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-2gs88.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-2gjc4.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-2gt5w.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-2gv24.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_char_sat](./simd_char_sat-2gvmc.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_char1](./simd_char1.md)
  A vector of one 8-bit signed integer element.
- [typealias simd_char2](./simd_char2.md)
  A vector of two 8-bit signed integer elements.
- [typealias simd_char4](./simd_char4.md)
  A vector of four 8-bit signed integer elements.
- [typealias simd_char8](./simd_char8.md)
  A vector of eight 8-bit signed integer elements.
- [typealias simd_char16](./simd_char16.md)
  A vector of sixteen 8-bit signed integer elements.
- [typealias simd_char32](./simd_char32.md)
  A vector of thirty-two 8-bit signed integer elements.
- [typealias simd_char64](./simd_char64.md)
  A vector of sixty-four 8-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_char3)*