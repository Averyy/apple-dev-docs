# simd_uint2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 32-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uint2 = SIMD2<UInt32>
```

```c
typedef unsigned int __attribute__((ext_vector_type(2))) simd_uint2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_uint2(simd_uint2) -> simd_uint2](./simd_make_uint2%28_%29-3fnd3.md)
  Returns a new vector from the specified vector.
- [func simd_make_uint2(simd_uint3) -> simd_uint2](./simd_make_uint2%28_%29-3cbr2.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_uint2(simd_uint4) -> simd_uint2](./simd_make_uint2%28_%29-3m281.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_uint2(simd_uint8) -> simd_uint2](./simd_make_uint2%28_%29-40jb1.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_uint2(simd_uint16) -> simd_uint2](./simd_make_uint2%28_%29-9b05l.md)
  Returns a new vector by truncating the specified sixteen-element vector.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_uint2(UInt32) -> simd_uint2](./simd_make_uint2%28_%29-82fnu.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uint2(UInt32, UInt32) -> simd_uint2](./simd_make_uint2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_uint2_undef(UInt32) -> simd_uint2](./simd_make_uint2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_uint2, simd_uint2, simd_uint2) -> simd_uint2](./simd_clamp%28_,_,_%29-5yp7.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<UInt32>, min: UInt32, max: UInt32) -> SIMD2<UInt32>](./clamp%28_,min,max%29-5cyx4.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<UInt32>, min: SIMD2<UInt32>, max: SIMD2<UInt32>) -> SIMD2<UInt32>](./clamp%28_,min,max%29-59rk7.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uint2, simd_uint2) -> simd_bool](./simd_equal%28_,_%29-2urgh.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uint2) -> UInt32](./simd_reduce_min%28_%29-49p5s.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD2<UInt32>) -> UInt32](./reduce_min%28_%29-2b4fr.md)
  Returns the minimum value in a vector.
- [func simd_reduce_max(simd_uint2) -> UInt32](./simd_reduce_max%28_%29-4ket4.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD2<UInt32>) -> UInt32](./reduce_max%28_%29-5dxp4.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uint2) -> UInt32](./simd_reduce_add%28_%29-2q44e.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD2<UInt32>) -> UInt32](./reduce_add%28_%29-5uvts.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uint2, simd_uint2) -> simd_uint2](./simd_min%28_,_%29-9b5n7.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD2<UInt32>, UInt32) -> SIMD2<UInt32>](./min%28_,_%29-6xef7.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD2<UInt32>, SIMD2<UInt32>) -> SIMD2<UInt32>](./min%28_,_%29-70ls4.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uint2, simd_uint2) -> simd_uint2](./simd_max%28_,_%29-8931y.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD2<UInt32>, UInt32) -> SIMD2<UInt32>](./max%28_,_%29-9ch4d.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD2<UInt32>, SIMD2<UInt32>) -> SIMD2<UInt32>](./max%28_,_%29-9fm5e.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uint2) -> simd_bool](./simd_any%28_%29-64hll.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_uint2) -> simd_bool](./simd_all%28_%29-1d7bv.md)
  Returns true if the high-order bit of every element is set; false otherwise.
- [func simd_bitselect(simd_uint2, simd_uint2, simd_int2) -> simd_uint2](./simd_bitselect%28_,_,_%29-5dqwa.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias uint2](./uint2.md)
- [typealias vector_uint2](./vector_uint2.md)

## See Also

### Vector Data Types
- [typealias simd_uint1](./simd_uint1.md)
  A vector of one 32-bit unsigned integer element.
- [typealias simd_uint3](./simd_uint3.md)
  A vector of three 32-bit unsigned integer elements.
- [typealias simd_uint4](./simd_uint4.md)
  A vector of four 32-bit unsigned integer elements.
- [typealias simd_uint8](./simd_uint8.md)
  A vector of eight 32-bit unsigned integer elements.
- [typealias simd_uint16](./simd_uint16.md)
  A vector of sixteen 32-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uint2)*