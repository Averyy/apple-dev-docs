# simd_ushort2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 16-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ushort2 = SIMD2<UInt16>
```

```c
typedef unsigned short __attribute__((ext_vector_type(2))) simd_ushort2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_ushort2(simd_ushort2) -> simd_ushort2](./simd_make_ushort2%28_%29-2dkjj.md)
  Returns a new vector from the specified vector.
- [func simd_make_ushort2(simd_ushort3) -> simd_ushort2](./simd_make_ushort2%28_%29-2gsja.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_ushort2(simd_ushort4) -> simd_ushort2](./simd_make_ushort2%28_%29-1sfxh.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_ushort2(simd_ushort8) -> simd_ushort2](./simd_make_ushort2%28_%29-2yrlt.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_ushort2(simd_ushort16) -> simd_ushort2](./simd_make_ushort2%28_%29-72vh1.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_ushort2(simd_ushort32) -> simd_ushort2](./simd_make_ushort2%28_%29-8zwg1.md)
  Returns a new vector by truncating the specified thirty two-element vector.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_ushort2(UInt16) -> simd_ushort2](./simd_make_ushort2%28_%29-4i2ym.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ushort2(UInt16, UInt16) -> simd_ushort2](./simd_make_ushort2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_ushort2_undef(UInt16) -> simd_ushort2](./simd_make_ushort2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector2](./vector2-39jw3.md)
  Returns a new vector from the specified scalar values.
### Common Functions
- [func simd_clamp(simd_ushort2, simd_ushort2, simd_ushort2) -> simd_ushort2](./simd_clamp%28_,_,_%29-3o9ad.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ushort2, simd_ushort2) -> simd_bool](./simd_equal%28_,_%29-ktbu.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ushort2) -> UInt16](./simd_reduce_min%28_%29-49m28.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ushort2) -> UInt16](./simd_reduce_max%28_%29-4kcqg.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ushort2) -> UInt16](./simd_reduce_add%28_%29-2pw16.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_ushort2, simd_ushort2) -> simd_ushort2](./simd_min%28_,_%29-717c8.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ushort2, simd_ushort2) -> simd_ushort2](./simd_max%28_,_%29-27z7q.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ushort2) -> simd_bool](./simd_any%28_%29-649i9.md)
- [func simd_all(simd_ushort2) -> simd_bool](./simd_all%28_%29-1dffj.md)
- [func simd_bitselect(simd_ushort2, simd_ushort2, simd_short2) -> simd_ushort2](./simd_bitselect%28_,_,_%29-9p6cd.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ushort2](./vector_ushort2.md)
### Functions to Create Two-Element Vectors From Vectors of Other Types
- [simd_ushort](./simd_ushort-3j95f.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ushort](./simd_ushort-3jj4j.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-3j49f.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ushort](./simd_ushort-3je8j.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-3jb1r.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ushort](./simd_ushort-3jl2n.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-3ja7h.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ushort](./simd_ushort-3jk19.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ushort](./simd_ushort-3ji9x.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ushort](./simd_ushort-3jhkd.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_ushort_sat](./simd_ushort_sat-7h07e.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7ha6i.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7h54a.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7hf1m.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7h23i.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7hc2m.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7h2xq.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7hcwu.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ushort_sat](./simd_ushort_sat-7hb0i.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ushort_sat](./simd_ushort_sat-7haim.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_ushort1](./simd_ushort1.md)
  A vector of one 16-bit unsigned integer element.
- [typealias simd_ushort3](./simd_ushort3.md)
  A vector of three 16-bit unsigned integer elements.
- [typealias simd_ushort4](./simd_ushort4.md)
  A vector of four 16-bit unsigned integer elements.
- [typealias simd_ushort8](./simd_ushort8.md)
  A vector of eight 16-bit unsigned integer elements.
- [typealias simd_ushort16](./simd_ushort16.md)
  A vector of sixteen 16-bit unsigned integer elements.
- [typealias simd_ushort32](./simd_ushort32.md)
  A vector of thirty-two 16-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ushort2)*