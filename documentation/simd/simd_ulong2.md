# simd_ulong2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 64-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ulong2 = SIMD2<simd_ulong1>
```

```c
typedef unsigned long __attribute__((ext_vector_type(2))) simd_ulong2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_ulong2(simd_ulong2) -> simd_ulong2](./simd_make_ulong2%28_%29-oc6t.md)
  Returns a new vector from the specified vector.
- [func simd_make_ulong2(simd_ulong3) -> simd_ulong2](./simd_make_ulong2%28_%29-rr3e.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_ulong2(simd_ulong4) -> simd_ulong2](./simd_make_ulong2%28_%29-ulyf.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_ulong2(simd_ulong8) -> simd_ulong2](./simd_make_ulong2%28_%29-17hvf.md)
  Returns a new vector by truncating the specified eight-element vector.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_ulong2(simd_ulong1) -> simd_ulong2](./simd_make_ulong2%28_%29-14omj.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ulong2(simd_ulong1, simd_ulong1) -> simd_ulong2](./simd_make_ulong2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_ulong2_undef(simd_ulong1) -> simd_ulong2](./simd_make_ulong2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector2](./vector2-6n9bx.md)
  Returns a new vector from the specified scalar values.
### Common Functions
- [func simd_clamp(simd_ulong2, simd_ulong2, simd_ulong2) -> simd_ulong2](./simd_clamp%28_,_,_%29-5y5rd.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ulong2, simd_ulong2) -> simd_bool](./simd_equal%28_,_%29-80jzi.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ulong2) -> simd_ulong1](./simd_reduce_min%28_%29-49qq4.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ulong2) -> simd_ulong1](./simd_reduce_max%28_%29-4kgd8.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ulong2) -> simd_ulong1](./simd_reduce_add%28_%29-2q2jq.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_ulong2, simd_ulong2) -> simd_ulong2](./simd_min%28_,_%29-9be6.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ulong2, simd_ulong2) -> simd_ulong2](./simd_max%28_,_%29-86a4g.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ulong2) -> simd_bool](./simd_any%28_%29-64g1r.md)
- [func simd_all(simd_ulong2) -> simd_bool](./simd_all%28_%29-1d8u9.md)
- [func simd_bitselect(simd_ulong2, simd_ulong2, simd_long2) -> simd_ulong2](./simd_bitselect%28_,_,_%29-886h0.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ulong2](./vector_ulong2.md)
### Functions to Create Two-Element Vectors From Vectors of Other Types
- [simd_ulong](./simd_ulong-1r8xg.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ulong](./simd_ulong-1rir8.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ulong](./simd_ulong-1rdv8.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ulong](./simd_ulong-1rnp0.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ulong](./simd_ulong-1rbpo.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ulong](./simd_ulong-1rlsc.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ulong](./simd_ulong-1rb2o.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ulong](./simd_ulong-1rkuo.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ulong](./simd_ulong-1rhpk.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ulong](./simd_ulong-1ri80.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_ulong_sat](./simd_ulong_sat-1lmym.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_ulong_sat](./simd_ulong_sat-1lwse.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_ulong_sat](./simd_ulong_sat-1lrzy.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_ulong_sat](./simd_ulong_sat-1m1q6.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_ulong_sat](./simd_ulong_sat-1ll2i.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_ulong_sat](./simd_ulong_sat-1lv3e.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_ulong_sat](./simd_ulong_sat-1llwi.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_ulong_sat](./simd_ulong_sat-1lvtu.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_ulong_sat](./simd_ulong_sat-1lxxa.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_ulong_sat](./simd_ulong_sat-1lyhe.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_ulong1](./simd_ulong1.md)
  A vector of one 64-bit unsigned integer element.
- [typealias simd_ulong3](./simd_ulong3.md)
  A vector of three 64-bit unsigned integer elements.
- [typealias simd_ulong4](./simd_ulong4.md)
  A vector of four 64-bit unsigned integer elements.
- [typealias simd_ulong8](./simd_ulong8.md)
  A vector of eight 64-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ulong2)*