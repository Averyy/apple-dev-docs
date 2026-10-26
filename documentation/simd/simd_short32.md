# simd_short32

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of thirty-two 16-bit signed integer elements.

## Declaration

```swift
typealias simd_short32 = SIMD32<Int16>
```

```c
typedef short __attribute__((ext_vector_type(32))) simd_short32;
```

## Topics

### Functions to Create Thirty Two-Element Vectors From Other Vectors
- [func simd_make_short32(simd_short2) -> simd_short32](./simd_make_short32%28_%29-ubpt.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_short32(simd_short3) -> simd_short32](./simd_make_short32%28_%29-xjmw.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_short32(simd_short4) -> simd_short32](./simd_make_short32%28_%29-9757.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_short32(simd_short8) -> simd_short32](./simd_make_short32%28_%29-1eywv.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_short32(simd_short16) -> simd_short32](./simd_make_short32%28_%29-9m5sz.md)
  Returns a new vector from the specified sixteen-element vector, and other elements set to zero.
- [func simd_make_short32(simd_short32) -> simd_short32](./simd_make_short32%28_%29-94o20.md)
  Returns a new vector from the specified vector.
- [func simd_make_short32(simd_short16, simd_short16) -> simd_short32](./simd_make_short32%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_short32_undef(simd_short2) -> simd_short32](./simd_make_short32_undef%28_%29-lops.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_short32_undef(simd_short3) -> simd_short32](./simd_make_short32_undef%28_%29-hws9.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_short32_undef(simd_short4) -> simd_short32](./simd_make_short32_undef%28_%29-ri8y.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_short32_undef(simd_short8) -> simd_short32](./simd_make_short32_undef%28_%29-169di.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
- [func simd_make_short32_undef(simd_short16) -> simd_short32](./simd_make_short32_undef%28_%29-435zw.md)
  Returns a new vector from the specified sixteen-element vector, and other elements undefined.
### Functions to Create Thirty Two-Element Vectors From Scalar Values
- [func simd_make_short32(Int16) -> simd_short32](./simd_make_short32%28_%29-8b798.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_short32_undef(Int16) -> simd_short32](./simd_make_short32_undef%28_%29-94vzp.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_short32) -> simd_short32](./simd_abs%28_%29-2cf7j.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_short32, simd_short32, simd_short32) -> simd_short32](./simd_clamp%28_,_,_%29-v73.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_short32, simd_short32) -> simd_bool](./simd_equal%28_,_%29-2cuv8.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_short32) -> Int16](./simd_reduce_min%28_%29-2az34.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_short32) -> Int16](./simd_reduce_max%28_%29-9j1wo.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_short32) -> Int16](./simd_reduce_add%28_%29-1v4iv.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_short32, simd_short32) -> simd_short32](./simd_min%28_,_%29-6joky.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_short32, simd_short32) -> simd_short32](./simd_max%28_,_%29-8macj.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_short32) -> simd_bool](./simd_any%28_%29-3b445.md)
- [func simd_all(simd_short32) -> simd_bool](./simd_all%28_%29-1kcj7.md)
- [func simd_bitselect(simd_short32, simd_short32, simd_short32) -> simd_short32](./simd_bitselect%28_,_,_%29-9so3n.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_short32](./vector_short32.md)

## See Also

### Vector Data Types
- [typealias simd_short1](./simd_short1.md)
  A vector of one 16-bit signed integer element.
- [typealias simd_short2](./simd_short2.md)
  A vector of two 16-bit signed integer elements.
- [typealias simd_short3](./simd_short3.md)
  A vector of three 16-bit signed integer elements.
- [typealias simd_short4](./simd_short4.md)
  A vector of four 16-bit signed integer elements.
- [typealias simd_short8](./simd_short8.md)
  A vector of eight 16-bit signed integer elements.
- [typealias simd_short16](./simd_short16.md)
  A vector of sixteen 16-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_short32)*