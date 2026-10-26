# simd_uchar2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 8-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uchar2 = SIMD2<UInt8>
```

```c
typedef unsigned char __attribute__((ext_vector_type(2))) simd_uchar2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_uchar2(simd_uchar2) -> simd_uchar2](./simd_make_uchar2%28_%29-5a6cb.md)
  Returns a new vector from the specified vector.
- [func simd_make_uchar2(simd_uchar3) -> simd_uchar2](./simd_make_uchar2%28_%29-5dlsy.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_uchar2(simd_uchar4) -> simd_uchar2](./simd_make_uchar2%28_%29-5vkwh.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_uchar2(simd_uchar8) -> simd_uchar2](./simd_make_uchar2%28_%29-4p97x.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_uchar2(simd_uchar16) -> simd_uchar2](./simd_make_uchar2%28_%29-6etds.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_uchar2(simd_uchar32) -> simd_uchar2](./simd_make_uchar2%28_%29-4hies.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_uchar2(simd_uchar64) -> simd_uchar2](./simd_make_uchar2%28_%29-1bfr0.md)
  Returns a new vector by truncating the specified sixty four-element vector.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_uchar2(UInt8) -> simd_uchar2](./simd_make_uchar2%28_%29-152cz.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uchar2(UInt8, UInt8) -> simd_uchar2](./simd_make_uchar2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_uchar2_undef(UInt8) -> simd_uchar2](./simd_make_uchar2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_uchar2, simd_uchar2, simd_uchar2) -> simd_uchar2](./simd_clamp%28_,_,_%29-71hrv.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uchar2, simd_uchar2) -> simd_bool](./simd_equal%28_,_%29-7ujh6.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uchar2) -> UInt8](./simd_reduce_min%28_%29-49quo.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_uchar2) -> UInt8](./simd_reduce_max%28_%29-4khx4.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uchar2) -> UInt8](./simd_reduce_add%28_%29-2q16y.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uchar2, simd_uchar2) -> simd_uchar2](./simd_min%28_,_%29-45w1z.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uchar2, simd_uchar2) -> simd_uchar2](./simd_max%28_,_%29-8i357.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uchar2) -> simd_bool](./simd_any%28_%29-64ekh.md)
- [func simd_all(simd_uchar2) -> simd_bool](./simd_all%28_%29-1dafz.md)
- [func simd_bitselect(simd_uchar2, simd_uchar2, simd_char2) -> simd_uchar2](./simd_bitselect%28_,_,_%29-2yxn9.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_uchar2](./vector_uchar2.md)

## See Also

### Vector Data Types
- [typealias simd_uchar1](./simd_uchar1.md)
  A vector of one 8-bit unsigned integer element.
- [typealias simd_uchar3](./simd_uchar3.md)
  A vector of three 8-bit unsigned integer elements.
- [typealias simd_uchar4](./simd_uchar4.md)
  A vector of four 8-bit unsigned integer elements.
- [typealias simd_uchar8](./simd_uchar8.md)
  A vector of eight 8-bit unsigned integer elements.
- [typealias simd_uchar16](./simd_uchar16.md)
  A vector of sixteen 8-bit unsigned integer elements.
- [typealias simd_uchar32](./simd_uchar32.md)
  A vector of thirty-two 8-bit unsigned integer elements.
- [typealias simd_uchar64](./simd_uchar64.md)
  A vector of sixty-four 8-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uchar2)*