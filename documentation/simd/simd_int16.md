# simd_int16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixteen 32-bit signed integer elements.

## Declaration

```swift
typealias simd_int16 = SIMD16<Int32>
```

```c
typedef int __attribute__((ext_vector_type(16))) simd_int16;
```

## Topics

### Functions to Create Sixteen-Element Vectors From Other Vectors
- [func simd_make_int16(simd_int2) -> simd_int16](./simd_make_int16%28_%29-35atp.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_int16(simd_int3) -> simd_int16](./simd_make_int16%28_%29-31p8k.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_int16(simd_int4) -> simd_int16](./simd_make_int16%28_%29-3b5u3.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_int16(simd_int8) -> simd_int16](./simd_make_int16%28_%29-25e3r.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_int16(simd_int16) -> simd_int16](./simd_make_int16%28_%29-4wuqs.md)
  Returns a new vector from the specified vector.
- [func simd_make_int16(simd_int8, simd_int8) -> simd_int16](./simd_make_int16%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_int16_undef(simd_int2) -> simd_int16](./simd_make_int16_undef%28_%29-3zkgc.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_int16_undef(simd_int3) -> simd_int16](./simd_make_int16_undef%28_%29-431ed.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_int16_undef(simd_int4) -> simd_int16](./simd_make_int16_undef%28_%29-3eopu.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_int16_undef(simd_int8) -> simd_int16](./simd_make_int16_undef%28_%29-4lk92.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
### Functions to Create Sixteen-Element Vectors From Scalar Values
- [func simd_make_int16(Int32) -> simd_int16](./simd_make_int16%28_%29-26gfd.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_int16_undef(Int32) -> simd_int16](./simd_make_int16_undef%28_%29-6radb.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_int16) -> simd_int16](./simd_abs%28_%29-477j8.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_int16, simd_int16, simd_int16) -> simd_int16](./simd_clamp%28_,_,_%29-5xcny.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_int16, simd_int16) -> simd_bool](./simd_equal%28_,_%29-5fwh2.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_int16) -> Int32](./simd_reduce_min%28_%29-3coa3.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_int16) -> Int32](./simd_reduce_max%28_%29-8igr1.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_int16) -> Int32](./simd_reduce_add%28_%29-7msaw.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_int16, simd_int16) -> simd_int16](./simd_min%28_,_%29-3f9xy.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_int16, simd_int16) -> simd_int16](./simd_max%28_,_%29-ybh4.md)
  Returns the maximum value of each element in a vector.
### Alternative Type Alias
- [typealias vector_int16](./vector_int16.md)
### Logic and Bitwise Functions
- [func simd_any(simd_int16) -> simd_bool](./simd_any%28_%29-92rsm.md)
- [func simd_all(simd_int16) -> simd_bool](./simd_all%28_%29-idpg.md)
- [func simd_bitselect(simd_int16, simd_int16, simd_int16) -> simd_int16](./simd_bitselect%28_,_,_%29-9fgtc.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## See Also

### Vector Data Types
- [typealias simd_int1](./simd_int1.md)
  A vector of one 32-bit signed integer element.
- [typealias simd_int2](./simd_int2.md)
  A vector of two 32-bit signed integer elements.
- [typealias simd_int3](./simd_int3.md)
  A vector of three 32-bit signed integer elements.
- [typealias simd_int4](./simd_int4.md)
  A vector of four 32-bit signed integer elements.
- [typealias simd_int8](./simd_int8.md)
  A vector of eight 32-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_int16)*