# simd_uchar64

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixty-four 8-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uchar64 = SIMD64<UInt8>
```

```c
typedef unsigned char __attribute__((ext_vector_type(64))) simd_uchar64;
```

## Topics

### Functions to Create Sixty Four-Element Vectors From Other Vectors
- [func simd_make_uchar64(simd_uchar2) -> simd_uchar64](./simd_make_uchar64%28_%29-57u64.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uchar64(simd_uchar3) -> simd_uchar64](./simd_make_uchar64%28_%29-5apn9.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_uchar64(simd_uchar4) -> simd_uchar64](./simd_make_uchar64%28_%29-51eby.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_uchar64(simd_uchar8) -> simd_uchar64](./simd_make_uchar64%28_%29-65i5u.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_uchar64(simd_uchar16) -> simd_uchar64](./simd_make_uchar64%28_%29-3wfeh.md)
  Returns a new vector from the specified sixteen-element vector, and other elements set to zero.
- [func simd_make_uchar64(simd_uchar32) -> simd_uchar64](./simd_make_uchar64%28_%29-56lh8.md)
  Returns a new vector from the specified thirty two-element vector, and other elements set to zero.
- [func simd_make_uchar64(simd_uchar64) -> simd_uchar64](./simd_make_uchar64%28_%29-1g5oc.md)
  Returns a new vector from the specified vector.
- [func simd_make_uchar64(simd_uchar32, simd_uchar32) -> simd_uchar64](./simd_make_uchar64%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_uchar64_undef(simd_uchar2) -> simd_uchar64](./simd_make_uchar64_undef%28_%29-8lvix.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_uchar64_undef(simd_uchar3) -> simd_uchar64](./simd_make_uchar64_undef%28_%29-8ig34.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_uchar64_undef(simd_uchar4) -> simd_uchar64](./simd_make_uchar64_undef%28_%29-8fhu3.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_uchar64_undef(simd_uchar8) -> simd_uchar64](./simd_make_uchar64_undef%28_%29-9jm47.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
- [func simd_make_uchar64_undef(simd_uchar16) -> simd_uchar64](./simd_make_uchar64_undef%28_%29-p0tj.md)
  Returns a new vector from the specified sixteen-element vector, and other elements undefined.
- [func simd_make_uchar64_undef(simd_uchar32) -> simd_uchar64](./simd_make_uchar64_undef%28_%29-9ldf2.md)
  Returns a new vector from the specified thirty two-element vector, and other elements undefined.
### Functions to Create Sixty Four-Element Vectors From Scalar Values
- [func simd_make_uchar64(UInt8) -> simd_uchar64](./simd_make_uchar64%28_%29-9d1w7.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uchar64_undef(UInt8) -> simd_uchar64](./simd_make_uchar64_undef%28_%29-6vlwv.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Reduce Functions
- [func simd_reduce_min(simd_uchar64) -> UInt8](./simd_reduce_min%28_%29-jpn5.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_uchar64) -> UInt8](./simd_reduce_max%28_%29-micz.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uchar64) -> UInt8](./simd_reduce_add%28_%29-936l4.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uchar64, simd_uchar64) -> simd_uchar64](./simd_min%28_,_%29-ep1f.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uchar64, simd_uchar64) -> simd_uchar64](./simd_max%28_,_%29-5la8o.md)
  Returns the maximum value of each element in a vector.
### Common Functions
- [func simd_clamp(simd_uchar64, simd_uchar64, simd_uchar64) -> simd_uchar64](./simd_clamp%28_,_,_%29-52h9h.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uchar64, simd_uchar64) -> simd_bool](./simd_equal%28_,_%29-494kp.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Logic and Bitwise Functions
- [func simd_any(simd_uchar64) -> simd_bool](./simd_any%28_%29-jl1j.md)
- [func simd_all(simd_uchar64) -> simd_bool](./simd_all%28_%29-2m0jp.md)
- [func simd_bitselect(simd_uchar64, simd_uchar64, simd_char64) -> simd_uchar64](./simd_bitselect%28_,_,_%29-2bway.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

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
- [typealias simd_uchar16](./simd_uchar16.md)
  A vector of sixteen 8-bit unsigned integer elements.
- [typealias simd_uchar32](./simd_uchar32.md)
  A vector of thirty-two 8-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uchar64)*