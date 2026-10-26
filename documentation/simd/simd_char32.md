# simd_char32

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of thirty-two 8-bit signed integer elements.

## Declaration

```swift
typealias simd_char32 = SIMD32<CChar>
```

```c
typedef char __attribute__((ext_vector_type(32))) simd_char32;
```

## Topics

### Functions to Create Thirty Two-Element Vectors From Other Vectors
- [func simd_make_char32(simd_char2) -> simd_char32](./simd_make_char32%28_%29-384hl.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_char32(simd_char3) -> simd_char32](./simd_make_char32%28_%29-3bm80.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_char32(simd_char4) -> simd_char32](./simd_make_char32%28_%29-2n9wz.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_char32(simd_char8) -> simd_char32](./simd_make_char32%28_%29-2ag5j.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_char32(simd_char16) -> simd_char32](./simd_make_char32%28_%29-3g5k3.md)
  Returns a new vector from the specified sixteen-element vector, and other elements set to zero.
- [func simd_make_char32(simd_char32) -> simd_char32](./simd_make_char32%28_%29-8fqzf.md)
  Returns a new vector from the specified vector.
- [func simd_make_char32(simd_char64) -> simd_char32](./simd_make_char32%28_%29-6kn8l.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_char32(simd_char16, simd_char16) -> simd_char32](./simd_make_char32%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_char32_undef(simd_char2) -> simd_char32](./simd_make_char32_undef%28_%29-7t6qn.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_char32_undef(simd_char3) -> simd_char32](./simd_make_char32_undef%28_%29-7poo6.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_char32_undef(simd_char4) -> simd_char32](./simd_make_char32_undef%28_%29-7z0ct.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_char32_undef(simd_char8) -> simd_char32](./simd_make_char32_undef%28_%29-6t8l5.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
- [func simd_make_char32_undef(simd_char16) -> simd_char32](./simd_make_char32_undef%28_%29-3vq4m.md)
  Returns a new vector from the specified sixteen-element vector, and other elements undefined.
### Functions to Create Thirty Two-Element Vectors From Scalar Values
- [func simd_make_char32(CChar) -> simd_char32](./simd_make_char32%28_%29-20u7n.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char32_undef(CChar) -> simd_char32](./simd_make_char32_undef%28_%29-9nqa9.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_char32) -> simd_char32](./simd_abs%28_%29-2ca9r.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_char32, simd_char32, simd_char32) -> simd_char32](./simd_clamp%28_,_,_%29-2eiom.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_char32, simd_char32) -> simd_bool](./simd_equal%28_,_%29-2iweh.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_char32) -> CChar](./simd_reduce_min%28_%29-2au68.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_char32) -> CChar](./simd_reduce_max%28_%29-9j748.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_char32) -> CChar](./simd_reduce_add%28_%29-1uzk7.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_char32, simd_char32) -> simd_char32](./simd_min%28_,_%29-2isjs.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_char32, simd_char32) -> simd_char32](./simd_max%28_,_%29-9ec8n.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_char32) -> simd_bool](./simd_any%28_%29-3az4l.md)
- [func simd_all(simd_char32) -> simd_bool](./simd_all%28_%29-1k7jn.md)
- [func simd_bitselect(simd_char32, simd_char32, simd_char32) -> simd_char32](./simd_bitselect%28_,_,_%29-2da13.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_char32](./vector_char32.md)

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
- [typealias simd_char16](./simd_char16.md)
  A vector of sixteen 8-bit signed integer elements.
- [typealias simd_char64](./simd_char64.md)
  A vector of sixty-four 8-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_char32)*