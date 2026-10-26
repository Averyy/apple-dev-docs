# simd_short16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixteen 16-bit signed integer elements.

## Declaration

```swift
typealias simd_short16 = SIMD16<Int16>
```

```c
typedef short __attribute__((ext_vector_type(16))) simd_short16;
```

## Topics

### Functions to Create Sixteen-Element Vectors From Other Vectors
- [func simd_make_short16(simd_short2) -> simd_short16](./simd_make_short16%28_%29-8892t.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_short16(simd_short3) -> simd_short16](./simd_make_short16%28_%29-8bejg.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_short16(simd_short4) -> simd_short16](./simd_make_short16%28_%29-82czr.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_short16(simd_short8) -> simd_short16](./simd_make_short16%28_%29-984rv.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_short16(simd_short16) -> simd_short16](./simd_make_short16%28_%29-5xtuv.md)
  Returns a new vector from the specified vector.
- [func simd_make_short16(simd_short32) -> simd_short16](./simd_make_short16%28_%29-4ubc7.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_short16(simd_short8, simd_short8) -> simd_short16](./simd_make_short16%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_short16_undef(simd_short2) -> simd_short16](./simd_make_short16_undef%28_%29-19u0l.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_short16_undef(simd_short3) -> simd_short16](./simd_make_short16_undef%28_%29-150ws.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_short16_undef(simd_short4) -> simd_short16](./simd_make_short16_undef%28_%29-11st3.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_short16_undef(simd_short8) -> simd_short16](./simd_make_short16_undef%28_%29-27knv.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
### Functions to Create Sixteen-Element Vectors From Scalar Values
- [func simd_make_short16(Int16) -> simd_short16](./simd_make_short16%28_%29-3x8mr.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_short16_undef(Int16) -> simd_short16](./simd_make_short16_undef%28_%29-mhi.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_short16) -> simd_short16](./simd_abs%28_%29-47an0.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_short16, simd_short16, simd_short16) -> simd_short16](./simd_clamp%28_,_,_%29-9ykva.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_short16, simd_short16) -> simd_bool](./simd_equal%28_,_%29-220xu.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_short16) -> Int16](./simd_reduce_min%28_%29-3cwd3.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_short16) -> Int16](./simd_reduce_max%28_%29-8iihx.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_short16) -> Int16](./simd_reduce_add%28_%29-7mz6g.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_short16, simd_short16) -> simd_short16](./simd_min%28_,_%29-9vjqx.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_short16, simd_short16) -> simd_short16](./simd_max%28_,_%29-9xf7i.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_short16) -> simd_bool](./simd_any%28_%29-92yq2.md)
- [func simd_all(simd_short16) -> simd_bool](./simd_all%28_%29-i5jw.md)
- [func simd_bitselect(simd_short16, simd_short16, simd_short16) -> simd_short16](./simd_bitselect%28_,_,_%29-3vpt5.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_short16](./vector_short16.md)

## See Also

### Vector Data Types
- [typealias simd_short1](./simd_short1.md)
  A vector of one 16-bit signed integer element.
- [typealias simd_short2](./simd_short2.md)
  A vector of two 16-bit signed integer elements.
- [typealias simd_short3](./simd_short3.md)
  A vector of three 16-bit signed integer elements.
- [typealias simd_short4](./simd_short4.md)
  A vector of four 16-bit signed integer elements.
- [typealias simd_short8](./simd_short8.md)
  A vector of eight 16-bit signed integer elements.
- [typealias simd_short32](./simd_short32.md)
  A vector of thirty-two 16-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_short16)*