# simd_char64

**Framework**: simd  
**Kind**: typealias  
**Role**: Type Alias

A vector of sixty-four 8-bit signed integer elements.

## Declaration

```swift
typealias simd_char64 = SIMD64<CChar>
```

```c
typedef char __attribute__((ext_vector_type(64))) simd_char64;
```

## Topics

### Functions to Create Sixty Four-Element Vectors From Other Vectors
- [func simd_make_char64(simd_char2) -> simd_char64](./simd_make_char64%28_%29-mo7n.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_char64(simd_char3) -> simd_char64](./simd_make_char64%28_%29-kchm.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_char64(simd_char4) -> simd_char64](./simd_make_char64%28_%29-18pa1.md)
  Returns a new vector from the specified four-element vector, and other elements set to zero.
- [func simd_make_char64(simd_char8) -> simd_char64](./simd_make_char64%28_%29-1mmet.md)
  Returns a new vector from the specified eight-element vector, and other elements set to zero.
- [func simd_make_char64(simd_char16) -> simd_char64](./simd_make_char64%28_%29-kijk.md)
  Returns a new vector from the specified sixteen-element vector, and other elements set to zero.
- [func simd_make_char64(simd_char32) -> simd_char64](./simd_make_char64%28_%29-747mj.md)
  Returns a new vector from the specified thirty two-element vector, and other elements set to zero.
- [func simd_make_char64(simd_char64) -> simd_char64](./simd_make_char64%28_%29-v4n8.md)
  Returns a new vector from the specified vector.
- [func simd_make_char64(simd_char32, simd_char32) -> simd_char64](./simd_make_char64%28_,_%29.md)
  Returns a new vector from the specified vectors.
- [func simd_make_char64_undef(simd_char2) -> simd_char64](./simd_make_char64_undef%28_%29-9r2mn.md)
  Returns a new vector from the specified two-element vector, and other elements undefined.
- [func simd_make_char64_undef(simd_char3) -> simd_char64](./simd_make_char64_undef%28_%29-9ui3q.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.
- [func simd_make_char64_undef(simd_char4) -> simd_char64](./simd_make_char64_undef%28_%29-cbyu.md)
  Returns a new vector from the specified four-element vector, and other elements undefined.
- [func simd_make_char64_undef(simd_char8) -> simd_char64](./simd_make_char64_undef%28_%29-p5ey.md)
  Returns a new vector from the specified eight-element vector, and other elements undefined.
- [func simd_make_char64_undef(simd_char16) -> simd_char64](./simd_make_char64_undef%28_%29-ax60.md)
  Returns a new vector from the specified sixteen-element vector, and other elements undefined.
- [func simd_make_char64_undef(simd_char32) -> simd_char64](./simd_make_char64_undef%28_%29-5axfx.md)
  Returns a new vector from the specified thirty two-element vector, and other elements undefined.
### Functions to Create Sixty Four-Element Vectors From Scalar Values
- [func simd_make_char64(CChar) -> simd_char64](./simd_make_char64%28_%29-bvt7.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char64_undef(CChar) -> simd_char64](./simd_make_char64_undef%28_%29-2ljie.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
### Common Functions
- [func simd_abs(simd_char64) -> simd_char64](./simd_abs%28_%29-1p85t.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_char64, simd_char64, simd_char64) -> simd_char64](./simd_clamp%28_,_,_%29-6jkxk.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_char64, simd_char64) -> simd_bool](./simd_equal%28_,_%29-8ghe2.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.
### Reduce Functions
- [func simd_reduce_min(simd_char64) -> CChar](./simd_reduce_min%28_%29-jzf5.md)
  Returns the miniumum value in a vector.
- [func simd_reduce_max(simd_char64) -> CChar](./simd_reduce_max%28_%29-mshf.md)
  Returns the maximum value in a vector.
- [func simd_reduce_add(simd_char64) -> CChar](./simd_reduce_add%28_%29-92wpk.md)
  Returns the sum of all elements in a vector.
### Logic and Bitwise Functions
- [func simd_any(simd_char64) -> simd_bool](./simd_any%28_%29-jb9j.md)
- [func simd_all(simd_char64) -> simd_bool](./simd_all%28_%29-2mapx.md)
- [func simd_bitselect(simd_char64, simd_char64, simd_char64) -> simd_char64](./simd_bitselect%28_,_,_%29-2qkxa.md)
  Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.
### Extrema Functions
- [func simd_min(simd_char64, simd_char64) -> simd_char64](./simd_min%28_,_%29-66xtr.md)
  Returns the minimum value of each element in a vector.
- [func simd_max(simd_char64, simd_char64) -> simd_char64](./simd_max%28_,_%29-4dt8v.md)
  Returns the maximum value of each element in a vector.

## See Also

### Vector Data Types
- [typealias simd_char1](./simd_char1.md)
  A vector of one 8-bit signed integer element.
- [typealias simd_char2](./simd_char2.md)
  A vector of two 8-bit signed integer elements.
- [typealias simd_char3](./simd_char3.md)
  A vector of three 8-bit signed integer elements.
- [typealias simd_char4](./simd_char4.md)
  A vector of four 8-bit signed integer elements.
- [typealias simd_char8](./simd_char8.md)
  A vector of eight 8-bit signed integer elements.
- [typealias simd_char16](./simd_char16.md)
  A vector of sixteen 8-bit signed integer elements.
- [typealias simd_char32](./simd_char32.md)
  A vector of thirty-two 8-bit signed integer elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_char64)*