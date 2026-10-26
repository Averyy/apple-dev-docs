# simd_uchar4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 8-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uchar4 = SIMD4<UInt8>
```

```c
typedef unsigned char __attribute__((ext_vector_type(4))) simd_uchar4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_uchar4(simd_uchar2) -> simd_uchar4](./simd_make_uchar4%28_%29-4hwy4.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uchar4(simd_uchar3) -> simd_uchar4](./simd_make_uchar4%28_%29-4lf1x.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_uchar4(simd_uchar4) -> simd_uchar4](./simd_make_uchar4%28_%29-3x2fa.md)
  Returns a new vector from the specified vector.
- [func simd_make_uchar4(simd_uchar8) -> simd_uchar4](./simd_make_uchar4%28_%29-3i1f6.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_uchar4(simd_uchar16) -> simd_uchar4](./simd_make_uchar4%28_%29-174yg.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_uchar4(simd_uchar32) -> simd_uchar4](./simd_make_uchar4%28_%29-6662s.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_uchar4(simd_uchar64) -> simd_uchar4](./simd_make_uchar4%28_%29-4d9x4.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_uchar4(simd_uchar2, simd_uchar2) -> simd_uchar4](./simd_make_uchar4%28_,_%29-29ka1.md)
  Returns a new vector from the specified vectors.
- [func simd_make_uchar4_undef(simd_uchar2) -> simd_uchar4](./simd_make_uchar4_undef%28_%29-5we7j.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_uchar4_undef(simd_uchar3) -> simd_uchar4](./simd_make_uchar4_undef%28_%29-5tfyu.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [vector4](./vector4-3tea7.md)
  Returns a new vector from the specified vectors.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_uchar4(UInt8) -> simd_uchar4](./simd_make_uchar4%28_%29-7gszj.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uchar4(UInt8, UInt8, UInt8, UInt8) -> simd_uchar4](./simd_make_uchar4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_uchar4_undef(UInt8) -> simd_uchar4](./simd_make_uchar4_undef%28_%29-7uno.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector4](./vector4-7c8o4.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_uchar4(simd_uchar2, UInt8, UInt8) -> simd_uchar4](./simd_make_uchar4%28_,_,_%29-5x9io.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_uchar4(simd_uchar3, UInt8) -> simd_uchar4](./simd_make_uchar4%28_,_%29-3zlj2.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_uchar4(UInt8, UInt8, simd_uchar2) -> simd_uchar4](./simd_make_uchar4%28_,_,_%29-9rqjk.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_uchar4(UInt8, simd_uchar2, UInt8) -> simd_uchar4](./simd_make_uchar4%28_,_,_%29-53d7w.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_uchar4(UInt8, simd_uchar3) -> simd_uchar4](./simd_make_uchar4%28_,_%29-4sdi7.md)
  Returns a new vector from a scalar value and a vector.
- [vector4](./vector4-8y2oj.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_clamp(simd_uchar4, simd_uchar4, simd_uchar4) -> simd_uchar4](./simd_clamp%28_,_,_%29-7gs2x.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uchar4, simd_uchar4) -> simd_bool](./simd_equal%28_,_%29-4wf8b.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uchar4) -> UInt8](./simd_reduce_min%28_%29-4uo6i.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_uchar4) -> UInt8](./simd_reduce_max%28_%29-4qv6y.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uchar4) -> UInt8](./simd_reduce_add%28_%29-2yos8.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uchar4, simd_uchar4) -> simd_uchar4](./simd_min%28_,_%29-9muwy.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uchar4, simd_uchar4) -> simd_uchar4](./simd_max%28_,_%29-2f249.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uchar4) -> simd_bool](./simd_any%28_%29-6d22b.md)
- [func simd_all(simd_uchar4) -> simd_bool](./simd_all%28_%29-1jo4t.md)
- [func simd_bitselect(simd_uchar4, simd_uchar4, simd_char4) -> simd_uchar4](./simd_bitselect%28_,_,_%29-46k0t.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_uchar4](./vector_uchar4.md)
### Functions to Create Four-Element Vectors From Vectors of Other Types
- [simd_uchar](./simd_uchar-8g94o.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_uchar](./simd_uchar-8fzaw.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_uchar](./simd_uchar-8geew.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_uchar](./simd_uchar-8g46w.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_uchar](./simd_uchar-8g7eg.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_uchar](./simd_uchar-8fxko.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_uchar](./simd_uchar-8g90k.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_uchar](./simd_uchar-8fz6s.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_uchar](./simd_uchar-8g0ws.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_uchar](./simd_uchar-8g1h0.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_uchar_sat](./simd_uchar_sat-2dfgm.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_uchar_sat](./simd_uchar_sat-2d5ae.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_uchar_sat](./simd_uchar_sat-2dkfa.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_uchar_sat](./simd_uchar_sat-2daau.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_uchar_sat](./simd_uchar_sat-2ddea.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_uchar_sat](./simd_uchar_sat-2d3ma.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_uchar_sat](./simd_uchar_sat-2deje.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_uchar_sat](./simd_uchar_sat-2d4d6.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_uchar_sat](./simd_uchar_sat-2d6fq.md)
  Returns a new vector from the specified vector of 32-bit, floating point elements.
- [simd_uchar_sat](./simd_uchar_sat-2d6wq.md)
  Returns a new vector from the specified vector of 64-bit, floating point elements.

## See Also

### Vector Data Types
- [typealias simd_uchar1](./simd_uchar1.md)
  A vector of one 8-bit unsigned integer element.
- [typealias simd_uchar2](./simd_uchar2.md)
  A vector of two 8-bit unsigned integer elements.
- [typealias simd_uchar3](./simd_uchar3.md)
  A vector of three 8-bit unsigned integer elements.
- [typealias simd_uchar8](./simd_uchar8.md)
  A vector of eight 8-bit unsigned integer elements.
- [typealias simd_uchar16](./simd_uchar16.md)
  A vector of sixteen 8-bit unsigned integer elements.
- [typealias simd_uchar32](./simd_uchar32.md)
  A vector of thirty-two 8-bit unsigned integer elements.
- [typealias simd_uchar64](./simd_uchar64.md)
  A vector of sixty-four 8-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uchar4)*