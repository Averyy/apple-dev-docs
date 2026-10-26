# simd_char4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 8-bit signed integer elements.

## Declaration

```swift
typealias simd_char4 = SIMD4<CChar>
```

```c
typedef char __attribute__((ext_vector_type(4))) simd_char4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_char4(simd_char2) -> simd_char4](./simd_make_char4%28_%29-mdlt.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_char4(simd_char3) -> simd_char4](./simd_make_char4%28_%29-k1u0.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_char4(simd_char4) -> simd_char4](./simd_make_char4%28_%29-gjz7.md)
  Returns a new vector from the specified vector.
- [func simd_make_char4(simd_char8) -> simd_char4](./simd_make_char4%28_%29-1mbtb.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_char4(simd_char16) -> simd_char4](./simd_make_char4%28_%29-4y0kh.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_char4(simd_char32) -> simd_char4](./simd_make_char4%28_%29-3tnz9.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_char4(simd_char64) -> simd_char4](./simd_make_char4%28_%29-69u9q.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_char4(simd_char2, simd_char2) -> simd_char4](./simd_make_char4%28_,_%29-3vf4l.md)
  Returns a new vector from the specified vectors.
- [func simd_make_char4_undef(simd_char2) -> simd_char4](./simd_make_char4_undef%28_%29-6zlek.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_char4_undef(simd_char3) -> simd_char4](./simd_make_char4_undef%28_%29-73111.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [vector4](./vector4-695o8.md)
  Returns a new vector from the specified vectors.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_char4(CChar) -> simd_char4](./simd_make_char4%28_%29-8kfe3.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char4(CChar, CChar, CChar, CChar) -> simd_char4](./simd_make_char4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_char4_undef(CChar) -> simd_char4](./simd_make_char4_undef%28_%29-99pql.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector4](./vector4-2lql7.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Value
- [func simd_make_char4(simd_char2, CChar, CChar) -> simd_char4](./simd_make_char4%28_,_,_%29-82ftd.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_char4(simd_char3, CChar) -> simd_char4](./simd_make_char4%28_,_%29-226qq.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_char4(CChar, CChar, simd_char2) -> simd_char4](./simd_make_char4%28_,_,_%29-9mb46.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_char4(CChar, simd_char2, CChar) -> simd_char4](./simd_make_char4%28_,_,_%29-94kun.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_char4(CChar, simd_char3) -> simd_char4](./simd_make_char4%28_,_%29-76rpp.md)
  Returns a new vector from a scalar value and a vector.
- [vector4](./vector4-4dfou.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_char4) -> simd_char4](./simd_abs%28_%29-81ics.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_char4, simd_char4, simd_char4) -> simd_char4](./simd_clamp%28_,_,_%29-1lm34.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_char4, simd_char4) -> simd_bool](./simd_equal%28_,_%29-4x3vb.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_char4) -> CChar](./simd_reduce_min%28_%29-4ue96.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_char4) -> CChar](./simd_reduce_max%28_%29-4ql9m.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_char4) -> CChar](./simd_reduce_add%28_%29-2yeuw.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_char4, simd_char4) -> simd_char4](./simd_min%28_,_%29-2mbto.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_char4, simd_char4) -> simd_char4](./simd_max%28_,_%29-7qdak.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_char4) -> simd_bool](./simd_any%28_%29-6cs8j.md)
- [func simd_all(simd_char4) -> simd_bool](./simd_all%28_%29-1jxv1.md)
- [func simd_bitselect(simd_char4, simd_char4, simd_char4) -> simd_char4](./simd_bitselect%28_,_,_%29-4mvfw.md)
### Alternative Type Alias
- [typealias vector_char4](./vector_char4.md)
### Functions to Create Four-Element Vectors From Vectors of Other Types
- [simd_char](./simd_char-7q0xi.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_char](./simd_char-7pqwm.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_char](./simd_char-7q5x2.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_char](./simd_char-7pvsm.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_char](./simd_char-7pz0a.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_char](./simd_char-7pp6i.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_char](./simd_char-7pxci.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_char](./simd_char-7pnki.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_char](./simd_char-7pp9i.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_char](./simd_char-7pptu.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_char_sat](./simd_char_sat-1z4wz.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-1yuzn.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-1z9tv.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-1yzyb.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-1z32v.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-1yt3r.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-1z4mp.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_char_sat](./simd_char_sat-1yupd.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_char_sat](./simd_char_sat-1ywi1.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_char_sat](./simd_char_sat-1yx5t.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_char1](./simd_char1.md)
  A vector of one 8-bit signed integer element.
- [typealias simd_char2](./simd_char2.md)
  A vector of two 8-bit signed integer elements.
- [typealias simd_char3](./simd_char3.md)
  A vector of three 8-bit signed integer elements.
- [typealias simd_char8](./simd_char8.md)
  A vector of eight 8-bit signed integer elements.
- [typealias simd_char16](./simd_char16.md)
  A vector of sixteen 8-bit signed integer elements.
- [typealias simd_char32](./simd_char32.md)
  A vector of thirty-two 8-bit signed integer elements.
- [typealias simd_char64](./simd_char64.md)
  A vector of sixty-four 8-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_char4)*