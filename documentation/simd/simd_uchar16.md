# simd_uchar16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixteen 8-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uchar16 = SIMD16<UInt8>
```

```c
typedef unsigned char __attribute__((ext_vector_type(16))) simd_uchar16;
```

## Topics

### Functions to Create Sixteen-Element Vectors From Other Vectors
- [func simd_make_uchar16(simd_uchar2) -> simd_uchar16](./simd_make_uchar16%28_%29-3fz5p.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uchar16(simd_uchar3) -> simd_uchar16](./simd_make_uchar16%28_%29-3d3no.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_uchar16(simd_uchar4) -> simd_uchar16](./simd_make_uchar16%28_%29-39lkf.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_uchar16(simd_uchar8) -> simd_uchar16](./simd_make_uchar16%28_%29-2v4kz.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_uchar16(simd_uchar16) -> simd_uchar16](./simd_make_uchar16%28_%29-3jakr.md)
  Returns a new vector from the specified vector.
- [func simd_make_uchar16(simd_uchar32) -> simd_uchar16](./simd_make_uchar16%28_%29-1q2p8.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_uchar16(simd_uchar64) -> simd_uchar16](./simd_make_uchar16%28_%29-4u0bo.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_uchar16(simd_uchar8, simd_uchar8) -> simd_uchar16](./simd_make_uchar16%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_uchar16_undef(simd_uchar2) -> simd_uchar16](./simd_make_uchar16_undef%28_%29-7pk27.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_uchar16_undef(simd_uchar3) -> simd_uchar16](./simd_make_uchar16_undef%28_%29-7sziu.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_uchar16_undef(simd_uchar4) -> simd_uchar16](./simd_make_uchar16_undef%28_%29-7jo0t.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_uchar16_undef(simd_uchar8) -> simd_uchar16](./simd_make_uchar16_undef%28_%29-74mxt.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
### Functions to Create Sixteen-Element Vectors From Scalar Values
- [func simd_make_uchar16(UInt8) -> simd_uchar16](./simd_make_uchar16%28_%29-v6ux.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uchar16_undef(UInt8) -> simd_uchar16](./simd_make_uchar16_undef%28_%29-4x6v6.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_uchar16, simd_uchar16, simd_uchar16) -> simd_uchar16](./simd_clamp%28_,_,_%29-1zlhc.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uchar16, simd_uchar16) -> simd_bool](./simd_equal%28_,_%29-6la77.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uchar16) -> UInt8](./simd_reduce_min%28_%29-3d193.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_uchar16) -> UInt8](./simd_reduce_max%28_%29-8inet.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uchar16) -> UInt8](./simd_reduce_add%28_%29-7n460.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uchar16, simd_uchar16) -> simd_uchar16](./simd_min%28_,_%29-8haop.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uchar16, simd_uchar16) -> simd_uchar16](./simd_max%28_,_%29-248h3.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uchar16) -> simd_bool](./simd_any%28_%29-933sa.md)
- [func simd_all(simd_uchar16) -> simd_bool](./simd_all%28_%29-ikbg.md)
- [func simd_bitselect(simd_uchar16, simd_uchar16, simd_char16) -> simd_uchar16](./simd_bitselect%28_,_,_%29-9i5ku.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_uchar16](./vector_uchar16.md)

## See Also

### Vector Data Types
- [typealias simd_uchar1](./simd_uchar1.md)
  A vector of one 8-bit unsigned integer element.
- [typealias simd_uchar2](./simd_uchar2.md)
  A vector of two 8-bit unsigned integer elements.
- [typealias simd_uchar3](./simd_uchar3.md)
  A vector of three 8-bit unsigned integer elements.
- [typealias simd_uchar4](./simd_uchar4.md)
  A vector of four 8-bit unsigned integer elements.
- [typealias simd_uchar8](./simd_uchar8.md)
  A vector of eight 8-bit unsigned integer elements.
- [typealias simd_uchar32](./simd_uchar32.md)
  A vector of thirty-two 8-bit unsigned integer elements.
- [typealias simd_uchar64](./simd_uchar64.md)
  A vector of sixty-four 8-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uchar16)*