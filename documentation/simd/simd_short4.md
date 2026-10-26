# simd_short4

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of four 16-bit signed integer elements.

## Declaration

```swift
typealias simd_short4 = SIMD4<Int16>
```

```c
typedef short __attribute__((ext_vector_type(4))) simd_short4;
```

## Topics

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_short4(simd_short2) -> simd_short4](./simd_make_short4%28_%29-6bvw4.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_short4(simd_short3) -> simd_short4](./simd_make_short4%28_%29-68qml.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_short4(simd_short4) -> simd_short4](./simd_make_short4%28_%29-662gm.md)
  Returns a new vector from the specified vector.
- [func simd_make_short4(simd_short8) -> simd_short4](./simd_make_short4%28_%29-5rbcq.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_short4(simd_short16) -> simd_short4](./simd_make_short4%28_%29-9muje.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_short4(simd_short32) -> simd_short4](./simd_make_short4%28_%29-7tcxn.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_short4(simd_short2, simd_short2) -> simd_short4](./simd_make_short4%28_,_%29-8h120.md)
  Returns a new vector from the specified vectors.
- [func simd_make_short4_undef(simd_short2) -> simd_short4](./simd_make_short4_undef%28_%29-8g0xr.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_short4_undef(simd_short3) -> simd_short4](./simd_make_short4_undef%28_%29-8imcm.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [vector4](./vector4-5h3is.md)
  Returns a new vector from the specified vectors.
### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_short4(Int16) -> simd_short4](./simd_make_short4%28_%29-1emve.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_short4(Int16, Int16, Int16, Int16) -> simd_short4](./simd_make_short4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_short4_undef(Int16) -> simd_short4](./simd_make_short4_undef%28_%29-36i14.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [vector4](./vector4-42vpa.md)
  Returns a new vector from the specified scalar values.
### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_short4(simd_short2, Int16, Int16) -> simd_short4](./simd_make_short4%28_,_,_%29-6v1lj.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_short4(simd_short3, Int16) -> simd_short4](./simd_make_short4%28_,_%29-8tpr6.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_short4(Int16, Int16, simd_short2) -> simd_short4](./simd_make_short4%28_,_,_%29-34dcj.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_short4(Int16, simd_short2, Int16) -> simd_short4](./simd_make_short4%28_,_,_%29-21v12.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_short4(Int16, simd_short3) -> simd_short4](./simd_make_short4%28_,_%29-46aby.md)
  Returns a new vector from a scalar value and a vector.
- [vector4](./vector4-8l9kg.md)
  Returns a new vector from a vector and a scalar value.
### Common Functions
- [func simd_abs(simd_short4) -> simd_short4](./simd_abs%28_%29-81n9o.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_short4, simd_short4, simd_short4) -> simd_short4](./simd_clamp%28_,_,_%29-3fip1.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_short4, simd_short4) -> simd_bool](./simd_equal%28_,_%29-51wsu.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_short4) -> Int16](./simd_reduce_min%28_%29-4uj62.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_short4) -> Int16](./simd_reduce_max%28_%29-4qgga.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_short4) -> Int16](./simd_reduce_add%28_%29-2y9o8.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_short4, simd_short4) -> simd_short4](./simd_min%28_,_%29-3w6s9.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_short4, simd_short4) -> simd_short4](./simd_max%28_,_%29-7xxnr.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_short4) -> simd_bool](./simd_any%28_%29-6cn5f.md)
- [func simd_all(simd_short4) -> simd_bool](./simd_all%28_%29-1k2rx.md)
- [func simd_bitselect(simd_short4, simd_short4, simd_short4) -> simd_short4](./simd_bitselect%28_,_,_%29-u3k7.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_short4](./vector_short4.md)
### Functions to Create Four-Element Vectors From Vectors of Other Types
- [simd_short](./simd_short-6kz7g.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_short](./simd_short-6l9fg.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_short](./simd_short-6kubg.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_short](./simd_short-6l458.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_short](./simd_short-6kwdg.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_short](./simd_short-6l678.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_short](./simd_short-6kus0.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_short](./simd_short-6l4k0.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_short](./simd_short-6l7r4.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_short](./simd_short-6l78g.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.
### Functions to Perform Saturating Conversion From Vectors of Other Types
- [simd_short_sat](./simd_short_sat-3gjfp.md)
  Returns a new vector from the specified vector of 8-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-3g9id.md)
  Returns a new vector from the specified vector of 8-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-3geh1.md)
  Returns a new vector from the specified vector of 16-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-3g4p1.md)
  Returns a new vector from the specified vector of 16-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-3glj1.md)
  Returns a new vector from the specified vector of 32-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-3gblp.md)
  Returns a new vector from the specified vector of 32-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-3gn33.md)
  Returns a new vector from the specified vector of 64-bit, signed integer elements.
- [simd_short_sat](./simd_short_sat-3gcwv.md)
  Returns a new vector from the specified vector of 64-bit, unsigned integer elements.
- [simd_short_sat](./simd_short_sat-3gb7n.md)
  Returns a new vector from the specified vector of 32-bit, floating-point elements.
- [simd_short_sat](./simd_short_sat-3ganz.md)
  Returns a new vector from the specified vector of 64-bit, floating-point elements.

## See Also

### Vector Data Types
- [typealias simd_short1](./simd_short1.md)
  A vector of one 16-bit signed integer element.
- [typealias simd_short2](./simd_short2.md)
  A vector of two 16-bit signed integer elements.
- [typealias simd_short3](./simd_short3.md)
  A vector of three 16-bit signed integer elements.
- [typealias simd_short8](./simd_short8.md)
  A vector of eight 16-bit signed integer elements.
- [typealias simd_short16](./simd_short16.md)
  A vector of sixteen 16-bit signed integer elements.
- [typealias simd_short32](./simd_short32.md)
  A vector of thirty-two 16-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_short4)*