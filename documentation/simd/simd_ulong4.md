# simd_ulong4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 64-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ulong4 = SIMD4<simd_ulong1>
```

```c
typedef unsigned long __attribute__((ext_vector_type(4))) simd_ulong4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_ulong4(simd_ulong2) -> simd_ulong4](./simd_make_ulong4%28_%29-364ux.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_ulong4(simd_ulong3) -> simd_ulong4](./simd_make_ulong4%28_%29-39may.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_ulong4(simd_ulong4) -> simd_ulong4](./simd_make_ulong4%28_%29-2zv2b.md)
  Returns a new vector from the specified vector.
- [func simd_make_ulong4(simd_ulong8) -> simd_ulong4](./simd_make_ulong4%28_%29-43wof.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_ulong4(simd_ulong2, simd_ulong2) -> simd_ulong4](./simd_make_ulong4%28_,_%29-9oy4u.md)
  Returns a new vector from the specified vectors.
- [func simd_make_ulong4_undef(simd_ulong2) -> simd_ulong4](./simd_make_ulong4_undef%28_%29-o0j.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_ulong4_undef(simd_ulong3) -> simd_ulong4](./simd_make_ulong4_undef%28_%29-9xbtd.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_ulong4(simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_%29-6kawu.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ulong4(simd_ulong1, simd_ulong1, simd_ulong1, simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_ulong4_undef(simd_ulong1) -> simd_ulong4](./simd_make_ulong4_undef%28_%29-jgtr.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_ulong4(simd_ulong1, simd_ulong1, simd_ulong2) -> simd_ulong4](./simd_make_ulong4%28_,_,_%29-4du2m.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_ulong4(simd_ulong1, simd_ulong2, simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_,_,_%29-8asm5.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_ulong4(simd_ulong1, simd_ulong3) -> simd_ulong4](./simd_make_ulong4%28_,_%29-5mtth.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_ulong4(simd_ulong2, simd_ulong1, simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_,_,_%29-8g4ch.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_ulong4(simd_ulong3, simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_,_%29-cnt3.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_clamp(simd_ulong4, simd_ulong4, simd_ulong4) -> simd_ulong4](./simd_clamp%28_,_,_%29-5cuj3.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ulong4, simd_ulong4) -> simd_bool](./simd_equal%28_,_%29-8d8x.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ulong4) -> simd_ulong1](./simd_reduce_min%28_%29-4ujwm.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ulong4) -> simd_ulong1](./simd_reduce_max%28_%29-4qsf2.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ulong4) -> simd_ulong1](./simd_reduce_add%28_%29-2yjx0.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_ulong4, simd_ulong4) -> simd_ulong4](./simd_min%28_,_%29-9meuw.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ulong4, simd_ulong4) -> simd_ulong4](./simd_max%28_,_%29-6x9fu.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ulong4) -> simd_bool](./simd_any%28_%29-6cxel.md)
- [func simd_all(simd_ulong4) -> simd_bool](./simd_all%28_%29-1jlbv.md)
- [func simd_bitselect(simd_ulong4, simd_ulong4, simd_long4) -> simd_ulong4](./simd_bitselect%28_,_,_%29-6gszc.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ulong4](./vector_ulong4.md)

## See Also

### Vector Data Types
- [typealias simd_ulong1](./simd_ulong1.md)
  A vector of one 64-bit unsigned integer element.
- [typealias simd_ulong2](./simd_ulong2.md)
  A vector of two 64-bit unsigned integer elements.
- [typealias simd_ulong3](./simd_ulong3.md)
  A vector of three 64-bit unsigned integer elements.
- [typealias simd_ulong8](./simd_ulong8.md)
  A vector of eight 64-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ulong4)*