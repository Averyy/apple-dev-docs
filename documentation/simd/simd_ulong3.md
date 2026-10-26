# simd_ulong3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 64-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ulong3 = SIMD3<simd_ulong1>
```

```c
typedef unsigned long __attribute__((ext_vector_type(3))) simd_ulong3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_ulong3(simd_ulong2) -> simd_ulong3](./simd_make_ulong3%28_%29-5autj.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_ulong3(simd_ulong3) -> simd_ulong3](./simd_make_ulong3%28_%29-57xdw.md)
  Returns a new vector from the specified vector.
- [func simd_make_ulong3(simd_ulong4) -> simd_ulong3](./simd_make_ulong3%28_%29-5w7y5.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_ulong3(simd_ulong8) -> simd_ulong3](./simd_make_ulong3%28_%29-4pyq9.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_ulong3_undef(simd_ulong2) -> simd_ulong3](./simd_make_ulong3_undef%28_%29-5oqlt.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_ulong3(simd_ulong1) -> simd_ulong3](./simd_make_ulong3%28_%29-3eb9a.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ulong3(simd_ulong1, simd_ulong1, simd_ulong1) -> simd_ulong3](./simd_make_ulong3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_ulong3_undef(simd_ulong1) -> simd_ulong3](./simd_make_ulong3_undef%28_%29-7s0qh.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_ulong3(simd_ulong1, simd_ulong2) -> simd_ulong3](./simd_make_ulong3%28_,_%29-3zpz6.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_ulong3(simd_ulong2, simd_ulong1) -> simd_ulong3](./simd_make_ulong3%28_,_%29-3orcm.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_clamp(simd_ulong3, simd_ulong3, simd_ulong3) -> simd_ulong3](./simd_clamp%28_,_,_%29-5ce6.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ulong3, simd_ulong3) -> simd_bool](./simd_equal%28_,_%29-2p336.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ulong3) -> simd_ulong1](./simd_reduce_min%28_%29-4697f.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ulong3) -> simd_ulong1](./simd_reduce_max%28_%29-4h1hr.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ulong3) -> simd_ulong1](./simd_reduce_add%28_%29-2v51x.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_ulong3, simd_ulong3) -> simd_ulong3](./simd_min%28_,_%29-914t0.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ulong3, simd_ulong3) -> simd_ulong3](./simd_max%28_,_%29-765ec.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ulong3) -> simd_bool](./simd_any%28_%29-69ij0.md)
- [func simd_all(simd_ulong3) -> simd_bool](./simd_all%28_%29-1adyq.md)
- [func simd_bitselect(simd_ulong3, simd_ulong3, simd_long3) -> simd_ulong3](./simd_bitselect%28_,_,_%29-600bp.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ulong3](./vector_ulong3.md)

## See Also

### Vector Data Types
- [typealias simd_ulong1](./simd_ulong1.md)
  A vector of one 64-bit unsigned integer element.
- [typealias simd_ulong2](./simd_ulong2.md)
  A vector of two 64-bit unsigned integer elements.
- [typealias simd_ulong4](./simd_ulong4.md)
  A vector of four 64-bit unsigned integer elements.
- [typealias simd_ulong8](./simd_ulong8.md)
  A vector of eight 64-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ulong3)*