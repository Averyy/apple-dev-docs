# simd_uchar3

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of three 8-bit unsigned integer elements.

## Declaration

```swift
typealias simd_uchar3 = SIMD3<UInt8>
```

```c
typedef unsigned char __attribute__((ext_vector_type(3))) simd_uchar3;
```

## Topics

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_uchar3(simd_uchar2) -> simd_uchar3](./simd_make_uchar3%28_%29-4qkxz.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uchar3(simd_uchar3) -> simd_uchar3](./simd_make_uchar3%28_%29-4nmxq.md)
  Returns a new vector from the specified vector.
- [func simd_make_uchar3(simd_uchar4) -> simd_uchar3](./simd_make_uchar3%28_%29-45nsd.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_uchar3(simd_uchar8) -> simd_uchar3](./simd_make_uchar3%28_%29-3sucp.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_uchar3(simd_uchar16) -> simd_uchar3](./simd_make_uchar3%28_%29-90ge7.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_uchar3(simd_uchar32) -> simd_uchar3](./simd_make_uchar3%28_%29-38lno.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_uchar3(simd_uchar64) -> simd_uchar3](./simd_make_uchar3%28_%29-3p7i8.md)
  Returns a new vector by truncating the specified sixty four-element vector.
- [func simd_make_uchar3_undef(simd_uchar2) -> simd_uchar3](./simd_make_uchar3_undef%28_%29-99t25.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_uchar3(UInt8) -> simd_uchar3](./simd_make_uchar3%28_%29-bybh.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uchar3(UInt8, UInt8, UInt8) -> simd_uchar3](./simd_make_uchar3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_uchar3_undef(UInt8) -> simd_uchar3](./simd_make_uchar3_undef%28_%29-562ub.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Functions to Create Three-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_uchar3(simd_uchar2, UInt8) -> simd_uchar3](./simd_make_uchar3%28_,_%29-5tgih.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_uchar3(UInt8, simd_uchar2) -> simd_uchar3](./simd_make_uchar3%28_,_%29-2m5x7.md)
  Returns a new vector from a scalar value and a vector.
### Common Functions
- [func simd_clamp(simd_uchar3, simd_uchar3, simd_uchar3) -> simd_uchar3](./simd_clamp%28_,_,_%29-6h8i3.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uchar3, simd_uchar3) -> simd_bool](./simd_equal%28_,_%29-8iga0.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_uchar3) -> UInt8](./simd_reduce_min%28_%29-46bd5.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_uchar3) -> UInt8](./simd_reduce_max%28_%29-4gzsh.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_uchar3) -> UInt8](./simd_reduce_add%28_%29-2v6nn.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_uchar3, simd_uchar3) -> simd_uchar3](./simd_min%28_,_%29-8h62y.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_uchar3, simd_uchar3) -> simd_uchar3](./simd_max%28_,_%29-8ylny.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_uchar3) -> simd_bool](./simd_any%28_%29-69k4o.md)
- [func simd_all(simd_uchar3) -> simd_bool](./simd_all%28_%29-1aceu.md)
- [func simd_bitselect(simd_uchar3, simd_uchar3, simd_char3) -> simd_uchar3](./simd_bitselect%28_,_,_%29-2syfj.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_uchar3](./vector_uchar3.md)

## See Also

### Vector Data Types
- [typealias simd_uchar1](./simd_uchar1.md)
  A vector of one 8-bit unsigned integer element.
- [typealias simd_uchar2](./simd_uchar2.md)
  A vector of two 8-bit unsigned integer elements.
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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_uchar3)*