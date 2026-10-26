# simd_ushort16

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixteen 16-bit unsigned integer elements.

## Declaration

```swift
typealias simd_ushort16 = SIMD16<UInt16>
```

```c
typedef unsigned short __attribute__((ext_vector_type(16))) simd_ushort16;
```

## Topics

### Functions to Create Sixteen-Element Vectors From Other Vectors
- [func simd_make_ushort16(simd_ushort2) -> simd_ushort16](./simd_make_ushort16%28_%29-5h1oe.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_ushort16(simd_ushort3) -> simd_ushort16](./simd_make_ushort16%28_%29-5dtrr.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_ushort16(simd_ushort4) -> simd_ushort16](./simd_make_ushort16%28_%29-4vumc.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_ushort16(simd_ushort8) -> simd_ushort16](./simd_make_ushort16%28_%29-4h3f4.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_ushort16(simd_ushort16) -> simd_ushort16](./simd_make_ushort16%28_%29-43b0g.md)
  Returns a new vector from the specified vector.
- [func simd_make_ushort16(simd_ushort32) -> simd_ushort16](./simd_make_ushort16%28_%29-5wstb.md)
  Returns a new vector by truncating the specified thirty two-element vector.
- [func simd_make_ushort16(simd_ushort8, simd_ushort8) -> simd_ushort16](./simd_make_ushort16%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_ushort16_undef(simd_ushort2) -> simd_ushort16](./simd_make_ushort16_undef%28_%29-3jyo.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_ushort16_undef(simd_ushort3) -> simd_ushort16](./simd_make_ushort16_undef%28_%29-8phl.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_ushort16_undef(simd_ushort4) -> simd_ushort16](./simd_make_ushort16_undef%28_%29-bxgi.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_ushort16_undef(simd_ushort8) -> simd_ushort16](./simd_make_ushort16_undef%28_%29-957cx.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
### Functions to Create Sixteen-Element Vectors From Scalar Values
- [func simd_make_ushort16(UInt16) -> simd_ushort16](./simd_make_ushort16%28_%29-6sqah.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ushort16_undef(UInt16) -> simd_ushort16](./simd_make_ushort16_undef%28_%29-6iivl.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_clamp(simd_ushort16, simd_ushort16, simd_ushort16) -> simd_ushort16](./simd_clamp%28_,_,_%29-5hezy.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_ushort16, simd_ushort16) -> simd_bool](./simd_equal%28_,_%29-9luz4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_ushort16) -> UInt16](./simd_reduce_min%28_%29-3d6c7.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_ushort16) -> UInt16](./simd_reduce_max%28_%29-8isf9.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_ushort16) -> UInt16](./simd_reduce_add%28_%29-7n920.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_ushort16, simd_ushort16) -> simd_ushort16](./simd_min%28_,_%29-99clp.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_ushort16, simd_ushort16) -> simd_ushort16](./simd_max%28_,_%29-1332e.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_ushort16) -> simd_bool](./simd_any%28_%29-938p6.md)
- [func simd_all(simd_ushort16) -> simd_bool](./simd_all%28_%29-iffg.md)
- [func simd_bitselect(simd_ushort16, simd_ushort16, simd_short16) -> simd_ushort16](./simd_bitselect%28_,_,_%29-144l9.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_ushort16](./vector_ushort16.md)

## See Also

### Vector Data Types
- [typealias simd_ushort1](./simd_ushort1.md)
  A vector of one 16-bit unsigned integer element.
- [typealias simd_ushort2](./simd_ushort2.md)
  A vector of two 16-bit unsigned integer elements.
- [typealias simd_ushort3](./simd_ushort3.md)
  A vector of three 16-bit unsigned integer elements.
- [typealias simd_ushort4](./simd_ushort4.md)
  A vector of four 16-bit unsigned integer elements.
- [typealias simd_ushort8](./simd_ushort8.md)
  A vector of eight 16-bit unsigned integer elements.
- [typealias simd_ushort32](./simd_ushort32.md)
  A vector of thirty-two 16-bit unsigned integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_ushort16)*