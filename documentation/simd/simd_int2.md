# simd_int2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 32-bit signed integer elements.

## Declaration

```swift
typealias simd_int2 = SIMD2<Int32>
```

```c
typedef int __attribute__((ext_vector_type(2))) simd_int2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_int2(simd_int2) -> simd_int2](./simd_make_int2%28_%29-1j0r7.md)
  Returns a new vector from the specified vector.
- [func simd_make_int2(simd_int3) -> simd_int2](./simd_make_int2%28_%29-1mclu.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_int2(simd_int4) -> simd_int2](./simd_make_int2%28_%29-1qyb9.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_int2(simd_int8) -> simd_int2](./simd_make_int2%28_%29-23rr5.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_int2(simd_int16) -> simd_int2](./simd_make_int2%28_%29-4okip.md)
  Returns a new vector by truncating the specified sixteen-element vector.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_int2(Int32) -> simd_int2](./simd_make_int2%28_%29-3zby.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_int2(Int32, Int32) -> simd_int2](./simd_make_int2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_int2_undef(Int32) -> simd_int2](./simd_make_int2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_int2) -> simd_int2](./simd_abs%28_%29-88kbu.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD2<Int32>) -> SIMD2<Int32>](./abs%28_%29-770jg.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_int2, simd_int2, simd_int2) -> simd_int2](./simd_clamp%28_,_,_%29-9n2rx.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Int32>, min: SIMD2<Int32>, max: SIMD2<Int32>) -> SIMD2<Int32>](./clamp%28_,min,max%29-y596.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Int32>, min: Int32, max: Int32) -> SIMD2<Int32>](./clamp%28_,min,max%29-11cyt.md)
  Returns each element in a vector clamped to a specified scalar range.
- [func simd_equal(simd_int2, simd_int2) -> simd_bool](./simd_equal%28_,_%29-8sg1t.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_int2) -> Int32](./simd_reduce_min%28_%29-49f1c.md)
  Returns the minimum value in a vector.
- [func reduce_min(SIMD2<Int32>) -> Int32](./reduce_min%28_%29-34ha7.md)
  Returns the minimum value in a vector.
- [func simd_reduce_max(simd_int2) -> Int32](./simd_reduce_max%28_%29-4kojc.md)
  Returns the maximum value in a vector.
- [func reduce_max(SIMD2<Int32>) -> Int32](./reduce_max%28_%29-6qw44.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_int2) -> Int32](./simd_reduce_add%28_%29-2qeam.md)
  Returns the sum of all elements in a vector.
- [func reduce_add(SIMD2<Int32>) -> Int32](./reduce_add%28_%29-4edwc.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_max(simd_int2, simd_int2) -> simd_int2](./simd_max%28_,_%29-2xs4j.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD2<Int32>, SIMD2<Int32>) -> SIMD2<Int32>](./max%28_,_%29-9xpv0.md)
  Returns the maximum value of each element in a vector.
- [func max(SIMD2<Int32>, Int32) -> SIMD2<Int32>](./max%28_,_%29-9uijf.md)
  Returns the maximum value of each element in a vector.
- [func simd_min(simd_int2, simd_int2) -> simd_int2](./simd_min%28_,_%29-3focz.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD2<Int32>, SIMD2<Int32>) -> SIMD2<Int32>](./min%28_,_%29-jyi5.md)
  Returns the minimum value of each element in a vector.
- [func min(SIMD2<Int32>, Int32) -> SIMD2<Int32>](./min%28_,_%29-goji.md)
  Returns the minimum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_int2) -> simd_bool](./simd_any%28_%29-64rh5.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_int2) -> simd_bool](./simd_all%28_%29-1cxjv.md)
  Returns true if the high-order bit of every element is set; false otherwise.
- [func simd_bitselect(simd_int2, simd_int2, simd_int2) -> simd_int2](./simd_bitselect%28_,_,_%29-6p66c.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias int2](./int2.md)
- [typealias vector_int2](./vector_int2.md)

## See Also

### Vector Data Types
- [typealias simd_int1](./simd_int1.md)
  A vector of one 32-bit signed integer element.
- [typealias simd_int3](./simd_int3.md)
  A vector of three 32-bit signed integer elements.
- [typealias simd_int4](./simd_int4.md)
  A vector of four 32-bit signed integer elements.
- [typealias simd_int8](./simd_int8.md)
  A vector of eight 32-bit signed integer elements.
- [typealias simd_int16](./simd_int16.md)
  A vector of sixteen 32-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_int2)*