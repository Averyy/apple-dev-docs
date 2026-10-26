# simd_uint3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 32-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uint3 = SIMD3<UInt32>
```

```c
typedef unsigned int __attribute__((ext_vector_type(3))) simd_uint3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_uint3(simd_uint2) -> simd_uint3](./simd_make_uint3%28_%29-7e6jd.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uint3(simd_uint3) -> simd_uint3](./simd_make_uint3%28_%29-7h348.md)
  Returns a new vector from the specified vector.
- [func simd_make_uint3(simd_uint4) -> simd_uint3](./simd_make_uint3%28_%29-77mmf.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_uint3(simd_uint8) -> simd_uint3](./simd_make_uint3%28_%29-6sqjv.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_uint3(simd_uint16) -> simd_uint3](./simd_make_uint3%28_%29-6rqe9.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_uint3_undef(simd_uint2) -> simd_uint3](./simd_make_uint3_undef%28_%29-3a81k.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_uint3(UInt32) -> simd_uint3](./simd_make_uint3%28_%29-512r5.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uint3(UInt32, UInt32, UInt32) -> simd_uint3](./simd_make_uint3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_uint3_undef(UInt32) -> simd_uint3](./simd_make_uint3_undef%28_%29-1waea.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector3](./vector3-3qyta.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_uint3(simd_uint2, UInt32) -> simd_uint3](./simd_make_uint3%28_,_%29-5y5kc.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_uint3(UInt32, simd_uint2) -> simd_uint3](./simd_make_uint3%28_,_%29-210g2.md)
  Returns a new vector from a vector and a scalar value.
- [vector3](./vector3-3xwc.md)
  Returns a new vector from a scalar value and a vector.
### Common Functions
- [func simd_clamp(simd_uint3, simd_uint3, simd_uint3) -> simd_uint3](./simd_clamp%28_,_,_%29-7ssi2.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<UInt32>, min: UInt32, max: UInt32) -> SIMD3<UInt32>](./clamp%28_,min,max%29-dhvg.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<UInt32>, min: SIMD3<UInt32>, max: SIMD3<UInt32>) -> SIMD3<UInt32>](./clamp%28_,min,max%29-gp7z.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uint3, simd_uint3) -> simd_bool](./simd_equal%28_,_%29-57xz1.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uint3) -> UInt32](./simd_reduce_min%28_%29-4688x.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD3<UInt32>) -> UInt32](./reduce_min%28_%29-1yst6.md)
  Returns the minimum value in a vector.
- [func simd_reduce_max(simd_uint3) -> UInt32](./simd_reduce_max%28_%29-4h33d.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD3<UInt32>) -> UInt32](./reduce_max%28_%29-1h2j7.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uint3) -> UInt32](./simd_reduce_add%28_%29-2v3pj.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD3<UInt32>) -> UInt32](./reduce_add%28_%29-7drmm.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uint3, simd_uint3) -> simd_uint3](./simd_min%28_,_%29-2sp22.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD3<UInt32>, UInt32) -> SIMD3<UInt32>](./min%28_,_%29-9iyne.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD3<UInt32>, SIMD3<UInt32>) -> SIMD3<UInt32>](./min%28_,_%29-9ftkl.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uint3, simd_uint3) -> simd_uint3](./simd_max%28_,_%29-7a6cq.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD3<UInt32>, UInt32) -> SIMD3<UInt32>](./max%28_,_%29-703ka.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD3<UInt32>, SIMD3<UInt32>) -> SIMD3<UInt32>](./max%28_,_%29-6ww7t.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uint3) -> simd_bool](./simd_any%28_%29-69h3c.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_uint3) -> simd_bool](./simd_all%28_%29-1afl6.md)
  Returns true if the high-order bit of every element is set; false otherwise.
- [func simd_bitselect(simd_uint3, simd_uint3, simd_int3) -> simd_uint3](./simd_bitselect%28_,_,_%29-4hak.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias uint3](./uint3.md)
- [typealias vector_uint3](./vector_uint3.md)
### Functions to Create Three-Element Vectors From Vectors of Other Types
- [simd_uint](./simd_uint-7h2bf.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_uint](./simd_uint-7gs6z.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_uint](./simd_uint-7h797.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_uint](./simd_uint-7gxbv.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_uint](./simd_uint-7h087.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_uint](./simd_uint-7gqav.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_uint](./simd_uint-7gzhl.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_uint](./simd_uint-7gpgp.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_uint](./simd_uint-7grch.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_uint](./simd_uint-7grux.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_uint_sat](./simd_uint_sat-ncn5.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_uint_sat](./simd_uint_sat-n2o1.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_uint_sat](./simd_uint_sat-nhgh.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_uint_sat](./simd_uint_sat-n7q9.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_uint_sat](./simd_uint_sat-nfrd.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_uint_sat](./simd_uint_sat-n5op.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_uint_sat](./simd_uint_sat-ngif.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_uint_sat](./simd_uint_sat-n6qf.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_uint_sat](./simd_uint_sat-n3iz.md)
  Returns a new vector from the specified vector of 32-bit, floating point elements.
- [simd_uint_sat](./simd_uint_sat-n44n.md)
  Returns a new vector from the specified vector of 64-bit, floating point elements.

## See Also

### Vector Data Types
- [typealias simd_uint1](./simd_uint1.md)
  A vector of one 32-bit unsigned integer element.
- [typealias simd_uint2](./simd_uint2.md)
  A vector of two 32-bit unsigned integer elements.
- [typealias simd_uint4](./simd_uint4.md)
  A vector of four 32-bit unsigned integer elements.
- [typealias simd_uint8](./simd_uint8.md)
  A vector of eight 32-bit unsigned integer elements.
- [typealias simd_uint16](./simd_uint16.md)
  A vector of sixteen 32-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uint3)*