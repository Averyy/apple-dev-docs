# simd_uint4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 32-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uint4 = SIMD4<UInt32>
```

```c
typedef unsigned int __attribute__((ext_vector_type(4))) simd_uint4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_uint4(simd_uint2) -> simd_uint4](./simd_make_uint4%28_%29-236jz.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uint4(simd_uint3) -> simd_uint4](./simd_make_uint4%28_%29-1zpti.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_uint4(simd_uint4) -> simd_uint4](./simd_make_uint4%28_%29-2o2f5.md)
  Returns a new vector from the specified vector.
- [func simd_make_uint4(simd_uint8) -> simd_uint4](./simd_make_uint4%28_%29-333jp.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_uint4(simd_uint16) -> simd_uint4](./simd_make_uint4%28_%29-4a98b.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_uint4(simd_uint2, simd_uint2) -> simd_uint4](./simd_make_uint4%28_,_%29-14dxw.md)
  Returns a new vector from the specified vectors.
- [func simd_make_uint4_undef(simd_uint2) -> simd_uint4](./simd_make_uint4_undef%28_%29-4iaj6.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_uint4_undef(simd_uint3) -> simd_uint4](./simd_make_uint4_undef%28_%29-4lr3n.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_uint4(UInt32) -> simd_uint4](./simd_make_uint4%28_%29-1vdsn.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uint4(UInt32, UInt32, UInt32, UInt32) -> simd_uint4](./simd_make_uint4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_uint4_undef(UInt32) -> simd_uint4](./simd_make_uint4_undef%28_%29-5wuto.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_uint4(simd_uint2, UInt32, UInt32) -> simd_uint4](./simd_make_uint4%28_,_,_%29-5ftg3.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_uint4(simd_uint3, UInt32) -> simd_uint4](./simd_make_uint4%28_,_%29-9arct.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_uint4(UInt32, UInt32, simd_uint2) -> simd_uint4](./simd_make_uint4%28_,_,_%29-73ivt.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_uint4(UInt32, simd_uint2, UInt32) -> simd_uint4](./simd_make_uint4%28_,_,_%29-45zbh.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_uint4(UInt32, simd_uint3) -> simd_uint4](./simd_make_uint4%28_,_%29-4kh9u.md)
  Returns a new vector from a scalar value and a vector.
### Common Functions
- [func simd_clamp(simd_uint4, simd_uint4, simd_uint4) -> simd_uint4](./simd_clamp%28_,_,_%29-1y56u.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<UInt32>, min: UInt32, max: UInt32) -> SIMD4<UInt32>](./clamp%28_,min,max%29-6ix39.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<UInt32>, min: SIMD4<UInt32>, max: SIMD4<UInt32>) -> SIMD4<UInt32>](./clamp%28_,min,max%29-6fsdy.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uint4, simd_uint4) -> simd_bool](./simd_equal%28_,_%29-6tvg4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uint4) -> UInt32](./simd_reduce_min%28_%29-4ukuu.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD4<UInt32>) -> UInt32](./reduce_min%28_%29-3yrpe.md)
  Returns the minimum value in a vector.
- [func simd_reduce_max(simd_uint4) -> UInt32](./simd_reduce_max%28_%29-4qtcm.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD4<UInt32>) -> UInt32](./reduce_max%28_%29-ko69.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uint4) -> UInt32](./simd_reduce_add%28_%29-2ylgg.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD4<UInt32>) -> UInt32](./reduce_add%28_%29-9xs7v.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uint4, simd_uint4) -> simd_uint4](./simd_min%28_,_%29-7hpr6.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD4<UInt32>, UInt32) -> SIMD4<UInt32>](./min%28_,_%29-7l4j0.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD4<UInt32>, SIMD4<UInt32>) -> SIMD4<UInt32>](./min%28_,_%29-7o4pn.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uint4, simd_uint4) -> simd_uint4](./simd_max%28_,_%29-6870v.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD4<UInt32>, UInt32) -> SIMD4<UInt32>](./max%28_,_%29-2m7il.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD4<UInt32>, SIMD4<UInt32>) -> SIMD4<UInt32>](./max%28_,_%29-2pev2.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uint4) -> simd_bool](./simd_any%28_%29-6cz27.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_uint4) -> simd_bool](./simd_all%28_%29-1jm2d.md)
  Returns true if the high-order bit of every element is set; false otherwise.
- [func simd_bitselect(simd_uint4, simd_uint4, simd_int4) -> simd_uint4](./simd_bitselect%28_,_,_%29-1rrhy.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias uint4](./uint4.md)
- [typealias vector_uint4](./vector_uint4.md)

## See Also

### Vector Data Types
- [typealias simd_uint1](./simd_uint1.md)
  A vector of one 32-bit unsigned integer element.
- [typealias simd_uint2](./simd_uint2.md)
  A vector of two 32-bit unsigned integer elements.
- [typealias simd_uint3](./simd_uint3.md)
  A vector of three 32-bit unsigned integer elements.
- [typealias simd_uint8](./simd_uint8.md)
  A vector of eight 32-bit unsigned integer elements.
- [typealias simd_uint16](./simd_uint16.md)
  A vector of sixteen 32-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uint4)*