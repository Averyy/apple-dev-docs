# simd_short2

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of two 16-bit signed integer elements.

## Declaration

```swift
typealias simd_short2 = SIMD2<Int16>
```

```c
typedef short __attribute__((ext_vector_type(2))) simd_short2;
```

## Topics

### Functions to Create Two-Element Vectors From Other Vectors
- [func simd_make_short2(simd_short2) -> simd_short2](./simd_make_short2%28_%29-6juuy.md)
  Returns a new vector from the specified vector.
- [func simd_make_short2(simd_short3) -> simd_short2](./simd_make_short2%28_%29-6gmv7.md)
  Returns a new vector by truncating the specified three-element vector.
- [func simd_make_short2(simd_short4) -> simd_short2](./simd_make_short2%28_%29-5z7ps.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_short2(simd_short8) -> simd_short2](./simd_make_short2%28_%29-74zg4.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_short2(simd_short16) -> simd_short2](./simd_make_short2%28_%29-58qns.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_short2(simd_short32) -> simd_short2](./simd_make_short2%28_%29-6bz90.md)
  Returns a new vector by truncating the specified thirty two-element vector.
### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_short2(Int16) -> simd_short2](./simd_make_short2%28_%29-222xa.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_short2(Int16, Int16) -> simd_short2](./simd_make_short2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_short2_undef(Int16) -> simd_short2](./simd_make_short2_undef%28_%29.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_short2) -> simd_short2](./simd_abs%28_%29-88dfi.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_short2, simd_short2, simd_short2) -> simd_short2](./simd_clamp%28_,_,_%29-5qqhe.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_short2, simd_short2) -> simd_bool](./simd_equal%28_,_%29-6gad6.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_short2) -> Int16](./simd_reduce_min%28_%29-49c4w.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_short2) -> Int16](./simd_reduce_max%28_%29-4kmuw.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_short2) -> Int16](./simd_reduce_add%28_%29-2q65m.md)
  Returns the sum of all elements in a vector.
### Extrema Functions
- [func simd_min(simd_short2, simd_short2) -> simd_short2](./simd_min%28_,_%29-13ip4.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_short2, simd_short2) -> simd_short2](./simd_max%28_,_%29-6w9rg.md)
  Returns the maximum value of each element in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_short2) -> simd_bool](./simd_any%28_%29-64jj5.md)
- [func simd_all(simd_short2) -> simd_bool](./simd_all%28_%29-1d5nj.md)
- [func simd_bitselect(simd_short2, simd_short2, simd_short2) -> simd_short2](./simd_bitselect%28_,_,_%29-625jo.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Alternative Type Alias
- [typealias vector_short2](./vector_short2.md)

## See Also

### Vector Data Types
- [typealias simd_short1](./simd_short1.md)
  A vector of one 16-bit signed integer element.
- [typealias simd_short3](./simd_short3.md)
  A vector of three 16-bit signed integer elements.
- [typealias simd_short4](./simd_short4.md)
  A vector of four 16-bit signed integer elements.
- [typealias simd_short8](./simd_short8.md)
  A vector of eight 16-bit signed integer elements.
- [typealias simd_short16](./simd_short16.md)
  A vector of sixteen 16-bit signed integer elements.
- [typealias simd_short32](./simd_short32.md)
  A vector of thirty-two 16-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_short2)*