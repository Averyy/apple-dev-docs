# simd_long8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 64-bit signed integer elements.

## Declaration

```swift
typealias simd_long8 = SIMD8<simd_long1>
```

```c
typedef long __attribute__((ext_vector_type(8))) simd_long8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_long8(simd_long2) -> simd_long8](./simd_make_long8%28_%29-7pzt7.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_long8(simd_long3) -> simd_long8](./simd_make_long8%28_%29-7netg.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_long8(simd_long4) -> simd_long8](./simd_make_long8%28_%29-7wvxt.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_long8(simd_long8) -> simd_long8](./simd_make_long8%28_%29-6saal.md)
  Returns a new vector from the specified vector.
- [func simd_make_long8(simd_long4, simd_long4) -> simd_long8](./simd_make_long8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_long8_undef(simd_long2) -> simd_long8](./simd_make_long8_undef%28_%29-5uowh.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_long8_undef(simd_long3) -> simd_long8](./simd_make_long8_undef%28_%29-5y3qm.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_long8_undef(simd_long4) -> simd_long8](./simd_make_long8_undef%28_%29-59t0j.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [vector8](./vector8-6qxy0.md)
  Returns a new vector from the specified vectors.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_long8(simd_long1) -> simd_long8](./simd_make_long8%28_%29-2kqft.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_long8_undef(simd_long1) -> simd_long8](./simd_make_long8_undef%28_%29-9h1v1.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_long8) -> simd_long8](./simd_abs%28_%29-7osxw.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_long8, simd_long8, simd_long8) -> simd_long8](./simd_clamp%28_,_,_%29-7h5og.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_long8, simd_long8) -> simd_bool](./simd_equal%28_,_%29-1fygf.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_long8) -> simd_long1](./simd_reduce_min%28_%29-3okve.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_long8) -> simd_long1](./simd_reduce_max%28_%29-55m7m.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_long8) -> simd_long1](./simd_reduce_add%28_%29-3b63s.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_long8, simd_long8) -> simd_long8](./simd_min%28_,_%29-1z34d.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_long8, simd_long8) -> simd_long8](./simd_max%28_,_%29-4cbvp.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_long8) -> simd_bool](./simd_any%28_%29-6pjhd.md)
- [func simd_all(simd_long8) -> simd_bool](./simd_all%28_%29-1yys7.md)
- [func simd_bitselect(simd_long8, simd_long8, simd_long8) -> simd_long8](./simd_bitselect%28_,_,_%29-5k6g.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_long8](./vector_long8.md)
### Conversion to Signed 64-Bit (Round Half to Even) Functions
- [simd_long_rte](./simd_long_rte-90anl.md)
  Returns a new eight-element vector by rounding halves to the nearest even value.
### Functions to Create Eight-Element Vectors From Vectors of Other Types
- [simd_long](./simd_long-93qrw.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_long](./simd_long-93gss.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_long](./simd_long-93vu4.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_long](./simd_long-93lpo.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_long](./simd_long-93sno.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_long](./simd_long-93iok.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_long](./simd_long-93ti0.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_long](./simd_long-93jiw.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_long](./simd_long-93hmw.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_long](./simd_long-93h2w.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_long_sat](./simd_long_sat-6s8z2.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-6rz5a.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-6sdu6.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-6s426.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-6s5qq.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-6rvv6.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-6s53e.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-6rux6.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-6ry46.md)
  Returns a new vector from the specified vector of 32-bit, floating point elements.
- [simd_long_sat](./simd_long_sat-6rxje.md)
  Returns a new vector from the specified vector of 64-bit, floating point elements.

## See Also

### Vector Data Types
- [typealias simd_long1](./simd_long1.md)
  A vector of one 64-bit signed integer element.
- [typealias simd_long2](./simd_long2.md)
  A vector of two 64-bit signed integer elements.
- [typealias simd_long3](./simd_long3.md)
  A vector of three 64-bit signed integer elements.
- [typealias simd_long4](./simd_long4.md)
  A vector of four 64-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_long8)*