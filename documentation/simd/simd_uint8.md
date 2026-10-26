# simd_uint8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 32-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uint8 = SIMD8<UInt32>
```

```c
typedef unsigned int __attribute__((ext_vector_type(8))) simd_uint8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_uint8(simd_uint2) -> simd_uint8](./simd_make_uint8%28_%29-2vaoh.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uint8(simd_uint3) -> simd_uint8](./simd_make_uint8%28_%29-2rtxs.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_uint8(simd_uint4) -> simd_uint8](./simd_make_uint8%28_%29-2ovzr.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_uint8(simd_uint8) -> simd_uint8](./simd_make_uint8%28_%29-3sztf.md)
  Returns a new vector from the specified vector.
- [func simd_make_uint8(simd_uint16) -> simd_uint8](./simd_make_uint8%28_%29-64gkj.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_uint8(simd_uint4, simd_uint4) -> simd_uint8](./simd_make_uint8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_uint8_undef(simd_uint2) -> simd_uint8](./simd_make_uint8_undef%28_%29-ck1m.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_uint8_undef(simd_uint3) -> simd_uint8](./simd_make_uint8_undef%28_%29-hojv.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_uint8_undef(simd_uint4) -> simd_uint8](./simd_make_uint8_undef%28_%29-6a8k.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_uint8(UInt32) -> simd_uint8](./simd_make_uint8%28_%29-7jqj3.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uint8_undef(UInt32) -> simd_uint8](./simd_make_uint8_undef%28_%29-8p5i8.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_uint8, simd_uint8, simd_uint8) -> simd_uint8](./simd_clamp%28_,_,_%29-9evfi.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uint8, simd_uint8) -> simd_bool](./simd_equal%28_,_%29-1v1wn.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uint8) -> UInt32](./simd_reduce_min%28_%29-3o9f6.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_uint8) -> UInt32](./simd_reduce_max%28_%29-55ah6.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uint8) -> UInt32](./simd_reduce_add%28_%29-3av90.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uint8, simd_uint8) -> simd_uint8](./simd_min%28_,_%29-873mx.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uint8, simd_uint8) -> simd_uint8](./simd_max%28_,_%29-4l2k6.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uint8) -> simd_bool](./simd_any%28_%29-6p8mz.md)
- [func simd_all(simd_uint8) -> simd_bool](./simd_all%28_%29-1ynbd.md)
- [func simd_bitselect(simd_uint8, simd_uint8, simd_int8) -> simd_uint8](./simd_bitselect%28_,_,_%29-803fj.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_uint8](./vector_uint8.md)

## See Also

### Vector Data Types
- [typealias simd_uint1](./simd_uint1.md)
  A vector of one 32-bit unsigned integer element.
- [typealias simd_uint2](./simd_uint2.md)
  A vector of two 32-bit unsigned integer elements.
- [typealias simd_uint3](./simd_uint3.md)
  A vector of three 32-bit unsigned integer elements.
- [typealias simd_uint4](./simd_uint4.md)
  A vector of four 32-bit unsigned integer elements.
- [typealias simd_uint16](./simd_uint16.md)
  A vector of sixteen 32-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uint8)*