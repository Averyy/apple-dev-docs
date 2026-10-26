# simd_long3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 64-bit signed integer elements.

## Declaration

```swift
typealias simd_long3 = SIMD3<simd_long1>
```

```c
typedef long __attribute__((ext_vector_type(3))) simd_long3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_long3(simd_long2) -> simd_long3](./simd_make_long3%28_%29-4le1z.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_long3(simd_long3) -> simd_long3](./simd_make_long3%28_%29-4osz8.md)
  Returns a new vector from the specified vector.
- [func simd_make_long3(simd_long4) -> simd_long3](./simd_make_long3%28_%29-40i9p.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_long3(simd_long8) -> simd_long3](./simd_make_long3%28_%29-567hd.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_long3_undef(simd_long2) -> simd_long3](./simd_make_long3_undef%28_%29-8anf9.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_long3(simd_long1) -> simd_long3](./simd_make_long3%28_%29-1n0vi.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_long3(simd_long1, simd_long1, simd_long1) -> simd_long3](./simd_make_long3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_long3_undef(simd_long1) -> simd_long3](./simd_make_long3_undef%28_%29-4ehx.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector3](./vector3-3pmc2.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_long3(simd_long1, simd_long2) -> simd_long3](./simd_make_long3%28_,_%29-3zz23.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_long3(simd_long2, simd_long1) -> simd_long3](./simd_make_long3%28_,_%29-36pz0.md)
  Returns a new vector from a vector and a scalar value.
- [vector3](./vector3-6gwfj.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_long3) -> simd_long3](./simd_abs%28_%29-8d3rx.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_long3, simd_long3, simd_long3) -> simd_long3](./simd_clamp%28_,_,_%29-6yqku.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_long3, simd_long3) -> simd_bool](./simd_equal%28_,_%29-1ikxk.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_long3) -> simd_long1](./simd_reduce_min%28_%29-45zbv.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_long3) -> simd_long1](./simd_reduce_max%28_%29-4hb9r.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_long3) -> simd_long1](./simd_reduce_add%28_%29-2uv9x.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_long3, simd_long3) -> simd_long3](./simd_min%28_,_%29-3a034.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_long3, simd_long3) -> simd_long3](./simd_max%28_,_%29-2hury.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_long3) -> simd_bool](./simd_any%28_%29-698ng.md)
- [func simd_all(simd_long3) -> simd_bool](./simd_all%28_%29-1ao6q.md)
- [func simd_bitselect(simd_long3, simd_long3, simd_long3) -> simd_long3](./simd_bitselect%28_,_,_%29-9hl4.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_long3](./vector_long3.md)
### Conversion to Signed 64-Bit (Round Half to Even) Functions
- [simd_long_rte](./simd_long_rte-83sbc.md)
  Returns a new three-element vector by rounding halves to the nearest even value.
### Functions to Create Three-Element Vectors From Vectors of Other Types
- [simd_long](./simd_long-7iv6.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_long](./simd_long-7936.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_long](./simd_long-7dya.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_long](./simd_long-740y.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_long](./simd_long-7kye.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_long](./simd_long-7aza.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_long](./simd_long-7miu.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_long](./simd_long-7ccm.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_long](./simd_long-7aju.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_long](./simd_long-79xy.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_long_sat](./simd_long_sat-5ov8p.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-5p5gp.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-5oqa1.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-5p05l.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-5oscx.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-5p28h.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-5oqsr.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_long_sat](./simd_long_sat-5p0mj.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_long_sat](./simd_long_sat-5p3tb.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_long_sat](./simd_long_sat-5p3aj.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_long1](./simd_long1.md)
  A vector of one 64-bit signed integer element.
- [typealias simd_long2](./simd_long2.md)
  A vector of two 64-bit signed integer elements.
- [typealias simd_long4](./simd_long4.md)
  A vector of four 64-bit signed integer elements.
- [typealias simd_long8](./simd_long8.md)
  A vector of eight 64-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_long3)*