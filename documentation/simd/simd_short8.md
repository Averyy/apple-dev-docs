# simd_short8

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of eight 16-bit signed integer elements.

## Declaration

```swift
typealias simd_short8 = SIMD8<Int16>
```

```c
typedef short __attribute__((ext_vector_type(8))) simd_short8;
```

## Topics

### Functions to Create Eight-Element Vectors From Other Vectors
- [func simd_make_short8(simd_short2) -> simd_short8](./simd_make_short8%28_%29-600rc.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_short8(simd_short3) -> simd_short8](./simd_make_short8%28_%29-5wv29.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_short8(simd_short4) -> simd_short8](./simd_make_short8%28_%29-6l7oy.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_short8(simd_short8) -> simd_short8](./simd_make_short8%28_%29-5gjta.md)
  Returns a new vector from the specified vector.
- [func simd_make_short8(simd_short16) -> simd_short8](./simd_make_short8%28_%29-22n5y.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_short8(simd_short32) -> simd_short8](./simd_make_short8%28_%29-8mc9h.md)
  Returns a new vector by truncating the specified thrity two-element vector.
- [func simd_make_short8(simd_short4, simd_short4) -> simd_short8](./simd_make_short8%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_short8_undef(simd_short2) -> simd_short8](./simd_make_short8_undef%28_%29-54hbi.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_short8_undef(simd_short3) -> simd_short8](./simd_make_short8_undef%28_%29-57mlz.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_short8_undef(simd_short4) -> simd_short8](./simd_make_short8_undef%28_%29-5ny5g.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [vector8](./vector8-7jnqf.md)
  Returns a new vector from the specified vectors.
### Functions to Create Eight-Element Vectors From Scalar Values
- [func simd_make_short8(Int16) -> simd_short8](./simd_make_short8%28_%29-1jz7f.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_short8_undef(Int16) -> simd_short8](./simd_make_short8_undef%28_%29-7945n.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_short8) -> simd_short8](./simd_abs%28_%29-7otzk.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_short8, simd_short8, simd_short8) -> simd_short8](./simd_clamp%28_,_,_%29-3cc2g.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_short8, simd_short8) -> simd_bool](./simd_equal%28_,_%29-4n1gi.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_short8) -> Int16](./simd_reduce_min%28_%29-3ordy.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_short8) -> Int16](./simd_reduce_max%28_%29-55r7y.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_short8) -> Int16](./simd_reduce_add%28_%29-3bda4.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_short8, simd_short8) -> simd_short8](./simd_min%28_,_%29-40hpn.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_short8, simd_short8) -> simd_short8](./simd_max%28_,_%29-1u1su.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_short8) -> simd_bool](./simd_any%28_%29-6pqh3.md)
- [func simd_all(simd_short8) -> simd_bool](./simd_all%28_%29-1ytzd.md)
- [func simd_bitselect(simd_short8, simd_short8, simd_short8) -> simd_short8](./simd_bitselect%28_,_,_%29-1vm6y.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_short8](./vector_short8.md)
### Functions to Create Eight-Element Vectors From Vectors of Other Types
- [simd_short](./simd_short-7008o.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_short](./simd_short-6zqew.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_short](./simd_short-705iw.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_short](./simd_short-6zvaw.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_short](./simd_short-6zxf4.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_short](./simd_short-6zn74.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_short](./simd_short-6zy24.md)
  Returns a new vector from the specified vector of 64-bit, signed integer element.
- [simd_short](./simd_short-6zo8c.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_short](./simd_short-6zrfo.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_short](./simd_short-6zqvg.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_short_sat](./simd_short_sat-31ieh.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-318h5.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-31nk9.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-31de1.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-31khl.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-31ad5.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-31jcj.md)
  Returns a new vector from the specified vector of 64-bit, signed integer element.
- [simd_short_sat](./simd_short_sat-319ir.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-317n3.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_short_sat](./simd_short_sat-3170j.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

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
- [typealias simd_short16](./simd_short16.md)
  A vector of sixteen 16-bit signed integer elements.
- [typealias simd_short32](./simd_short32.md)
  A vector of thirty-two 16-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_short8)*