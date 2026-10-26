# simd_long2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 64-bit signed integer elements.

## Declaration

```swift
typealias simd_long2 = SIMD2<simd_long1>
```

```c
typedef long __attribute__((ext_vector_type(2))) simd_long2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_long2(simd_long2) -> simd_long2](./simd_make_long2%28_%29-96bn.md)
  Returns a new vector from the specified vector.
- [func simd_make_long2(simd_long3) -> simd_long2](./simd_make_long2%28_%29-5ou8.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_long2(simd_long4) -> simd_long2](./simd_make_long2%28_%29-2abd.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_long2(simd_long8) -> simd_long2](./simd_make_long2%28_%29-9ozpw.md)
  Returns a new vector by truncating the specified eight-element vector.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_long2(simd_long1) -> simd_long2](./simd_make_long2%28_%29-698vu.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_long2(simd_long1, simd_long1) -> simd_long2](./simd_make_long2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_long2_undef(simd_long1) -> simd_long2](./simd_make_long2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector2](./vector2-8txip.md)
  Returns a new vector from the specified scalar values.
### Common Functions
- [func simd_abs(simd_long2) -> simd_long2](./simd_abs%28_%29-88ipu.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_long2, simd_long2, simd_long2) -> simd_long2](./simd_clamp%28_,_,_%29-4sik.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_long2, simd_long2) -> simd_bool](./simd_equal%28_,_%29-2qcs1.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_long2) -> simd_long1](./simd_reduce_min%28_%29-49gjw.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_long2) -> simd_long1](./simd_reduce_max%28_%29-4kq58.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_long2) -> simd_long1](./simd_reduce_add%28_%29-2qco6.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_long2, simd_long2) -> simd_long2](./simd_min%28_,_%29-5lq3f.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_long2, simd_long2) -> simd_long2](./simd_max%28_,_%29-439j5.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_long2) -> simd_bool](./simd_any%28_%29-64pz3.md)
- [func simd_all(simd_long2) -> simd_bool](./simd_all%28_%29-1cyyp.md)
- [func simd_bitselect(simd_long2, simd_long2, simd_long2) -> simd_long2](./simd_bitselect%28_,_,_%29-8ffoo.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_long2](./vector_long2.md)
### Conversion to Signed 64-Bit (Round Half to Even) Functions
- [simd_long_rte](./simd_long_rte-80b73.md)
  Returns a new two-element vector by rounding halves to the nearest even value.
### Functions to Create Two-Element Vectors From Vectors of Other Types
- [simd_long](./simd_long-410r.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_long](./simd_long-4ay3.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_long](./simd_long-3w3v.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_long](./simd_long-462z.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_long](./simd_long-3z5r.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_long](./simd_long-49a7.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_long](./simd_long-3xox.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_long](./simd_long-47o1.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_long](./simd_long-49c1.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_long](./simd_long-4a75.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_long_sat](./simd_long_sat-5sao0.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-5s0w0.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-5sfmo.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-5s5sw.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-5s900.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-5ryts.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-5s7z8.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-5ry5g.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-5rzv0.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_long_sat](./simd_long_sat-5s0fo.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_long1](./simd_long1.md)
  A vector of one 64-bit signed integer element.
- [typealias simd_long3](./simd_long3.md)
  A vector of three 64-bit signed integer elements.
- [typealias simd_long4](./simd_long4.md)
  A vector of four 64-bit signed integer elements.
- [typealias simd_long8](./simd_long8.md)
  A vector of eight 64-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_long2)*